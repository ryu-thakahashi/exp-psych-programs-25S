from otree.api import Bot
from otree.api import Currency as c
from otree.api import currency_range, expect

from . import *


class PlayerBot(Bot):

    def play_round(self):
        assert str(self.player.participant.payoff) in self.html
