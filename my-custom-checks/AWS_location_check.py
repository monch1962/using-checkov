from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class AWSLocationCheck(BaseResourceCheck):
  def __init__(self):
    name = """Ensure AWS assets are stored in ap-southeast-2 region"""
    id = "DRAC_AWS_LOCATION"
    supported_resources = ['aws_*']
    categories = [CheckCategories.GENERAL_SECURITY]
    super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    
  def scan_resource_conf(self, conf):
    if 'region' in conf.keys():
      region = conf['region'][0]
      if 'ap-southeast-2' not in region:
        return CheckResult.FAILED
    return CheckResult.PASSED
  
scanner = AWSLocationCheck()
