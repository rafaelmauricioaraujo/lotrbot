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

from database.database import get_heroes, close, get_heroes_attributes


class ActionGetHeroes(Action):

    def name(self) -> Text:
        return "action_get_heores"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cursor = get_heroes()
        results = [hero for hero in cursor]
        heores_list = ''
        for result in results:
            heores_list += result['name'] + '\n'

        dispatcher.utter_message(text=heores_list)
        close()

        return []
        # return [SlotSet('')]

class ActionGetHeroesAttribuites(Action):

    def name(self) -> Text:
        return "action_get_attributes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('get heroes attributes called')
        hero = tracker.get_slot("hero")
        print('hero from tracker:  ', hero)

        cursor = get_heroes_attributes(hero)
        print("cursor: ", cursor)

        dispatcher.utter_message(text=cursor)
        close()

        return []
