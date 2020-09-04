# get the summary of a long text via its ID
#
# at http://127.0.0.1:8000/docs we see the cURL command needed:
# curl -X GET "http://127.0.0.1:8000/summaries/1" -H  "accept: application/json"
#
# the cURL-to-Python translator at https://curl.trillworks.com/#python then got us the basis for this script:
from pprint import pprint
import sys
import requests

if len(sys.argv) < 1:
    quit('Please specify the document ID. Exiting ...')
    
document_id = int(sys.argv[1])

headers = {
    'accept': 'application/json',
}

response = requests.get(f'http://127.0.0.1:8000/summaries/{document_id}', headers=headers)
pprint(response.json())
