from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from pprint import pprint

from rasa_core.actions import Action
from rasa_core.events  import SlotSet, Restarted, AllSlotsReset

FUNCTIONS = [ 
    "source data"
]

class Greet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class GoodBye(Action):
    def name(self):
        return 'action_goodbye'
        

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class OfferHelp(Action):
    def name(self):
        return 'action_offer_help'
        

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class SourceData(Action):
    def name(self):
        return 'action_source_data'


    def run(self, dispatcher, tracker, domain):
        """
        Find data sources that match tags. If no data sources are found,
        return an empty list
        """
        tags = tracker.get_slot('tags')
        limit = tracker.get_slot('limit')
        message = "Sourcing data ({})...".format(tags)

        if tags is not None:
            if limit is not None:
                message += " Limit ({})...".format(limit)
            dispatcher.utter_message(message)
        return []

class Help(Action):
    def name(self):
        return 'action_help'

    def run(self, dispatcher, tracker, domain):
        message = "Currently, I can ".join(FUNCTIONS) + '.'
        dispatcher.utter_message(message)
        return;

class CheckUnderstanding(Action):
    def name(self):
        return 'action_check_understanding'
        
    def run(self, dispatcher, tracker, domain):
        pass

class ReofferHelp(Action):
    def name(self):
        return 'action_reoffer_help'
        
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class SourceDataPromptTags(Action):
    def name(self):
        return 'action_source_data_prompt_tags'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template(self.name())
        return []

class ResetSlots(object):
    def name(self):
        return 'action_reset_slots'

    def run(self, dispatcher, tracker, domain):
        return [(AllSlotsReset())]