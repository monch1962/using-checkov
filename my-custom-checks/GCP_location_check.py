from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
import re

class GCPLocationCheck(BaseResourceCheck):
  def __init__(self):
    name = """Ensure GCP assets are located in only the accepted locations
    - australia-southeast-1
    - australia-southeast-2"""
    id = "DRAC_GCP_LOCATION_CHECK"
    supported_resources = ['google_*'] # May need to tweak this as not all GCP assets have a location field
    categories = [CheckCategories.GENERAL_SECURITY]
    super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    
  def scan_resource_conf(self, conf):
    if 'location' in conf.keys():
      locations = conf['location'][0]
      for l in locations:
        if not re.search("^(australia-southeast-1|australia-southeast-2)", l):
          return CheckResult.FAILED
      return CheckResult.PASSED
    return CheckResult.FAILED

  
scanner = GCPLocationCheck()
