import random

from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "prestige_sd"
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 3
    BC_RATIO = 3
    ENDOWMENT = 100


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        subsession.group_randomly()

    for p in subsession.get_players():
        p.show_payoff = random.choice([True, False])
        p.show_contribution = random.choice([True, False])


class Group(BaseGroup):
    total_contribution = models.CurrencyField()


class Player(BasePlayer):
    prev_contributions = models.CurrencyField()
    contribution = models.CurrencyField(min=0, max=C.ENDOWMENT)
    show_payoff = models.BooleanField()
    show_contribution = models.BooleanField()

    checktest_q1 = models.IntegerField(
        label="Q1. あなたは毎回意志決定をする前に 100 ポイントを与えられる",
        choices=[
            [1, "正しい"],
            [0, "間違い"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    checktest_q2 = models.IntegerField(
        label="Q2. 意志決定は 10 回行われる",
        choices=[
            [1, "正しい"],
            [0, "間違い"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    checktest_q3 = models.IntegerField(
        label="Q3. あなたが 70 ポイントを貢献した場合，あなたの手元には何ポイント残りますか？",
        min=0,
    )
    checktest_q4 = models.IntegerField(
        label="Q4. あなたが 70 ポイント，他のプレイヤーのAさんが 90 ポイント，Bさんが 100 ポイントをそれぞれ貢献した場合，グループの合計ポイント（増やされる前）はいくつになりますか？",
        min=0,
    )
    checktest_q5 = models.IntegerField(
        label="Q5. 「Q4」の状況で，グループのポイントが二倍に増やされた場合，ポイントはいくつになりますか？",
        min=0,
    )
    checktest_q6 = models.IntegerField(
        label="Q6. 「3人グループで貢献したポイントが（Q4）で，その合計ポイントが二倍された結果（Q5）になった．」この時，あなたに分配されるポイントはいくつになりますか？",
        min=0,
    )
    checktest_q7 = models.IntegerField(
        label="Q7. 「Q3」～「Q6」の結果を踏まえて，あなたの獲得ポイントはいくつになりますか？",
        min=0,
    )


# FUNCTIONS
def set_previous_contribution(player: Player):
    if player.round_number == 1:
        return

    player.prev_contributions = player.in_round(player.round_number - 1).contribution


def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    individual_share = group.total_contribution * C.BC_RATIO / len(players)
    for p in players:
        p.payoff = individual_share + C.ENDOWMENT - p.contribution
        set_previous_contribution(p)


def generate_others_results_list(player: Player):
    group = player.group
    other_players = player.get_others_in_group()
    res_list = []
    for p in other_players:
        player_dict = {
            "id": p.id_in_group,
            "contribution": p.contribution if player.show_contribution else "？",
            "payoff": p.payoff if player.show_payoff else "？",
        }
        res_list.append(player_dict)
    return res_list


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class CheckTest(Page):
    form_model = "player"
    form_fields = [
        "checktest_q1",
        "checktest_q2",
        "checktest_q3",
        "checktest_q4",
        "checktest_q5",
        "checktest_q6",
        "checktest_q7",
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def error_message(player, values):
        correct_dict = {
            "checktest_q1": 1,
            "checktest_q2": 0,
            "checktest_q3": 30,
            "checktest_q4": 260,
            "checktest_q5": 520,
            "checktest_q6": 140,
            "checktest_q7": 170,
        }
        print(values)
        for field, correct_value in correct_dict.items():
            if field in values and values[field] != correct_value:
                return "あなたは全問正解していません。もう一度やり直してください。"
        return None


def is_bot_error_message(player: Player, value):
    if value:
        return "全問正解していない"


class WaitForIntroduction(WaitPage):
    wait_for_all_groups = True


class Decision(Page):
    form_model = "player"
    form_fields = ["contribution"]

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        player_results = {"payoff": player.payoff, "contribution": player.contribution}
        return {
            "total_contribution": group.total_contribution,
            "player_results": player_results,
            "other_results": generate_others_results_list(player),
        }


page_sequence = [
    Introduction,
    CheckTest,
    WaitForIntroduction,
    Decision,
    ResultsWaitPage,
    Results,
]
