# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

#loggibng.basicConfig(level=logging.INFO)
class ChtBot:

    def __init__(self):
        self.bot = ChatBot(
            'Bot',
            database='noya',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.4,
                    'default_response': 'I will look into it...'
                }
            ],
        )

    def response(self, query):
        return self.bot.get_response(query)
