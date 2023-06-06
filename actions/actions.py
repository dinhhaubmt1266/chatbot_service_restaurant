from ast import Pass
import re
from tkinter import N
from typing import Any, Text, Dict, List
from aiohttp import TraceResponseChunkReceivedParams
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
from actions.time_handle import *
from actions.connectMySQL import *

menu = {"1": "Baba hầm hải vị kèm bánh mì",
        "2": "Bào ngư hầm nấm đông cô và cải thìa",
        "3": "Bánh cam chiên với nước cốt dừa",
        "4": "Bánh kem mềm chanh dây, trái cây, vụn hạt dẻ, xốt rượu Malibu",
        "5": "Bánh mochi",
        "6": "Bánh su với kem phomai hạt dẻ",
        "7": "Bánh tiramisu",
        "8": "Bánh xốp Macaron vị trà xanh",
        "9": "Bò nấu cay kiểu Mã Lai kèm bánh mì",
        "10": "Bò sốt vang Marzano",
        "11": "Bò úc áp chảo",
        "12": "Bồ câu tiềm thảo mộc hạt sen",
        "13": "Chem chép New Zealand sốt tiêu",
        "14": "Chân ngỗng sò điệp sốt bào ngư",
        "15": "Chè hạnh nhân tàu hũ với long nhãn",
        "16": "Càng cua bách hoa",
        "17": "Cá hồi nướng mè",
        "18": "Cừu hầm ngũ vị, cari hành tím, tỏi đen, nấm truffle và sốt tiêu Phú Quốc",
        "19": "Ghẹ rang muối kiểu Âu",
        "20": "Gà hấp đông cô sốt bào ngư",
        "21": "Gỏi hải sâm kèm bánh phồng tôm",
        "22": "Heo sữa quay kèm bánh mỳ",
        "23": "Nem nướng cuốn cá hồi và trứng cá đen",
        "24": "Salad cá ngừ",
        "25": "Salad hoàng đế",
        "26": "Salad trái cây tươi & vani",
        "27": "Sushi thập cẩm",
        "28": "Súp bào ngư & cua măng tây",
        "29": "Súp bào ngư phú quý",
        "30": "Súp cua & bong bóng cá",
        "31": "Súp cua bể hải sâm",
        "32": "Súp hải sản & nấm linh chi",
        "33": "Súp hải sản hoàng kim",
        "34": "Súp nghêu kem sữa",
        "35": "Súp rau củ kiểu Ý",
        "36": "Sườn non chiên Trung Hoa",
        "37": "Thăn bò mỹ sốt tiêu",
        "38": "Thạch xoài ăn kèm sữa dừa",
        "39": "Trái vải hạnh nhân lạnh",
        "40": "Tôm càng nướng wasabi",
        "41": "Tôm càng rang muối Hồng Kông",
        "42": "Tôm hùm nửa con đút lò kiểu Pháp",
        "43": "Tôm xào miến Hồng Kông",
        }

list_food_order = {}

list_time_using = {
    "time": "",
    "day": "",
    "month": "",
    "year": ""
}

information_customer = {
                    "name_customer": "",
                    "phone_number_customer": "",
                    "quatity_people_using": "",
                    "time_using_customer": list_time_using,
                    "list_food_order": list_food_order
}

infor_customer_need_change = None
infor_food_need_change = None


# class ActionWelcome(Action):
#     def name(self):
#         return 'action_welcome'

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_id = (tracker.current_state())["sender_id"]

#         utterself = "em"

#         if sexual is None:
#             sexual = "quý khách"

#         dispatcher.utter_message(response="utter_welcome", sexual=sexual)
#         return [SlotSet("utterself", utterself)]


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]

        global list_food_order
        global list_time_using
        global information_customer
        global infor_customer_need_change
        global infor_food_need_change

        list_food_order = {}

        list_time_using = {
            "time": "",
            "day": "",
            "month": "",
            "year": ""
        }

        information_customer = {
                            "name_customer": "",
                            "phone_number_customer": "",
                            "quatity_people_using": "",
                            "time_using_customer": list_time_using,
                            "list_food_order": list_food_order
        }

        infor_customer_need_change = None
        infor_food_need_change = None

        dispatcher.utter_message(response="utter_greet")
        dispatcher.utter_message(response="utter_question_service")

        return []


