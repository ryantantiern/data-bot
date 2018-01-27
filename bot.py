from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import argparse
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.tracker_store import TrackerStore
from rasa_core.domain import TemplateDomain
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter

DOMAIN_FILE = "domain.yml"
MODEL_PATH = "models/dialogue"
DATA = "data/data-1.json"
STORIES = "data/stories.md"
CONFIG_PATH = "nlu_model_config.json"

logger = logging.getLogger(__name__)

def train_dialogue(domain_file=DOMAIN_FILE, model_path=MODEL_PATH, training_data_file=STORIES):
    agent = Agent(domain=domain_file, policies=[MemoizationPolicy()])
    agent.train(filename=training_data_file, max_history=3)
    agent.persist(model_path)
    pass


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer

    training_data = load_data(DATA)
    trainer = Trainer(RasaNLUConfig(CONFIG_PATH))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu', fixed_model_name="current")

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")

    agent = Agent.load(MODEL_PATH, interpreter=interpreter)
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())

def run_databot_online(input_channel, interpreter,
                          domain_file=DOMAIN_FILE,
                          training_data_file=STORIES):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy()],
                  interpreter=interpreter)

    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "train-online", "run"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "train-online":
        run_databot_online(ConsoleInputChannel(), RasaNLUInterpreter("models/nlu/default/current"))
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)
