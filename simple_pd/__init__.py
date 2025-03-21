from otree.api import *

doc = """
Prisoner's Dilemma Game
"""


class C(BaseConstants):
    NAME_IN_URL = "simple_pd"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    PAYOFF_MATRIX = {
        ("C", "C"): [3, 3],
        ("C", "D"): [0, 5],
        ("D", "C"): [5, 0],
        ("D", "D"): [1, 1],
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    @staticmethod
    def set_payoffs(group: BaseGroup):
        p1, p2 = group.get_players()
        p1_decision = p1.decision
        p2_decision = p2.decision
        p1.payoff, p2.payoff = C.PAYOFF_MATRIX[(p1_decision, p2_decision)]


class Player(BasePlayer):
    decision = models.StringField(
        choices=["C", "D"],
        doc="This player's decision",
        widget=widgets.RadioSelect,
        label="Choose: Cooperate (C) or Defect (D)",
    )


class Decision(Page):
    form_model = "player"
    form_fields = ["decision"]


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = Group.set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        other_player = player.get_others_in_group()[0]
        return {
            "player": player,
            "other_player": other_player,
        }


page_sequence = [Decision, ResultsWaitPage, Results]
