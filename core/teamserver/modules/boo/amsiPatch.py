from core.teamserver.module import Module


class STModule(Module):
    def __init__(self):
        self.name = 'boo/amsiPatch'
        self.language = 'boo'
        self.description = 'Disables AMSI in the current process'
        self.author = 'AMSI patch by @_xpn_ & @_RastaMouse. Module by @byt3bl33d3r, @modexp, @daddycocoaman'
        self.references = []
        self.options = {}

    def payload(self):
        with open('core/teamserver/modules/boo/src/amsiPatch.boo', 'r') as module_src:
            return module_src.read()
