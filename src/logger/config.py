import os
import sys

SCRIPT      = ""
TEST        = False
LOGGING     = True
PROFILING   = False

LOG_FILE_TRUNCATE = False

DEBUG = True\
            if hasattr(sys, "gettrace") and sys.gettrace()\
            else\
        False

LOG_MULTI = False

if LOGGING:
    if TEST:
        LOG_TO_TERMINAL = False
    else:
        LOG_TO_TERMINAL = True
    LOG_TO_FILE     = True
else:
    LOG_MULTI       = False
    LOG_TO_TERMINAL = False
    LOG_TO_FILE     = False


FIELDS  =   [
                "SCRIPT",
                "TEST",
                "LOGGING",
                "LOG_FILE_TRUNCATE",
                "DEBUG",
                "LOG_MULTI",
                "LOG_TO_TERMINAL",
                "LOG_TO_FILE",
                "PROFILING",
            ]

# https://peps.python.org/pep-0713/
def __call__(conf = None):
    if conf is None:
        module = sys.modules[__name__]
        conf =  {
                    k : getattr(module, k, None) 
                    for k in FIELDS
                    if k.isupper() and not k.startswith("_")
                }
        return conf
    else:
        # container = type("Config", (object,), _dict)
        # conf = container()
        for k,v in conf.items():
            setattr(sys.modules[__name__], k, conf[k])
