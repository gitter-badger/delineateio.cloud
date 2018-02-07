#!/usr/bin/env python3

"""
Utilising the python-digitalocean library cleans up the
cloud environment using the branch id to remove resources
"""

import os
from sys import argv
import digitalocean
from termcolor import colored


class Cleaner():
    """ Class that manages the clean process """

    INDENT = "  - "

    _do_token = ""
    _branch = ""

    def __init__(self, do_token, branch):
        """ Provides the context to the cleaner """
        self._do_token = do_token
        self._branch = branch

    def get_token(self):
        """ Return the DO token """
        return self._do_token

    def get_branch(self):
        """ Returns the branch to be cleaned """
        return self._branch

    def destroy(self, resource):
        """ destroys the resource """
        resource.destroy()
        self.print_remove(resource)

    def delete(self, resource):
        """ Delete the resource """
        resource.delete()
        self.print_remove(resource)

    def print_remove(self, resource):
        """ Outputs the removal"""

        print(colored("{0}{1} was deleted".format(self.INDENT, resource.name), "cyan"))

    def print_start(self, branch):
        """ Prints the start of the cleaning """

        print()
        print(f"Cleaning for branch '{branch}' ...")

    def print_completion(self, branch):
        """ Prints the completion of the cleaning """

        print()
        print(colored(f"Cleaning for branch '{branch}' completed", "green", attrs=['bold']))
        print()

    def print_error(self, branch, exception):
        """ Prints out an error if required """

        print()
        print(colored(exception, "red"))
        print()
        print(colored(f"The clean for {branch} failed", "red", attrs=['bold']))
        print()

    def clean(self):
        """ Performs the clean of all the resources """

        branch = self.get_branch()

        try:

            self.print_start(branch)

            manager = digitalocean.Manager(token=self.get_token())

            self.remove("Load Balancers", manager.get_all_load_balancers(), self.destroy)
            self.remove("Firewalls", manager.get_all_firewalls(), self.destroy)
            self.remove("Droplets", manager.get_all_droplets(), self.destroy)
            self.remove("Images", manager.get_images(private=True), self.destroy)
            self.remove("Tags", manager.get_all_tags(), self.delete)
            self.print_completion(branch)

        except Exception as exception:

            self.print_error(exception, branch)


    def remove(self, resource_type, resources, func):
        """ Iterates the provided resources and selects those to destroy """

        print()
        print(colored(resource_type, "white", attrs=['bold']))

        if len(resources) is 0:
            print(colored(self.INDENT + "No resources to delete", "yellow"))
            return

        for resource in resources:
            if self.get_branch() in resource.name:
                func(resource)


def get_options(args):
    """ Parses the options provided """

    options = {}  # Empty dictionary to store key-value pairs.
    while args:  # While there are arguments left to parse...
        if args[0][0] == '-':  # Found a "-name value" pair.
            options[args[0]] = args[1]  # Add key and value to the dictionary.
        args = args[1:]  # Reduce the argument list by copying it starting from index 1.
    
    return options


if __name__ == "__main__":

    ARGS = get_options(argv)

    if "-b" in ARGS:
        CLEANER = Cleaner(os.environ['DO_TOKEN'], ARGS['-b']) # "822b91a")
        CLEANER.clean()
    
    else:
        print()
        print(colored("No branch was provided", "red"))
        print()