class ActionAskService(Action):
    def name(self) -> Text:
        return "ask_name_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        service = tracker.get_slot("service")

        if service is None:
            dispatcher.utter_message(response="utter_question_service")
        else:
            dispatcher.utter_message(response="utter_display_menu")
            dispatcher.utter_message(response="utter_request_choice_food")

        return [SlotSet("service", service)]


class ActionGetNameFood(Action):
    def name(self) -> Text:
        return "get_name_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        name_food = tracker.get_slot("name_food")
        if name_food not in menu.values():
            dispatcher.utter_message(text="Món ăn quý khách chọn không có trong thực đơn của nhà hàng chúng tôi. Quý khách vui lòng chọn lại!")
            return [SlotSet("name_food", None)]
        else:
            return [SlotSet("name_food", name_food)]


class ActionAskChoiceFood(Action):
    def name(self) -> Text:
        return "question_quantity_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        name_food = tracker.get_slot("name_food")
        if name_food != None:
            dispatcher.utter_message(response="utter_ask_quantity_food")
        return []


class ActionAskAddFood(Action):
    def name(self) -> Text:
        return "question_add_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        dispatcher.utter_message(response="utter_ask_add_food")
        name_food = tracker.get_slot("name_food")
        quantity_food = tracker.get_slot("quantity_food")
        list_food_order[name_food] = quantity_food
        return [SlotSet("quantity_food", quantity_food)]


def display_list_food(list_food):
    text_list_food = "Các món ăn quý khách đã đặt: \n"
    for i in list_food:
            if list_food[i] != None:
                text_list_food += str(i) + " : " + str(list_food[i]) + " phần \n" 
    return text_list_food

class ActionDisplayFood(Action):
    def name(self) -> Text:
        return "display_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quantity_food = tracker.get_slot("quantity_food")
        user_id = (tracker.current_state())["sender_id"]
        text_list_food = display_list_food(list_food_order)
        if infor_food_need_change == None and error_infor_food_change == None:
            dispatcher.utter_message(text = text_list_food)
            dispatcher.utter_message(text = "Quý khách vui lòng kiểm tra lại danh sách các món quý khách đã chọn đúng chưa ạ?.")
        else:
            dispatcher.utter_message(text = text_list_food)
        return []
       
class ActionQuestionInforFoodChange(Action): 
    def name(self) -> Text:
        return "question_infor_food_change"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        if infor_food_need_change == None:
            dispatcher.utter_message(text = "Quý khách muốn thay đổi món ăn, thay đổi số phần món ăn hay hủy món ăn?")
        else:
            return []

infor_food_change = None
error_infor_food_change = None

class ActionGetInforChangeFood(Action): 
    def name(self) -> Text:
        return "get_infor_change_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        infor_food_change = tracker.get_slot("infor_food_change")
        global infor_food_need_change
        global error_infor_food_change
        error_infor_food_change = None
        infor_food_need_change = infor_food_change
        return [SlotSet("infor_food_change", infor_food_change)]
    
class ActionQuestionFoodChange(Action): 
    def name(self) -> Text:
        return "question_food_change"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        if infor_food_need_change == "name_food_change":
            dispatcher.utter_message(text = "Quý khách muốn thay đổi món nào trong danh sách thành món nào trong thực đơn của nhà hàng ạ?")
        elif infor_food_need_change == "quantity_food_change":
            dispatcher.utter_message(text = "Quý khách muốn thay đổi số lượng của món ăn nào trong danh sách các món của quý khách đã chọn với số lượng bao nhiêu?")
        elif infor_food_need_change == "delete_food":
            dispatcher.utter_message(text = "Quý khách muốn hủy món ăn nào ạ?")
        else:
            dispatcher.utter_message(text = "Quý khách có thể nhắc lại không ạ?")
        return []

