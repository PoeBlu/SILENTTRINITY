from core.teamserver.module import Module


class STModule(Module):
    def __init__(self):
        self.name = 'boo/pathhijack'
        self.language = 'boo'
        self.description = 'Identify modifiable folders in %PATH%'
        self.author = '@Daudau'
        self.references = []
        self.options = {}

    def payload(self):
        with open('core/teamserver/modules/boo/src/pathhijack.boo', 'r') as module_src:
            return module_src.read()
