import random
import time

from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "prestige_sd"
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 30
    BC_RATIO = 2
    ENDOWMENT = 100


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number > 1:
        subsession.group_like_round(1)

    for p in subsession.get_players():
        p.show_payoff = random.choice([True, False])
        p.show_contribution = random.choice([True, False])


class Group(BaseGroup):
    total_contribution = models.CurrencyField()


class Player(BasePlayer):
    prev_contributions = models.CurrencyField()
    prev_show_payoff = models.BooleanField()
    prev_show_contribution = models.BooleanField()

    contribution = models.CurrencyField(min=0, max=C.ENDOWMENT)
    show_payoff = models.BooleanField()
    show_contribution = models.BooleanField()
    checktest_completed_time = models.FloatField()


# FUNCTIONS
def set_previous_contribution(player: Player):
    if player.round_number == 1:
        return

    prev_round_data = player.in_round(player.round_number - 1)
    player.prev_contributions = prev_round_data.contribution
    player.prev_show_payoff = prev_round_data.show_payoff
    player.prev_show_contribution = prev_round_data.show_contribution


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
class WaitForDecision(WaitPage):
    group_by_arrival_time = True


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


page_sequence = [WaitForDecision, Decision, ResultsWaitPage, Results]
