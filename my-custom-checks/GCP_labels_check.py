from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class GCPLabelsCheck(BaseResourceCheck):
  def __init__(self):
    name = """Ensure GCP assets are labelled with the mandatory set of labels:
    - trustlevel must have one of the following values: [high, medium, low]
    - confidentiality must have one of the following values: [high, medium, low]
    - integrity must have one of the following values: [high, medium, low]"""
    id = "DRAC_GCP_MANDATORY_LABELS"
    supported_resources = ['google_*']
    categories = [CheckCategories.GENERAL_SECURITY]
    super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    
  def scan_resource_conf(self, conf):
    if 'labels' in conf.keys():
      labels = conf['labels'][0]
      if 'integrity' in labels and 'trustlevel' in labels and 'confidentiality' in labels:
        if labels['integrity'] in ['high', 'medium', 'low'] and labels['trustlevel'] in ['high', 'medium', 'low'] and labels['confidentiality'] in ['high', 'medium', 'low']:
          return CheckResult.PASSED
    return CheckResult.FAILED
  
scanner = GCPLabelsCheck()
