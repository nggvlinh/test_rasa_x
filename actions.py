import random
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher
import gc
from rasa_sdk.forms import FormAction


def load_button():
    button_lst = []

    button_lst.append({
        "type": "postback",
        "title": "Xem điểm số",
        "payload": "Xem điểm"
    })
    button_lst.append({
        "type": "postback",
        "title": "Xem tình trạng học phí",
        "payload": "xem học phí"
    })
    return button_lst


class act_unknown(Action):

    def name(self) -> Text:
        return "act_unknown"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        temp_button_lst = load_button()
        dispatcher.utter_message(text="Xin chào tôi là trợ lý ảo của CUSC. Bạn có muốn biết gì về điểm số hay tình trạng học phí hay không?",buttons=temp_button_lst)
        del temp_button_lst
        gc.collect()
        return []

class score_tution(Action):

    def name(self) -> Text:
        return "get_score_tuition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Vui lòng điền thêm thông tin cần thiết: tên đầy đủ")

        return []

class act_greet(Action):

    def name(self) -> Text:
        return "greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        temp_button_lst = load_button()
        dispatcher.utter_message(text="Xin chào tôi là trợ lý ảo của CUSC. Bạn có muốn biết gì về điểm số hay tình trạng học phí hay không?", buttons=temp_button_lst)
        del temp_button_lst
        gc.collect()

        return []


class show_info(Action):

    def name(self) -> Text:
        return "submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot('name')
        user_card = tracker.get_slot('card')
        dispatcher.utter_message("Thông tin điểm của {} ".format(user_name))

        dispatcher.utter_message("Thông tin học phí của {} ".format(user_name))

        return []





