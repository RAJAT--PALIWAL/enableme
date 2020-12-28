import config as cf
import http.client
import logging
import json
import os


def get_result(text):
    conn = http.client.HTTPSConnection("apis.sentient.io")
    payload_dict= {"text": text}
    payload = json.dumps(payload_dict)
    headers = {
        'content-type': "application/json",
        'x-api-key': 'F8F46ADEA3FB43888344'
    }
    conn.request("POST", "/microservices/nlp/namedentityrecognition/v1/getpredictions", payload, headers)

    res = conn.getresponse()
    status = res.status
    if status == 200:
        data = res.read()
        response = get_responses(json.loads(data.decode("utf-8")))
        return response
    else:
        logging.error("Failed to call sentient NLP API")
        return "Sorry, Could you please rephrase."


def callBase64():

    conn = http.client.HTTPSConnection("apis.sentient.io")

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"filePath\"\r\n\r\n"+str(os.path.join(cf.ABS_PATH, "audio.wav"))+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"format\"\r\n\r\njson\r\n-----011000010111000001101001--\r\n\r\n"

    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-api-key': "F8F46ADEA3FB43888344"
    }

    conn.request("POST", "/microservices/utility/base64encode/v0/getresults", payload, headers)

    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data.decode("utf-8"))
    encodedString = json_data["results"]["base64"]["file"]["data"]
    callSpeech2Text(conn, encodedString)


def callSpeech2Text(encodedString):
    payload_dict = {"model":"news_parliament","file_type":"wav","threshold":0.4}
    payload_dict["wav_base64"] = encodedString

    payload = json.dumps(payload_dict)

    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-api-key': "F8F46ADEA3FB43888344"
    }
    conn = http.client.HTTPSConnection("apis.sentient.io")
    conn.request("POST", "/microservices/voice/vadasr/v1/getpredictions", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def get_responses(data_dict):

    str_message = "Awesome, we have built your profile and noted down some important details."
    try:
        for key, val in data_dict["results"].items():
            if key == "per":
                str_message = str_message + " Name as "+ str(val[0]) + " ."
            if key == "org":
                str_message = str_message + " Company as " + str(val[0]) + " ."
            if key == "loc":
                str_message = str_message + " Location as " + str(val[0]) + " ."
    except Exception as error:
        logging.error(str(error))
    return str_message


if __name__ == "__main__":
    callBase64()