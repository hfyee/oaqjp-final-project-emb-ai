"""
Final project
The functions of Watson AI libraries are deployed on IBM's Cloud IDE server, 
    and cannot be imported here.
"""
import json
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """
    Takes a string input (text_to_analyse)
    """
    # URL of the emotion prediction service
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=5)

    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the set of emotions and their scores from the response
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions_dict = {
            'anger': anger_score, 
            'disgust': disgust_score, 
            'fear': fear_score, 
            'joy': joy_score, 
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)

     # If the response status code is 400 for blank entries, set the values for all keys to None
    elif response.status_code == 400:
        emotions_dict = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None
        }
        dominant_emotion = None
    
    emotions_dict.update({'dominant_emotion': dominant_emotion})

    # Return a dictionary containing emotion detection results
    return emotions_dict
