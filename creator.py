def create_request(request_type, text):
    if request_type == "ner":
        request_url = "/microservices/nlp/namedentityrecognition/v1/getpredictions"
    return request_url
