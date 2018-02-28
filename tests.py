from unittest import TestCase
from bot.utils import INTEPRETER_PATH, MODEL_PATH
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent

class TestStoriesChatFlow(TestCase):

	def setUp(self):
		interpreter = RasaNLUInterpreter(INTERPRETER_PATH)
		self.agent = Agent.load(MODEL_PATH, interpreter)

	def test_greet(self):
		

	def test_bye(self):
		pass