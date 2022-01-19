[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#github.com/monch1962/using-checkov)

# using-checkov
Spike around creating & executing custom checkov policies that are stored in their own git repo


## To use (not working yet)

To include the checkov policies contained in this repo to the standard set of checkov policies, try e.g.

`$ checkov --external-checks-git https://github.com/monch1962/using-checkov.git -f tfplan2.json`

where `tfplan2.json` is your Terraform plan file in JSON format.

To run just the AWS_CUSTOM_LABELS1 policy in this repo on its own, try e.g.

`$ checkov --external-checks-git https://github.com/monch1962/using-checkov.git --check CUSTOM_DRAC_LABELS1 -f tfplan2.json`

## Running inside Gitpod

To run the standard set of checkov checks against a simple S3 Terraform file:

`$ checkov -f tests/simple-s3.tf`

To run just the check tagged CUSTOM_DRAC_LABELS1 in `my-custom-checks`:

`$ checkov -f test-infra/simple-s3.tf --external-checks-dir my-custom-checks --check CUSTOM_DRAC_LABELS1`

To run all standard checks plus all custom checks in `my-custom-checks`:

`$ checkov -f test-infra/simple-s3.tf --external-checks-dir my-custom-checks`