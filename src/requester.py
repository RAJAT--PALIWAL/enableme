import config as cf
import http.client
import logging
import json


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
    get_result("My name is Rajat and I live in Pune")