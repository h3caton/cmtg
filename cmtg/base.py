"""
Base structures
"""
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys

MAIN_ACTIONS = ['cd ..', 'cd', 'quit']
WORDS = ['ls', 'help'] + MAIN_ACTIONS
CRED = '\033[91m'
CEND = '\033[0m'
CBLUE = '\033[34m'
CGRE = '\033[32m'
CORA = '\033[93m'

MANAGER = KeyBindingManager.for_prompt()

@MANAGER.registry.add_binding(Keys.ControlC)
@MANAGER.registry.add_binding(Keys.ControlD)
def _(event):
    print('By by...')
    event.cli.set_return_value('quit')
