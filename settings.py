from os import environ


SESSION_CONFIGS = [
    dict(
        name='my_experiment',
        display_name="my_experiment",
        app_sequence=['part_one', 'part_two'],
        num_demo_participants=18,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.0125, participation_fee=4.00, doc=""
)

PARTICIPANT_FIELDS = ["p1_group_id", "c_role",
                      "p1_risk_1", "p1_risk_2", "p1_risk_3", "p1_risk_4",
                      "p1_scenario_random", "p1_risk_random", "p1_lottery_random", "p1_payoff",
                      "p1_risk_random_str", "p1_safe_random_str", "p1_lottery_random_str",
                      "p2_risk_1", "p2_risk_2", "p2_risk_3", "p2_risk_4",
                      "p2_scenario_random", "p2_risk_random", "p2_lottery_random", "p2_payoff",
                      "p2_risk_random_str", "p2_safe_random_str", "p2_lottery_random_str",
                      "p2_character_random", "p2_character_sex",
                      "treatment_0", "treatment_1", "treatment_2"]

SESSION_FIELDS = ["t_groups", "character_random"]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'tokens'

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3786636135045'

INSTALLED_APPS = ['otree']
