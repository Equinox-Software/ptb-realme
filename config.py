import os

##########################################
# Contains variables used throughout the project
##########################################

PORT = int(os.environ.get('PORT', 5000))
DATABASE_URL = os.environ['DATABASE_URL'].replace('postgres', 'postgresql', 1)
TOKEN = os.environ['TOKEN']
TRANSLATE_AUTH = os.environ['TRANSLATE-AUTH']
TRANSLATE_URL = os.environ['TRANSLATE-URL']

CONTROL_GROUP = -1001228437777
OFFTOPIC_GROUP = -1001415779011
SUPPORT_GROUP = -1001374176745

NYX = 703453307
ADMINS = (NYX,
          806473770,  # BlueBettle
          1971709534  # Phoenix
          )
VERIFIED_USERS = set(ADMINS + (
    924295169,  # Lucky
    1038099761,  # Abhiskek
    1128670209  # LalitSaini
))
