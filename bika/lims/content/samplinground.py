
from Products.Archetypes.public import *

from AccessControl import ClassSecurityInfo
from plone.app.folder.folder import ATFolder
from zope.interface import implements

from bika.lims.config import PROJECTNAME
from bika.lims.content.bikaschema import BikaFolderSchema
from bika.lims.idserver import renameAfterCreation
from bika.lims.interfaces import ISamplingRound



schema = BikaFolderSchema.copy() + Schema((
))


class SamplingRound(ATFolder):
    implements(ISamplingRound)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        renameAfterCreation(self)

    def isOpen(self):
        """ Returns true if the SamplingRound is in 'open' state
        """
        return True


registerType(SamplingRound, PROJECTNAME)
