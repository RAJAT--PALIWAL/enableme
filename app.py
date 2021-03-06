from flask import Flask, render_template, request, jsonify
import json
import logging
from src import responser, requester

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        requester.callBase64()
        return render_template('profile.html', request="POST")
    else:
        return render_template('profile.html')


@app.route('/record', methods=['GET', 'POST'])
def record():
    return render_template('recorder.html')


@app.route("/assist", methods=['GET', 'POST'])
def assist():
    bin_data = request.data
    data = json.loads(bin_data.decode())
    intent_name = data["queryResult"]["intent"]["displayName"]
    result = responser.respond(intent_name, data)
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    logging.info('App is running successfully')
    app.run()
