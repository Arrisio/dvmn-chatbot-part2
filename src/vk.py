from loguru import logger
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

from src.dialogflow import get_response_text


def answer_vk_message(event, vk):
    if text := get_response_text(
        event.text, session_id=event.user_id, skip_if_not_understand=True
    ):
        vk.messages.send(
            user_id=event.user_id,
            message=text,
            random_id=random.randint(1, 1000),
        )


def main():
    vk_session = vk_api.VkApi(token=os.environ["VK_TOKEN"])
    longpoll = VkLongPoll(vk=vk_session)
    vk = vk_session.get_api()

    for event in longpoll.listen():
        # if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.type == VkEventType.MESSAGE_NEW:
            logger.info(
                "Income message", extra={"user_id": event.user_id, "text": event.text}
            )
            answer_vk_message(event, vk)


def run_vk_bot():
    logger.info("vk bot started")
    try:
        main()
    except (KeyboardInterrupt, SystemExit) as err:
        logger.info(f"shutting down.. {err}")

    logger.info("vk bot stopped")


if __name__ == "__main__":
    main()