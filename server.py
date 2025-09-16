# Final project

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Format the dictionary output without its curly brackets
    my_list = []
    for key, value in response.items():
        if key != 'dominant_emotion':
            my_list.append(f"'{key}': {value}")
    emotions_list = ", ".join(my_list)
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotions list and dominant emotion
    return "For the given statement, the system response is " + emotions_list + ". The dominant emotion is {}.".format(dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)