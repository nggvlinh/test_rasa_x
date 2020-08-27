import random
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher
import gc
from rasa_sdk.forms import FormAction

import pandas as pd
from urllib.request import urlopen
import json
import numpy as np



def load_button():
    button_lst = []

    button_lst.append({
        "type": "postback",
        "title": "Xem điểm số",
        "payload": "Xem điểm"
    })

    return button_lst

def TorF(t):
    if (t):
        return 1
    return 0

def convert_(i):
  if (i=='1'):
    return "Đậu" 
  return "Rớt"

def convert_t(i):
  if (i=='-1.00'):
    return "Bỏ thi"
  return i

class act_unknown(Action):

    def name(self) -> Text:
        return "act_unknown"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        temp_button_lst = load_button()
        dispatcher.utter_message(text="Xin chào tôi là trợ lý ảo của CUSC. Bạn có muốn biết gì về điểm số không?",buttons=temp_button_lst)
        del temp_button_lst
        gc.collect()
        return []

class score_tution(Action):

    def name(self) -> Text:
        return "get_score_tuition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Vui lòng điền thêm thông tin cần thiết: mã số sinh viên")

        return []

class act_greet(Action):

    def name(self) -> Text:
        return "greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        temp_button_lst = load_button()
        dispatcher.utter_message(text="Xin chào tôi là trợ lý ảo của CUSC. Bạn có muốn biết gì về điểm số không?", buttons=temp_button_lst)
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
        print(user_name)
        print(user_card)

        array_api = "https://qldt.cusc.vn/public/api/DiemThi?SV_MSSV="+user_name+"&SV_SOCMND="+user_card 
        
        response_score = urlopen(array_api)
        data_score = json.load(response_score)
        tn = ""
        td = ""
        kq = ""
        if (TorF(data_score)):
            for i in data_score:
                tn = i['MH_TEN']
                td = i["THI_DIEM"]
                kq = i["THI_KQ"]
                print(type(kq))
                dispatcher.utter_message(tn)
                dispatcher.utter_message(convert_t(td))
                dispatcher.utter_message(convert_(kq))
                dispatcher.utter_message("------------------")

        else : dispatcher.utter_message("Xin lỗi không tìm thấy thông tin sinh viên vui lòng nhập lại")
        return []





