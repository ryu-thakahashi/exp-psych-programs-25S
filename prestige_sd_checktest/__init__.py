from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "prestige_sd_checktest"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
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


# PAGES
class Introduction(Page):
    pass


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


page_sequence = [Introduction, CheckTest]
