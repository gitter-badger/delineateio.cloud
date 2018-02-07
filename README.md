# Cloud Utilities 

## Digital Ocean Clean

Script written in Python3 for destroying a Digital Ocean cloud deployment where the resources contain the Git branch short name.  This enables faster clean up of trial environments rather than using the UI.

## Destroyed Resources 

The clean_by_branch.py script destroys the following resources in order:

    1. DO Load Balancers
    2. DO Firewalls
    3. DO Droplets 
    4. DO Images 
    5. DO Tags

The script does not currently destroy the DO Records that contain the short branch name.

## Digital Ocean API Token 

To use the script unmodified a DO API key should be present as an environment variable $DO_TOKEN on the excuting host.  The API must have the required permissions to destroy the desired DO resources.

## Usage 

It is not anticipated that this script will be used for normal execution of the CI/CD pipeline, although that is possible.  The orginal use case was to clean during the development of the CI/CD pipeline itself.
