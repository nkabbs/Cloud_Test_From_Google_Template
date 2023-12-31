// Copyright 2023 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

'use strict';

const express = require('express');
const { HTTP } = require("cloudevents");
const {toMessagePublishedData} = require('@google/events/cloud/pubsub/v1/MessagePublishedData');

const app = express();

app.use(express.json());

app.post('/', (req, res) => {

  const cloudEvent = HTTP.toEvent({ headers: req.headers, body: req.body });
  //console.log(cloudEvent);

  console.log(`Event ID: ${cloudEvent.id}`);
  console.log(`Event Type: ${cloudEvent.type}`);

  const messagePublishedData = toMessagePublishedData(cloudEvent.data);

  const base64Data = messagePublishedData.message.data;
  const textData = base64Data ? Buffer.from(base64Data, 'base64').toString() : '';
  console.log(`TextData: ${textData}`);
  console.log(`Subscription: ${cloudEvent.data.subscription}`);

  res.status(204).send();
});

const port = parseInt(process.env.PORT) || 8080;
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});