class ActionChangeListFood(Action):
    def name(self) -> Text:
        return "change_list_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        global infor_food_need_change
        global list_food_order
        
        if infor_food_need_change == "name_food_change":
            name_food_delete = tracker.get_slot("name_food_delete")
            name_food = tracker.get_slot("name_food")
            if name_food_delete not in list_food_order.keys() or list_food_order[name_food_delete] == None:
                dispatcher.utter_message(text="Tên món quý khách muốn thay đổi không có trong danh sách món ăn quý khách đã chọn. Quý khách vui lòng nhập lại!")
            elif name_food not in menu.values():
                dispatcher.utter_message(text="Tên món quý khách chọn không có trong thực đơn của nhà hàng chúng tôi. Quý khách vui lòng nhập lại!")
            else:
                list_food_order[name_food] = None;
                list_food_order[name_food] = list_food_order[name_food_delete]
                list_food_order[name_food_delete] = None
                infor_food_need_change = None
                # dispatcher.utter_message(text = "Thông tin món ăn của quý khách đã đươc thay đổi")

        elif infor_food_need_change == "quantity_food_change":
            name_food = tracker.get_slot("name_food")
            if name_food not in list_food_order.keys() or list_food_order[name_food] == None:
                dispatcher.utter_message(text="Tên món quý khách muốn thay đổi không có trong danh sách món ăn quý khách đã chọn. Quý khách vui lòng nhập lại!")
                # text_list_food = display_list_food(list_food_order)
                # dispatcher.utter_message(text = text_list_food)
            else:
                quantity_food = tracker.get_slot("quantity_food")
                list_food_order[name_food] = quantity_food
                infor_food_need_change = None
                # dispatcher.utter_message(text = "Thông tin món ăn của quý khách đã đươc thay đổi")

        elif infor_food_need_change == "delete_food":
            name_food_delete = tracker.get_slot("name_food_delete")
            if name_food_delete not in list_food_order.keys() or list_food_order[name_food_delete] == None:
                dispatcher.utter_message(text="Tên món quý khách muốn thay đổi không có trong danh sách món ăn quý khách đã chọn. Quý khách vui lòng nhập lại!")
                # text_list_food = display_list_food(list_food_order)
                # dispatcher.utter_message(text = text_list_food)
            else:
                list_food_order[name_food_delete] = None
                infor_food_need_change = None
                # dispatcher.utter_message(text = "Thông tin món ăn của quý khách đã đươc thay đổi")
        elif infor_food_need_change == None:
            global error_infor_food_change
            error_infor_food_change = True
            dispatcher.utter_message(text = "Quý khách muốn thay đổi món ăn, thay đổi số phần món ăn hay hủy món ăn?")

class ActionGiveAnouUpdateListFood(Action):
    def name(self) -> Text:
        return "give_anou_updated_list_food"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        if infor_food_need_change == None and error_infor_food_change == None:
            dispatcher.utter_message(text = "Thông tin món ăn của quý khách đã đươc thay đổi")
        else:
            return []

class ActionQuestionQuantityPeople(Action):
    def name(self) -> Text:
        return "question_quantity_people"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        global information_customer
        information_customer["list_food_order"] = list_food_order
        dispatcher.utter_message(response="utter_ask_quantity_people")


class ActionAskTimeUsing(Action):
    def name(self) -> Text:
        return "get_quantity_people"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        quantity_people = tracker.get_slot("quantity_people")
        dispatcher.utter_message(response="utter_ask_timeday")
        global information_customer
        information_customer['quatity_people_using'] = quantity_people
        return [SlotSet("quantity_people", quantity_people)]


