from otree.api import Bot
from otree.api import Currency as c
from otree.api import currency_range, expect

from . import *


class PlayerBot(Bot):
    cases = [
        {
            "case": "basic",
            "p1": {"cont": 10, "payoff": 110},
            "p2": {"cont": 10, "payoff": 110},
            "p3": {"cont": 10, "payoff": 110},
        },
        {
            "case": "different_contributions",
            "p1": {"cont": 10, "payoff": 130},
            "p2": {"cont": 20, "payoff": 120},
            "p3": {"cont": 30, "payoff": 110},
        },
        {
            "case": "max_contributions",
            "p1": {"cont": 100, "payoff": 200},
            "p2": {"cont": 100, "payoff": 200},
            "p3": {"cont": 100, "payoff": 200},
        },
    ]

    def play_round(self):
        case = self.case
        p_id = f"p{self.player.id_in_group}"

        if (
            self.player.id_in_group == 1
            and case["case"] == "basic"
            and self.player.round_number == 1
        ):
            for invalid_contribution in [-1, 110]:
                yield SubmissionMustFail(
                    Decision, {"contribution": invalid_contribution}
                )

        yield Decision, dict(contribution=case[p_id]["cont"])
        yield Results
        # print("player.payoff: ", self.player.payoff)
        # print("case[p_id]['payoff']: ", case[p_id]["payoff"])

        assert self.player.payoff == case[p_id]["payoff"]

        another_res_dict = generate_others_results_list(self.player)[0]
        if not self.player.show_payoff:
            assert another_res_dict["payoff"] == "？"
        elif not self.player.show_contribution:
            assert another_res_dict["contribution"] == "？"

        # 2ラウンド目以降でグループIDが変わっていないかを確認
        if self.player.round_number > 1:
            assert (
                self.player.prev_contributions
                == self.player.in_round(self.player.round_number - 1).contribution
            )
