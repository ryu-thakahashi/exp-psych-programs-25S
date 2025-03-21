from otree.api import Bot
from otree.api import Currency as c
from otree.api import currency_range, expect

from . import *


class PlayerBot(Bot):
    # cases = [
    #     {"decision": "協力", "payoff": c(3)},
    #     {"decision": "非協力", "payoff": c(0)},
    # ]

    # def play_round(self):
    #     case = self.case
    #     yield MyPage, dict(decision=case["decision"])
    #     yield Results
    #     expect(self.player.payoff, case["payoff"])

    cases = [
        {
            "p1_d": "協力",
            "p2_d": "協力",
            "p3_d": "協力",
            "p1_payoff": c(3),
            "p2_payoff": c(3),
            "p3_payoff": c(3),
        },
        {
            "p1_d": "協力",
            "p2_d": "協力",
            "p3_d": "非協力",
            "p1_payoff": c(2),
            "p2_payoff": c(2),
            "p3_payoff": c(2),
        },
        {
            "p1_d": "協力",
            "p2_d": "非協力",
            "p3_d": "非協力",
            "p1_payoff": c(1),
            "p2_payoff": c(1),
            "p3_payoff": c(1),
        },
        {
            "p1_d": "非協力",
            "p2_d": "非協力",
            "p3_d": "非協力",
            "p1_payoff": c(0),
            "p2_payoff": c(0),
            "p3_payoff": c(0),
        },
    ]

    def play_round(self):
        case = self.case
        yield MyPage, dict(decision=case["p{}_d".format(self.player.id_in_group)])
        yield Results
        expect(self.player.payoff, case["p{}_payoff".format(self.player.id_in_group)])
