from otree.api import Bot
from otree.api import Currency as c
from otree.api import currency_range, expect

from . import *


class PlayerBot(Bot):
    cases = [
        {
            "correct_answers": {
                "checktest_q1": 1,
                "checktest_q2": 0,
                "checktest_q3": 30,
                "checktest_q4": 260,
                "checktest_q5": 520,
                "checktest_q6": 140,
                "checktest_q7": 170,
            },
            "incorrect_answers": {
                "checktest_q1": 1,
                "checktest_q2": 0,
                "checktest_q3": 30,
                "checktest_q4": 0,
                "checktest_q5": 520,
                "checktest_q6": 140,
                "checktest_q7": 170,
            },
        },
    ]

    def play_round(self):
        case = self.case
        yield Introduction

        if self.player.id_in_group == 1:
            yield SubmissionMustFail(CheckTest, case["incorrect_answers"])
        yield CheckTest, case["correct_answers"]
