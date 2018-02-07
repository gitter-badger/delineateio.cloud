# Cloud Utilities 

## Digital Ocean Clean

Script written in Python 3 for destroying a Digital Ocean cloud deployment where the resources contain the Git brnach short name.  This enables faster clean up of whole environments rather than using the UI.

## Destroyed Resources 

The clean_by_branch.py script destroys the following resources in order:

    1. DO Load Balancers
    2. DO Firewalls
    3. DO Droplets 
    4. DO Images 
    5. DO Tags

Please note that script does not currently destroy the DO Records that contain the short branch name.

## Digital Ocean API Token 

To use the script unmodified a DO API key should be present in an environment variable named DO_TOKEN that provides suitable access to destroy the desired DO resources.
