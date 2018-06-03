from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from cmtg.base import CRED, CEND, CORA, MAIN_ACTIONS, MANAGER
from cmtg.power import Power

GAME_ACTIONS = ['multi', 'power', 'bin']
ACTIONS = ['ls'] + GAME_ACTIONS
HISTORY = FileHistory('/tmp/hist.dat')

class Starter:
    """
    Main action hook
    """
    def __init__(self):
        pass

    @classmethod
    def help(cls):
        """ help """
        print('TODO: help')

    def run(self):
        """ main runner loop"""
        sig = None
        clp = WordCompleter(ACTIONS + ['quit', 'help'])

        while sig not in MAIN_ACTIONS:
            sig = prompt('cmtg>', completer=clp, history=HISTORY,
                         key_bindings_registry=MANAGER.registry)

            sig = sig.strip()

            if sig not in ACTIONS + ['quit']:
                print('{}Options are: {}'.format(CRED, CEND))
                Starter.help()
            if sig == 'help':
                Starter.help()
            if sig == 'ls':
                print('{}{}{}'.format(CORA, GAME_ACTIONS, CEND))
            if sig == 'power':
                pwr = Power()
                sig = pwr.run()