class ActionGetTime(Action):
    def name(self) -> Text:
        return "get_time_using"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]

        Date = datetime.now()
        str_year = tracker.get_slot("year")
        str_month = tracker.get_slot("month")
        str_day = tracker.get_slot("day")
        str_time = tracker.get_slot("time")

        if str_year is not None:
            Date = year_format(year=str_year, Date=Date)
        if str_month is not None:
            Date = month_format(month=str_month, Date=Date)
        if str_day is not None:
            Date = day_format(day=str_day, Date=Date)
        if str_time is not None:
            Date = time_format(time=str_time, Date=Date)
        else:
            dispatcher.utter_message(response="utter_ask_timeday")

        if Date == datetime.now():
            dispatcher.utter_message(response="utter_ask_timeday")

        else:
            time = str(Date.time().replace(microsecond=0))
            day = str(Date.day)
            month = str(Date.month)
            year = str(Date.year)
            print(time, "-", day, "-", month, "-", year)
            # sexual = tracker.get_slot("sexual")
            service = tracker.get_slot("service")
        
        global list_time_using
        list_time_using["time"] = time
        list_time_using["day"] = day
        list_time_using["month"] = month
        list_time_using["year"] = year

        global information_customer
        information_customer["time_using_customer"] = list_time_using

        return [SlotSet("time", time), SlotSet("day", day),
                SlotSet("month", month), SlotSet("year", year)]


class ActionAskName(Action):
    def name(self) -> Text:
        return "ask_name_customer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]

        dispatcher.utter_message(response="utter_display_time_table")
        # dispatcher.utter_message(text= tracker.get_slot("time") + ' ' + tracker.get_slot("day"))
        # dispatcher.utter_message(text= list_time_using["time"] + ' ' + list_time_using["day"])
        dispatcher.utter_message(response="utter_ask_name")

        return []


class ActionGetName(Action):
    def name(self) -> Text:
        return "get_name_customer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        name_customer = tracker.get_slot("name_customer")
        dispatcher.utter_message(response="utter_ask_phone_number")
        global information_customer
        information_customer["name_customer"] = name_customer
        return [SlotSet("name_customer", name_customer)]


class ActionAskNumberphone(Action):
    def name(self) -> Text:
        return "get_phone_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]

        phone_number = tracker.get_slot("phone_number")
        global information_customer
        information_customer["phone_number_customer"] = phone_number
        return [SlotSet("phone_number", phone_number)]


class ActionDisplayInformation(Action):
    def name(self) -> Text:
        return "display_information_customer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        name = information_customer["name_customer"]
        phone_number = information_customer['phone_number_customer']
        quantity_people = information_customer["quatity_people_using"]
        time = list_time_using["time"]
        day = list_time_using["day"]
        month = list_time_using["month"]
        year = list_time_using["year"]

        dispatcher.utter_message(text="Thông tin của quý khách đã được cập nhập")
        dispatcher.utter_message(text="Tên quý khách: " + str(name))
        dispatcher.utter_message(text="Số điện thoại quý khách: " + str(phone_number))
        dispatcher.utter_message(text="Số lượng người dự tiệc: " + str(quantity_people))
        dispatcher.utter_message(text="Thời gian quý khách sử dụng: " + str(time) + " - " + str(day) + " - " + str(month) + " - " + str(year))
        text_list_food = display_list_food(list_food_order)
        dispatcher.utter_message(text = text_list_food)
        dispatcher.utter_message(response="utter_ask_confirm")

        return []
    
class ActionQuestionInforChange(Action):
    def name(self) -> Text:
        return "question_infor_change"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        dispatcher.utter_message(text = "quý khách muốn thay đổi tên, số điện thoại, số lượng người tham gia hay thời gian sử dụng?")

        return []
    
class ActionGetInforChange(Action):
    def name(self) -> Text:
        return "get_infor_change"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        infor_change = tracker.get_slot("infor_change")
        global infor_customer_need_change
        infor_customer_need_change = infor_change

        return []
    
