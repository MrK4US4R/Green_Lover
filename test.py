import os, platform

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from KAUSAR_GREEN import login

    login()

elif bit == '32bit':

    from KAUSAR_GREEN import login

    login()
