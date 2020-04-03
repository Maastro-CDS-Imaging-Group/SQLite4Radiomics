"""
Module connects to ini-files and reads data from the ini-file and writes data to the ini-file
"""

import configparser
import os
from typing import Tuple, Any, AbstractSet

from configuration_service.configuration_error import ConfigurationError


class ConfigFileReader:
    """
    Class is used for reading data from and writing data to ini-files.
    """

    def __init__(self, config_file_path: str) -> None:
        """
        Constructor for the ConfigFileReader
        :param config_file_path: The path to the configuration file that the object will talk with.
        """
        self.config_file_path: str = config_file_path
        self.config_parser: configparser.ConfigParser = configparser.ConfigParser()
    
    def read_property(self, section_name: str, property_name: str) -> str:
        """
        Reads the value of an option in the ini-file.
        :param section_name: The section of the option to read.
        :param property_name: The option to read.
        :return: The value of the option.
        """
        try:
            # Opens the ini-file in read mode.
            with open(self.config_file_path, 'r') as config_file:

                # Reads the ini-file
                self.config_parser.read_file(config_file)

                # Checks if given section not exists.
                if not self.section_exists(section_name):
                    # Throws exception for non existent section.
                    raise ConfigurationError(
                        "The configuration file didn't have a section called {}".format(section_name))

                # Checks if given option not exists.
                if not self.option_exists(section_name, property_name):
                    # Throws exception for non existent option.
                    raise ConfigurationError(
                        "The configuration file didn't have an option called {} within section {}".format(
                            property_name, section_name)
                    )
                # Returns value of the option.
                return self.config_parser.get(section_name, property_name)
        except FileNotFoundError as error:
            # Throws error for error trying to access the ini-file.
            raise ConfigurationError("The configuration file {} couldn't be found or accessed!".format(
                self.config_file_path)) from error
    
    def save_property(self, section_name: str, property_name: str, property_value: str) -> None:
        """
        Save a value to the ini-file.
        :param section_name: The name of the section to store the value in.
        :param property_name: The name of the option to store the value in.
        :param property_value: The value to store.
        :return: The method has no return value.
        """

        # Checks if the path to the ini-file exists.
        if not os.path.exists(self.config_file_path):
            # Throws error for not finding the ini-file.
            raise ConfigurationError("The configuration file {} couldn't be found or accessed!".format(
                self.config_file_path))
        # Opens the file in append mode.
        with open(self.config_file_path, 'a') as config_file:
            # Checks if given section exists.
            if not self.section_exists(section_name):
                # Throws error for non existing section.
                raise ConfigurationError(
                    "The configuration file didn't have a section called {}".format(section_name))
            # Sets the option to the new value.
            self.config_parser.set(section_name, property_name, property_value)
            # Save changes made to the ini-file.
            self.config_parser.write(config_file)
            
    def add_section(self, section_name: str) -> None:
        """
        Adds a new section to the ini-file
        :param section_name: The name of the section to add.
        :return: The method has no return value.
        """

        # Checks if the path to the ini-file exists.
        if not os.path.exists(self.config_file_path):
            # Throws error for not finding the ini-file.
            raise ConfigurationError("The configuration file {} couldn't be found or accessed!".format(
                self.config_file_path))
        # Opens the file in append mode.
        with open(self.config_file_path, 'a') as config_file:
            # Checks if section already exists.
            if self.section_exists(section_name):
                # Skips adding the section since section already exists.
                return
            # Adds section to ini-file.
            self.config_parser.add_section(section_name)
            # Saves changes to the ini-file.
            self.config_parser.write(config_file)

    def get_all_properties_from_section(self, section_name: str) -> AbstractSet[Tuple[Any, Any]]:
        """
        Loads all options from a section of the ini-file.
        :param section_name: The section to read the options from.
        :return: A list with all options in the section with their current value.
        """

        # Checks if the path to the ini-file exists.
        if not os.path.exists(self.config_file_path):
            # Throws error for not finding the ini-file.
            raise ConfigurationError("The configuration file {} couldn't be found or accessed!".format(
                self.config_file_path))
        # Opens the ini-file in read mode.
        with open(self.config_file_path, 'r') as config_file:
            # Checks if given section exists.
            if not self.section_exists(section_name):
                # Throws error for non existing section.
                raise ConfigurationError(
                    "The configuration file didn't have a section called {}".format(section_name))
            # Reads ini-file
            self.config_parser.read(config_file)
        # Returns a list with all options in the section with their current value.
        return self.config_parser.items(section_name)
            
    def section_exists(self, section_name: str) -> bool:
        """
        Checks whether a section exists in the ini-file.
        :param section: The section to check for.
        :return: Returns true if section exists and returns false if section doesn't exists.
        """

        # Checks if the path to the ini-file exists.
        if not os.path.exists(self.config_file_path):
            # Throws error for not finding the ini-file.
            raise ConfigurationError("The configuration file {} couldn't be found or accessed!".format(
                self.config_file_path))

        # Opens the ini-file in read mode
        with open(self.config_file_path, 'r'):
            # Returns if the section exists or not.
            return self.config_parser.has_section(section_name)
    
    def option_exists(self, section_name: str, option_name: str) -> bool:
        """
        Checks whether an option exists in the ini-file.
        :param section: The section to check for.
        :param option: The option to check for.
        :return: Returns true if option exists and return false if section doesn't exists.
        """

        # Checks if the path to the ini-file exists.
        if not os.path.exists(self.config_file_path):
            # Throws error for not finding the ini-file.
            raise ConfigurationError("The configuration file {} couldn't be found or accessed!".format(
                self.config_file_path))
        # Checks if section doesn't exists.
        if not self.section_exists(section_name):
            # Throws error for non existing section.
            raise ConfigurationError(
                "The configuration file didn't have a section called {}".format(section_name))

        # Returns if the option exists or not.
        return self.config_parser.has_option(section_name, option_name)
