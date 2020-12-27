from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/assist", methods=['GET', 'POST'])
def assist():
    bin_data = request.data
    data = json.loads(bin_data.decode())
    intent_name = data["queryResult"]["intent"]["displayName"]

    return


if __name__ == "__main__":
    app.run()
