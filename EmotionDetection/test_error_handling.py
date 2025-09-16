"""
Final project
The functions of Watson AI libraries are deployed on IBM's Cloud IDE server, 
    and cannot be imported here.
Test for error handling of invalid entry
"""
import requests  # Import the requests library to handle HTTP requests

# URL of the emotion detection service
url = (
    'https://sn-watson-emotion.labs.skills.network/v1/'
    'watson.runtime.nlp.v1/NlpService/EmotionPredict'
)
# Set the headers required for the API request
header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
# Define the first payload with blank entry to test the API
myobj = { "raw_document": { "text": "" } }  
# Send a POST request to the API with the first payload and headers
response = requests.post(url, json = myobj, headers=header, timeout=5)  
# Print the status code of the first response
print(response.status_code)

# Define the second payload with meaningful text to test the API
myobj = { "raw_document": { "text": "Testing this application for error handling" } }
# Send a POST request to the API with the second payload and headers
response = requests.post(url, json = myobj, headers=header, timeout=5) 
# Print the status code of the first response
print(response.status_code)