class ActionQuestionInforChangeOfCustomer(Action):
    def name(self) -> Text:
        return "question_infor_change_of_customer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]

        if infor_customer_need_change == "name_customer":
            dispatcher.utter_message(text = "Quý khách vui lòng cho biết lại tên của quý khách: ")
        elif infor_customer_need_change == "phone_number":
            dispatcher.utter_message(text = "Quý khách vui lòng cho biết lại số điện thoại của quý khách: ")
        elif infor_customer_need_change == "quantity_people":
            dispatcher.utter_message(text = "Quý khách vui lòng cho biết lại số lượng người sử dụng: ")
        elif infor_customer_need_change == "time_using":
            dispatcher.utter_message(text= "Quý khách vui lòng cho biết lại thời gian sử dụng dịch vụ tại nhà hàng: ") 

        return []
        
    
class ActionGetInforOfCustomer(Action):
    def name(self) -> Text:
        return "get_infor_of_customer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        global infor_customer_need_change
        global information_customer

        if infor_customer_need_change == "name":
            name_customer = tracker.get_slot("name_customer")
            information_customer["name_customer"] = name_customer
            infor_customer_need_change = None
            return [SlotSet("name_customer", name_customer)]
        
        elif infor_customer_need_change == "phone_number":
            phone_number = tracker.get_slot("phone_number")
            information_customer["phone_number_customer"] = phone_number
            infor_customer_need_change = None
            return [SlotSet("phone_number", phone_number)]
        
        elif infor_customer_need_change == "quantity_people":
            quantity_people = tracker.get_slot("quantity_people")
            information_customer["quatity_people_using"] = quantity_people
            infor_customer_need_change = None
            return [SlotSet("quantity_people", quantity_people)]
        
        elif infor_customer_need_change == "time_using":
            str_year = tracker.get_slot("year")
            str_month = tracker.get_slot("month")
            str_day = tracker.get_slot("day")
            str_time = tracker.get_slot("time")

            if str_year is not None:
                Date = year_format(year=str_year, Date=Date)
            if str_month is not None:
                Date = month_format(month=str_month, Date=Date)
            if str_day is not None:
                Date = day_format(day=str_day, Date=Date)
            if str_time is not None:
                Date = time_format(time=str_time, Date=Date)
            else:
                dispatcher.utter_message(response="utter_ask_timeday")

            if Date == datetime.now():
                dispatcher.utter_message(response="utter_ask_timeday")

            else:
                time = str(Date.time().replace(microsecond=0))
                day = str(Date.day)
                month = str(Date.month)
                year = str(Date.year)
                print(time, "-", day, "-", month, "-", year)
                sexual = tracker.get_slot("sexual")
                service = tracker.get_slot("service")
            global list_time_using

            list_time_using["time"] = time
            list_time_using["day"] = day
            list_time_using["month"] = month
            list_time_using["year"] = year
            information_customer["time_using_customer"] = list_time_using
            infor_customer_need_change = None

            return [SlotSet("time", time), SlotSet("day", day),
                     SlotSet("month", month), SlotSet("year", year)]
        
class ActionUpdateInforOfCustomer(Action):
    def name(self) -> Text:
        return "update_infor_of_customer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        dispatcher.utter_message(text="Thông tin của quý khách đã được cập nhập!")
        dispatcher.utter_message(response="utter_ask_confirm")

        return []  

class ActionGoodBye(Action):
    def name(self) -> Text:
        return "goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = (tracker.current_state())["sender_id"]
        name = information_customer["name_customer"]
        phone_number = information_customer['phone_number_customer']
        quantity_people = information_customer['quatity_people_using']
        time_using = str(information_customer["time_using_customer"]['year']) + "-" + str(information_customer["time_using_customer"]['month']) + "-" + str(information_customer["time_using_customer"]['day']) + " " + str(information_customer["time_using_customer"]['time']) 
        # text_list_food = ""
        # for i in information_customer["list_food_order"]:
        #     if list_food_order[i] != None:
        #         text_list_food += str(i) + " : " + str(list_food_order[i]) + " phần \n"
        
        # inputdatabase(phone_number, 
        #               name, 
        #               quantity_people, 
        #               time_using, 
        #               information_customer["list_food_order"])

        dispatcher.utter_message(text="Thông tin của quý khách đã được ghi nhận!")
        dispatcher.utter_message(response="utter_thank")

        return []
    