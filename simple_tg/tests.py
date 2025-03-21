from otree.api import Bot
from otree.api import Currency as c
from otree.api import currency_range, expect

from . import *


class PlayerBot(Bot):
    cases = [{}]

    def play_round(self):
        # case = self.case
        p1_send_amount = 20
        p2_send_back_amount = 10

        if self.player.id_in_group == 1:
            yield Send, dict(send_amount=p1_send_amount)
        else:
            yield SendBack, dict(send_back_amount=p2_send_back_amount)
        yield Results
        if self.player.id_in_group == 1:
            expected_amount = C.ENDOWMENT - p1_send_amount + p2_send_back_amount
            expect(self.player.payoff, expected_amount)
        elif self.player.id_in_group == 2:
            expected_amount = C.BC_RATIO * p1_send_amount - p2_send_back_amount
            expect(self.player.payoff, expected_amount)
