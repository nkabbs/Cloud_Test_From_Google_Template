#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functions_framework
import json
from google.events.cloud import audit_v1

# Register a CloudEvent function with the Functions Framework
@functions_framework.cloud_event
def hello_auditlog(cloud_event):
  print(f"Event ID: {cloud_event['id']}")
  print(f"Event Type: {cloud_event['type']}")

  log_entry_data = audit_v1.LogEntryData.from_json(json.dumps(cloud_event.data))
  payload = log_entry_data.proto_payload
  if payload:
    print(f"ServiceName: {payload.service_name}")
    print(f"MethodName: {payload.method_name}")
    print(f"ResourceName: {payload.resource_name}")