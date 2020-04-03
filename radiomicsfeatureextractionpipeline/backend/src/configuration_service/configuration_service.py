"""
This module communicates between the tool and the configuration files.
It provides options for saving properties to ini-files and reading properties from ini-files.
"""

import logging
import os
from configparser import NoSectionError, NoOptionError
from typing import Dict, Optional

from configuration_service.config_file_reader import ConfigFileReader
from configuration_service.configuration_error import ConfigurationError

logger = logging.getLogger("__main__")


class ConfigurationService:
    """
    Facade class of configuration service package
    All calls for classes in the configuration service packages should go through this object
    """
    def __init__(self, config_file_reader: ConfigFileReader) -> None:
        """
        Constructor of the ConfigurationService class.
        :param config_file_reader: An instance of the ConfigFileReader class.
        """
        self.config_file_reader: ConfigFileReader = config_file_reader

    def save_database_settings(self, connection_string: str) -> None:
        """
        Saves the connection properties for connecting to the database
        :param connection_string: The connection properties for connection to the database.
        :return: The method has no return value.
        """
        self.config_file_reader.add_section('sscscp')
        self.config_file_reader.save_property('sscscp', 'SQLServer', connection_string)

    def load_database_settings(self) -> str:
        """
        Loads the connection properties for connecting to the database.
        :return: The connection properties for connecting to the database.
        """
        try:
            return self.config_file_reader.read_property('sscscp', 'SQLServer')
        except (NoSectionError, NoOptionError) as exception:
            logger.exception("No database properties found in {0}".format(
                os.path.abspath(self.config_file_reader.config_file_path)))
            raise ConfigurationError("An error occurred reading the database settings!") from exception

    def save_data_directory(self, data_directory: str) -> None:
        """
        Saves the path to the data directory containing the DICOM images.
        :param data_directory: The path to the data directory containing the DICOM images.
        :return: This method has no return value.
        """

        self.config_file_reader.add_section("sscscp")
        self.config_file_reader.save_property("sscscp", "MAGDevice0", data_directory)

    def load_data_directory(self) -> str:
        """
        Loads the path to the data directory containing the DICOM images.
        :return: Path to the data directory containing the DICOM Images.
        """
        return self.config_file_reader.read_property("sscscp", "MAGDevice0")

    def load_roi_selector_properties(self) -> Dict[str, str]:
        """
        Loads the properties used by the ROI selectors.
        :return: Returns a dictionary with all property names with their value.
        """
        return dict(self.config_file_reader.get_all_properties_from_section('Region of interest selector properties'))

    def load_strategy_selection(self, strategy_type: str) -> str:
        """
        Loads the selected strategy for the given strategy type.
        :param strategy_type: The type of the strategy to look for.
        :return: The name of the selected strategy.
        """
        return self.config_file_reader.read_property(strategy_type, 'Selected strategy')

    def load_strategy(self, strategy_type: str, selected_strategy: str) -> str:
        """
        Loads the path to the Python script of the selected strategy for the given strategy type.
        :param strategy_type: The type of the strategy that is selected.
        :param selected_strategy: The name of the strategy that is selected.
        :return: Path to the script for the selected strategy.
        """
        return self.config_file_reader.read_property(strategy_type + ' strategies', selected_strategy)

    def load_radiomics_params_file(self) -> Optional[str]:
        """
        Loads the path to the radiomics parameter file.
        :return: The path to the radiomics parameter file.
        """
        try:
            return self.config_file_reader.read_property('Radiomics', 'Parameter file location')
        except (NoSectionError, NoOptionError):
            logger.warning("No Parameter file given. Continuing with the default settings.")
            return None

    def load_database_type(self) -> str:
        """
        Loads the type of the database.
        :return: The type of the database.
        """
        return self.config_file_reader.read_property('Database', 'type')

    def load_save_type(self) -> str:
        """
        Loads the manner in which the csv file should be saved.
        :return: The type save method.
        """
        return self.config_file_reader.read_property('Save as csv', 'type')
