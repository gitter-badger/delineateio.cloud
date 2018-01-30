"""
Utilising the python-digitalocean library cleans up the
cloud environment using the branch id to remove resources
"""

# pylint: disable=invalid-name

import os
import digitalocean

do_token = os.environ['DO_TOKEN']
git_short = "awesome"

manager = digitalocean.Manager(token=do_token)
my_droplets = manager.get_all_droplets(tag_name=git_short)

print(my_droplets)
