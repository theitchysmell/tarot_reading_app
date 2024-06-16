import sys
import os

def load_tarot_dict():
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from data.tarot_dict import tarot_dict
    return tarot_dict
