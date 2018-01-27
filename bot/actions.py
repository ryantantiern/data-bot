from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from pprint import pprint

from rasa_core.actions import Action
from rasa_core.events  import SlotSet, Restarted


class SourceData(Action):

    def name(self):
        return "source_data"

    def run(self, dispatcher, tracker, domain):
        """
        Find data sources that match tags. If no data sources are found,
        return an empty list

        # TODO: Replace with actual data sourcing action
        # TODO: When querying database, verify that data returned is healthy
        """
        # Because SLOT type:list is not supported
        tags = list(tracker.get_latest_entity_values('tags'))
        limit = tracker.get_slot('limit')
        if tags is None:
            sys.exit("Error: Cannot source data with empty tags. Tracker state: {}".format(tracker.current_state()))

        message = "Sourcing data ({})...".format(tags)
        if limit is not None:
            message += " Limit ({})...".format(limit)

        dispatcher.utter_message(message)
        return []

class CheckUnderstanding(Action):

    def name(self):
        return "check_understanding"

    def run(self, dispatcher, tracker, domain):
        """
        Depending on the objective, checks that related Slots are correctly filled. if Objective is None,
        exit with an Error.
        TODO: Add support for list in Case 3
        """
        base_message = "I understood that {}. Is that correct?"
        objective = tracker.get_slot('objective')
        if objective == 'source_data':
            tags = tracker.get_slot("tags")
            limit = tracker.get_slot("limit")

            # Case 1: User intents to search for data but hasn't specified tags
            if tags is None:
                message = "you want to search for data"

            # Case 2: User intents to search for data and tags were specified in more than 1 turn
            elif True:
                pprint(tracker.current_state())
                sys.exit("Undefined Case 2 in CheckUnderstanding. Exiting gracefully... ")

            # Case 3: User intents to search for data and tags were specified in 1 turn
            else:
                message = "you want to search for data related to {}".format(tags)

            dispatcher.utter_message(base_message.format(message))
            return []

        sys.exit("Error: Cannot check_understanding with Objective: {}. Current State: {}".format(objective, tracker.current_state()))
        return []




