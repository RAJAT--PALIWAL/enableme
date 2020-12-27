import config as cf
import http.client


def get_result(request_url, text):
    conn = http.client.HTTPSConnection("apis.sentient.io")
    payload = "{\"text\":text}"

    headers = {
        'content-type': "application/json",
        'x-api-key': cf.API_KEY
    }

    conn.request("POST", request_url, payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
