import os, sys
try:
    __import__("KAUSAR_GREEN").login()
except Exception as e:
    exit(str(e))