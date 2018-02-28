from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
from rasa_core.agent import Agent
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel

DOMAIN_FILE = "domain.yml"
MODEL_PATH = "models/dialogue"
DATA = "data/data1.json"
STORIES = "data/stories.md"
CONFIG_PATH = "nlu_config.json"
INTEPRETER_PATH = "models/nlu/default/current"

def train_dialogue(domain_file=DOMAIN_FILE, model_path=MODEL_PATH, training_data_file=STORIES):
    agent = Agent(domain=domain_file, policies=[SklearnPolicy()])
    agent.train(filename=training_data_file, max_history=3)
    agent.persist(model_path)
    pass


def train_nlu():

    training_data = load_data(DATA)
    trainer = Trainer(RasaNLUConfig(CONFIG_PATH))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu', fixed_model_name="current")

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter(INTEPRETER_PATH)

    agent = Agent.load(MODEL_PATH, interpreter=interpreter)
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())

def run_databot_online(input_channel, interpreter=RasaNLUInterpreter("models/nlu/default/current"),
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
