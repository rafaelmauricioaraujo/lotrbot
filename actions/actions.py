# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from . import database
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sys
sys.path.append('..')

class ActionGetHeroes(Action):

    def name(self) -> Text:
        return "action_get_heores"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        heroes = database.get_heroes()
        dispatcher.utter_message(text=heroes)
        database.close()

        return []

class ActionGetHeroesAttribuites(Action):

    def name(self) -> Text:
        return "action_get_attributes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hero = tracker.get_slot("hero")
        message = database.get_heroes_attributes(hero)
        dispatcher.utter_message(text=message)
        database.close()

        return []

class ActionGetHeroesGears(Action):

    def name(self) -> Text:
        return "action_get_gears"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hero = tracker.get_slot("hero")
        message = database.get_heroes_gears(hero)
        dispatcher.utter_message(text=message)
        database.close()

        return []


class ActionGetAllAtributtes(Action):

    def name(self) -> Text:
        return 'action_get_all_attributes'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        hero = tracker.get_slot("hero")
        all_att = database.get_all_attributes(hero)
        dispatcher.utter_message(text=all_att)
        database.close()

        return []