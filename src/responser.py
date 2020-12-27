from src import requester, db_actions


def respond(intent, data):
    data_params = data["queryResult"]["parameters"]
    str_message = "Sorry, unable to understand you for this moment. Please try again later."
    if intent == "fill_profile":
        str_message = "Your profile has been built with role as " + str(data_params["role"])\
                      + ", experience in years "+ str(data_params["duration"]["amount"])+" and education as " + str(data_params["education"])+" ."
    if intent == "job_search":
        type_job = "default"
        str_message = db_actions.dummy_db(type_job, data_params["geo-city"])
    if intent == "display_next":
        type_job = "next"
        str_message = db_actions.dummy_db(type_job)
    if intent == "profile_summary":
        str_message = requester.get_result(data["queryResult"]["queryText"])
    return send_message(str_message)


def send_message(status):
    result = {
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": status
                            }
                        }
                    ]
                }
            }
        }
    }

    return result


