from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from cmtg.base import CRED, CEND, CORA, MAIN_ACTIONS, MANAGER

POWER_ACTIONS = ['setup', 'run']
HISTORY = FileHistory('/tmp/hist.dat')
ACTIONS = ['ls'] + POWER_ACTIONS

class Power2:
    """ Power of 2"""
    def __init__(self):
        pass

    def run(self):
        sig = None
        clp = WordCompleter(ACTIONS + ['quit', 'help'])

        while sig not in MAIN_ACTIONS:
            sig = prompt('cmtg>', completer=clp, history=HISTORY,
                         key_bindings_registry=MANAGER.registry)

            sig = sig.strip()

