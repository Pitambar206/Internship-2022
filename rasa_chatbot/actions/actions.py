# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import typing

from rasa_sdk import Action, Tracker
import rasa_sdk.events
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from database_connect import userinfo

class ValidateForm(Action):
    def name(self) -> typing.Text:
        return "user_details_form"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: typing.Dict
    ) -> typing.List[rasa_sdk.events.EventType]:
        required_slots = ["name", "number", "email", "age", "gender"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [rasa_sdk.events.SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [rasa_sdk.events.SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> typing.Text:
        return "action_submit"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> typing.List[typing.Dict[typing.Text, typing.Any]]:

        userinfo(tracker.get_slot("name"), tracker.get_slot("number"), tracker.get_slot("email"),
                 tracker.get_slot("age"), tracker.get_slot("gender"))

        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"),
                                 Email=tracker.get_slot("email"),
                                 Age=tracker.get_slot("age"),
                                 Gender=tracker.get_slot("gender"))

        dispatcher.utter_message(text="Thank you for the details")

        return []




