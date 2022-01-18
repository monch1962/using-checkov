from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class AWSLabelsCheck(BaseResourceCheck):
  def __init__(self):
    name = "Ensure AWS assets are tagged with the mandatory set of labels"
    id = "CUSTOM_DRAC_LABELS1"
    supported_resources = ['aws_s3_bucket']
    categories = [CheckCategories.GENERAL_SECURITY]
    super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    
  def scan_resource_conf(self, conf):
    if conf.get("tags",[]):
      env = conf["tags"][0].get("Environment",{})
      if env in ["Development", "Staging", "Production"]:
        return CheckResult.PASSED
    return CheckResult.FAILED
  
scanner = AWSLabelsCheck()
