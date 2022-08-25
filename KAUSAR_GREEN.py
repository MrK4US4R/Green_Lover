import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from KAUSAR_64 import __warningregistry__

        __warningregistry__()

elif bit == "32bit":

        from KAUSAR_32 import __warningregistry__

        __warningregistry__()







