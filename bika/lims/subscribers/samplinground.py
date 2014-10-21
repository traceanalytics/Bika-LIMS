from bika.lims.utils.analysisrequest import create_analysisrequest
from Products.CMFCore.utils import getToolByName

def ObjectInitializedEventHandler(obj, event):

  # uc = getToolByName(obj, 'uid_catalog')
  # bsc = getToolByName(obj, 'bika_setup_catalog')

  # bas = obj.bika_setup.bika_analysisspecs

  # client = obj.aq_parent

  # srtemplate = obj.getTemplate()

  # for template in srtemplate.getARTemplates():
  #   analyses = template.getAnalyses()
  #   for analysis in analyses:
  #     service = uc(UID=analysis['service_uid'])[0].getObject()
  #     default_analysisspec = bsc(
  #       portal_type='AnalysisSpec',
  #       getSampleTypeUID=template.getSampleTypeUID(),
  #       getClientUID=[client.UID(), bas.UID()]
  #     )[0].getObject()
  #     results = default_analysisspec.getResultsRange()
  #     results = next(o for o in results if o['keyword'] == service.getKeyword())
  #     print results


  #   create_analysisrequest(
  #     client,
  #     None,
  #     {
  #       "SampleType": template.getSampleType().UID(),
  #       "SamplePoint": template.getSamplePoint().UID()
  #     },
  #     template.getAnalyses(),
  #     template.getPartitions(),
  #   )

  # import pdb; pdb.set_trace()

  print 'create'

