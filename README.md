# using-checkov
Spike around using custom checkov controls


## To use

To run just the checkov checks contained in this repo, try e.g.

`$ checkov --external-checks-git https://github.com/monch1962/using-checkov.git -f tfplan2.json`

where `tfplan2.json` is your Terraform plan file in JSON format
