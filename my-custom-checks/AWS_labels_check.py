from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class AWSLabelsCheck(BaseResourceCheck):
  def __init__(self):
    name = """Ensure AWS assets are tagged with the mandatory set of labels:
    - trustlevel must have one of the following values: [high, medium, low]
    - confidentiality must have one of the following values: [high, medium, low]
    - integrity must have one of the following values: [high, medium, low]"""
    id = "DRAC_AWS_MANDATORY_LABELS"
    supported_resources = ['aws_*']
    categories = [CheckCategories.GENERAL_SECURITY]
    super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    
  def scan_resource_conf(self, conf):
    if 'tags' in conf.keys():
      tags = conf['tags'][0]
      if 'integrity' in tags and 'trustlevel' in tags and 'confidentiality' in tags:
        if tags['integrity'] in ['high', 'medium', 'low'] and tags['trustlevel'] in ['high', 'medium', 'low'] and tags['confidentiality'] in ['high', 'medium', 'low']:
          return CheckResult.PASSED
    return CheckResult.FAILED
  
scanner = AWSLabelsCheck()
