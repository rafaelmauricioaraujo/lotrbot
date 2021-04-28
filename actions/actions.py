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

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sys
sys.path.append('..')

from database.database import get_heroes, get_heroes_attributes, get_heroes_gears, close


class ActionGetHeroes(Action):

    def name(self) -> Text:
        return "action_get_heores"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        heroes = get_heroes()
        dispatcher.utter_message(text=heroes)
        close()

        return []

class ActionGetHeroesAttribuites(Action):

    def name(self) -> Text:
        return "action_get_attributes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hero = tracker.get_slot("hero")
        message = get_heroes_attributes(hero)
        dispatcher.utter_message(text=message)
        close()

        return []

class ActionGetHeroesGears(Action):

    def name(self) -> Text:
        return "action_get_gears"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hero = tracker.get_slot("hero")
        message = get_heroes_gears(hero)
        dispatcher.utter_message(text=message)
        close()

        return []