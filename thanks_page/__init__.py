from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "thanks_page"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class ThanksPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(res_payoff=player.participant.payoff, code=player.participant.code)


page_sequence = [ThanksPage]
