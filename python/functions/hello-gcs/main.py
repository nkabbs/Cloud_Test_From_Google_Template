#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functions_framework
import json
from google.events.cloud.storage_v1 import StorageObjectData

# Register a CloudEvent function with the Functions Framework
@functions_framework.cloud_event
def hello_gcs(cloud_event):
  print(f"Event ID: {cloud_event['id']}")
  print(f"Event Type: {cloud_event['type']}")

  storage_object_data = StorageObjectData.from_json(json.dumps(cloud_event.data))
  print(f"Bucket: {storage_object_data.bucket}")
  print(f"File: {storage_object_data.name}")
  print(f"Metageneration: {storage_object_data.metageneration}")
  print(f"Created: {storage_object_data.time_created}")
  print(f"Updated: {storage_object_data.updated}")
