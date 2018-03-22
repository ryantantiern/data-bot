from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import argparse
import warnings

from bot.utils                  import load_agent, load_interpreter #run, train_nlu, train_dialogue, run, run_databot_online #, load_agent, load_interpreter
from rasa_core                  import utils
from rasa_core.channels.console import ConsoleInputChannel


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    """

    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "train-online", "run"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task


    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "train-online":
        run_databot_online(ConsoleInputChannel())
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)
    """
    interpreter = load_interpreter()
    agent = load_agent(interpreter)
    
