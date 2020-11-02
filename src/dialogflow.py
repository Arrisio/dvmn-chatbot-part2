from typing import Union, NoReturn

import google.auth
from loguru import logger


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


def get_response_text(
    income_text: str, session_id=0, skip_if_not_understand: bool = False
) -> Union[str, NoReturn]:
    response = detect_intent_texts([income_text], session_id=session_id)
    logger.debug(
        "receive deialogflow intend",
        extra={
            "is_fallback": response.query_result.intent.is_fallback,
            "fulfillment_text": response.query_result.fulfillment_text,
        },
    )
    if skip_if_not_understand and response.query_result.intent.is_fallback:
        return

    return response.query_result.fulfillment_text
