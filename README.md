[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#github.com/monch1962/using-checkov)

# using-checkov
Spike around creating & executing custom checkov policies that are stored in their own git repo


## To use 
To include the checkov policies contained in this repo to the standard set of checkov policies, try e.g.

`$ checkov --external-checks-git https://github.com/monch1962/using-checkov.git//my-custom-checks -f tfplan2.json`

where `tfplan2.json` is your Terraform plan file in JSON format. Note the mandatory double `//` betweeen the git repo URL and the subdirectory inside that repo

To run just the DRAC_AWS_MANDATORY_LABELS policy in this repo on its own, try e.g.

`$ checkov --external-checks-git https://github.com/monch1962/using-checkov.git//my-custom-checks --check DRAC_AWS_MANDATORY_LABELS -f tfplan2.json`

## Running inside Gitpod

To run the standard set of checkov checks against a simple S3 Terraform file:

`$ checkov -f test-infra/simple-s3.tf`

To run just the check tagged DRAC_AWS_MANDATORY_LABELS in `my-custom-checks`:

`$ checkov -f test-infra/simple-s3.tf --external-checks-dir my-custom-checks --check DRAC_AWS_MANDATORY_LABELS`

To run all standard checks plus all custom checks in `my-custom-checks`:

`$ checkov -f test-infra/simple-s3.tf --external-checks-dir my-custom-checks`

To run checks against all Terraform files in the `./test-infra` directory:

`$ checkov -d test-infra/ --external-checks-dir my-custom-checks`

## References
- writing custom checkov policies: https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html
