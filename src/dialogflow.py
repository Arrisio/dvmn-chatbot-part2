import google.auth


def detect_intent_texts(
    texts, project_id=google.auth.default()[1], session_id=0, language_code="ru"
):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    import dialogflow_v2 as dialogflow

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        return session_client.detect_intent(session=session, query_input=query_input)


def get_response_text(income_text: str) -> str:
    return detect_intent_texts([income_text]).query_result.fulfillment_text
