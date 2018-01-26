from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.events  import SlotSet, Restarted
import pprint

# OUTPUT_CHANNEL = "get from config file"
available_methods = [
    "source_data",
]


class SourceData(Action):

    def name(self):
        return "action_source_data"

    def run(self, dispatcher, tracker, domain):
        """
        Find data sources that match tags. If no data sources are found,
        return an empty list
        """
        # TODO: Replace with actual data sourcing action
        tags = list(tracker.get_latest_entity_values('tags')) # because it can't detect list of slots
        pprint.pprint(tracker.current_state())
        limit = tracker.get_slot('limit')

        if tags is None:
            results = [SlotSet('current_objective_progress', 'query_parameters')]
            message = "Sorry, I couldn't identify any search terms. What search terms would you like to query?"

        else:
            message = "Sourcing data from tags: {}".format(tags)
            if limit is not None:
                message += " limited to the top {} results.".format(limit)
            # TODO: When querying database, verify that data returned is healthy and SlotSet accordingly
            results = [SlotSet('current_objective_progress', 'success')]

        dispatcher.utter_message(message)
        return results

