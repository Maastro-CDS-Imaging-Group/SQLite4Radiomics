"""
This module is used for booting up the Radiomic Feature Extraction Pipeline tool
It will also start the correct tool depending on the given input while calling the script.
Currently we have 3 different programs available:
1.  GUI
2.  ROIPrioritySetter
3.  Extraction Pipeline

ToDo: Explain programs
"""
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import importlib.util
import inspect
import logging
import sys
from importlib._bootstrap import ModuleSpec
from typing import Any, Optional

from cli.radiomic_feature_extraction_pipeline_cli import CLI
from configuration_service.config_file_reader import ConfigFileReader
from configuration_service.configuration_service import ConfigurationService
from dal.data_access_layer import DataAccessLayer
from dal.database_connector import DatabaseConnector
from dal.image_repository import ImageRepository
from dal.patient_repository import PatientRepository
from dal.radiomic_feature_repository import RadiomicFeatureRepository
from dal.roi_repository import ROIRepository
from dal.series_repository import SeriesRepository
from dal.sqlite.database_connector_sqlite import DatabaseConnectorSqlite
from dal.sqlite.image_repository_sqlite import ImageRepositorySqlite
from dal.sqlite.patient_repository_sqlite import PatientRepositorySqlite
from dal.sqlite.radiomic_feature_repository_sqlite import RadiomicFeatureRepositorySqlite
from dal.sqlite.roi_repository_sqlite import ROIRepositorySqlite
from dal.sqlite.series_repository_sqlite import SeriesRepositorySqlite
from dal.sqlite.study_repository_sqlite import StudyRepositorySqlite
from dal.study_repository import StudyRepository
from gui.radiomic_feature_extraction_pipeline_gui import GUI
from logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import \
    BinaryMaskAnd3DImageGenerator
from logic.dicom_file_reader.dicom_file_reader import DicomFileReader
from logic.feature_extractor.feature_calculator import FeatureCalculator
from logic.logic import Logic
from logic.roi_selector.roi_selector import ROISelector
from logic.roi_selector.roi_selector_properties import \
    ROISelectorProperties
from logic.utils.logging_utils import setup_logging


logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
setup_logging(filename='logs/bootstrapper.log', name=__name__, use_stdout=False)


class Bootstrapper:
    """
    This class is used for instantiating the other software components of the tool.
    It will also start the correct tool depending on the given input while calling the script.
    """

    def __init__(self) -> None:
        """
        Constructor of the Bootstrapper.
        Creates instances off all necessary software components that the tool needs.
        """

        # An instance of the ConfigurationService will be created which will handle the reading of and writing to the
        # conquest dicom.ini file.
        self.config_file_reader_conquest: ConfigFileReader = ConfigFileReader(r'..\Conquest\dicom.ini')
        self.conquest_settings: ConfigurationService = ConfigurationService(self.config_file_reader_conquest)

        # An instance of the ConfigurationService will be created which will handle the reading of and writing to the
        # conquest dicom.ini file.
        self.config_file_reader_feature_extraction: ConfigFileReader = ConfigFileReader(r"resources\config.ini")
        self.feature_extraction_settings: ConfigurationService = ConfigurationService(
            self.config_file_reader_feature_extraction)

        # The bootstrapper asks the feature extraction configuration file reader what type of database it should
        # connect to.
        database_type: str = self.feature_extraction_settings.load_database_type()

        # Empty field creation. These fields will later be used to store an instance of the DataAccessLayer, the GUI
        # and the CLI.
        self.data_access_layer: DataAccessLayer
        self.gui: Optional[GUI] = None
        self.cli: Optional[CLI] = None

        # If the database type is sqlite then the create_sqlite_data_access_layer method will be called.
        if database_type.lower() == 'sqlite':
            self.data_access_layer = self.create_sqlite_data_access_layer()

        # Loads the file path of the parameter file for PyRadiomics.
        pyradiomics_settings: str = self.feature_extraction_settings.load_radiomics_params_file()

        # Loads all the properties from the configuration-file that will be used by the ROISelectors.
        roi_selector_properties: ROISelectorProperties = ROISelectorProperties(
            self.feature_extraction_settings.load_roi_selector_properties())

        # Loads the selected ROISelector from the file path that is defined in the configuration-file.
        roi_selector: ROISelector = self.load_strategies_from_configuration_file(
            'Region of interest selector', ROISelector, self.data_access_layer.get_roi_repos(),
            roi_selector_properties)

        # Loads the selected BinaryMaskAnd3DImageGenerator from the file path that is defined in the configuration-file.
        binary_mask_and_3d_image_generator: BinaryMaskAnd3DImageGenerator = \
            self.load_strategies_from_configuration_file('Binary mask and 3d image generator',
                                                         BinaryMaskAnd3DImageGenerator)

        # Loads the selected DicomFileReader from the file path that is defined in the configuration-file.
        dicom_file_reader: DicomFileReader = self.load_strategies_from_configuration_file(
            'Dicom file reader', DicomFileReader, self.conquest_settings.load_data_directory())

        # Loads the selected FeatureCalculator from the file path that is defined in the configuration-file.
        feature_calculator: FeatureCalculator = self.load_strategies_from_configuration_file(
            'Feature calculator', FeatureCalculator, self.data_access_layer.get_radiomic_feature_repos(),
            pyradiomics_settings)

        # Creates an instance of the Logic class.
        self.logic: Logic = Logic(self.data_access_layer, self.conquest_settings, self.feature_extraction_settings,
                           roi_selector, binary_mask_and_3d_image_generator, dicom_file_reader, feature_calculator)


    def main(self) -> None:
        """
        This main method starts the GUI, Priority setter or extraction pipeline depending on the system arguments.

        -   If **-gui** is passed, the gui module is booted up.
        -   If **-priority-setter** is passed, the priority_setter program is booted up.
        -   If **-extraction-pipeline** *sop_instance_rtstruct* is passed, the extraction pipeline is booted up
            for the given sop-instance_rtstruct.

        """

        # This if statement checks if no argument was given.
        if len(sys.argv) == 1:
            self.show_warning_no_or_wrong_arguments_were_passed()
            return

        # This if statement checks if the -gui parameter was given while calling the script.
        if sys.argv[1].lower() == '-gui':
            print('Booting up the gui...')
            # Creates an instance of the GUI (Graphical User Interface).
            self.gui = GUI(self.logic)

            # Starts the GUI
            self.gui.start()

            #Makes sure the GUI keeps running after it has been started.
            self.gui.mainloop()
            print('Boot up complete')
            return

        # An instance of the CLI (Command Line Interface) will be created since -gui was not passed as an argument.
        self.cli: CLI = CLI(self.logic)

        # This if statement checks if the -priority-setter parameter was given while calling the script.
        if sys.argv[1].lower() == '-priority-setter':

            # Starts the priority setter tool.
            self.cli.start_priority_setter()
            return

        # This if statement checks if the -extraction-pipeline parameter was given while calling the script.
        if sys.argv[1].lower() == '-extraction-pipeline':

            # Checks if a second argument was passed with the call for the script and checks if the parameter was valid.
            if len(sys.argv) == 2:

                # Displays error for missing sop-instance.
                print("The sop instance parameter was missing.")
                print("Please call script using the following parameters:")
                print("python -m bootstrapper -extraction-pipeline 'SOP-instance of RTSTRUCT'")
                return

            # Starts the extraction pipeline tool.
            self.cli.start_extraction_pipeline(sys.argv[2])
            return

        # No options match the given argument. The argument was incorrect.
        self.show_warning_no_or_wrong_arguments_were_passed()

    @staticmethod
    def show_warning_no_or_wrong_arguments_were_passed() -> None:
        """
        If the second argument wasn't given or was incorrect a warning will be returned!
        """
        print('The expected arguments were missing or incorrect!')
        print("To start the GUI program use the '-gui' argument")
        print("To start the Priority Setter Program use the '-priority-setter' argument")
        print("To start the Extraction Pipeline Program use the '-extraction-pipeline' argument followed by a "
              "SOP-instance of an RTSTRUCT")

    def load_strategies_from_configuration_file(self, strategy_type: str, parent_class: Any, *args, **kwargs) -> Any:
        """
        Loads the selected strategies for the given strategy type with the correct parameters.
        :param strategy_type: The name of the configuration files section where the selected strategy can be found.
        :param parent_class: The class that the strategy should inherit from.
        :param args: A series of non-named arguments that will be passed to the constructor of the selected strategy.
        :param kwargs: A series of named arguments that will be passed to the constructor of the selected strategy.
        :return: An instance of the selected strategy.
        """

        # Loads the string that tells the program which strategy to select.
        selected_strategy: str = self.feature_extraction_settings.load_strategy_selection(strategy_type)

        # Loads the script location of the strategy that was selected.
        script_location: str = self.feature_extraction_settings.load_strategy(strategy_type, selected_strategy)

        # Loads the strategy itself using the static load_class_dynamically method.
        return self.load_class_dynamically(script_location, selected_strategy, parent_class, *args, **kwargs)

    def create_sqlite_data_access_layer(self) -> DataAccessLayer:
        """
        Initialises an instance of the Data Access Layer which will store an instance of all data repositories.
        :return: An instance of the Data Access Layer.
        """
        # Loads the saving method from the configuration-file
        type_of_save: str = self.feature_extraction_settings.load_save_type()

        # Sets the file location for the sqlite queries.
        queries_file_location: str = r"resources\queries\sqlite"

        # Creates an instance of the DatabaseConnectorSqlite which will be used to talk with the SQLite database.
        database_connector: DatabaseConnector = DatabaseConnectorSqlite(
            self.conquest_settings.load_database_settings())

        # Creates an instance of the PatientRepository which will manage the saving of patient data to and
        # loading patient data from the database.
        patient_repos: PatientRepository = PatientRepositorySqlite(database_connector, queries_file_location)

        # Creates an instance of the StudyRepository which will manage the saving of study data to and
        # loading study data from the database.
        study_repos: StudyRepository = StudyRepositorySqlite(database_connector, queries_file_location)

        # Creates an instance of the SeriesRepository which will manage the saving of series data to and
        # loading series data from the database.
        series_repos: SeriesRepository = SeriesRepositorySqlite(database_connector, queries_file_location)

        # Creates an instance of the ImageRepository which will manage the saving of image data to and
        # loading image data from the database.
        image_repos: ImageRepository = ImageRepositorySqlite(database_connector, series_repos, patient_repos,
                                                             study_repos, queries_file_location)

        # Creates an instance of the ROIRepository which will manage the saving of region of interest data to and
        # loading region of interest data from the database.
        roi_repos: ROIRepository = ROIRepositorySqlite(database_connector, series_repos, queries_file_location)

        # Creates an instance of the RadiomicFeatureRepository which will manage the saving of radiomic feature data
        # to and loading radiomic feature data from the database.
        radiomic_feature_repos: RadiomicFeatureRepository = RadiomicFeatureRepositorySqlite(
            database_connector, patient_repos, series_repos, queries_file_location, type_of_save)

        # Creates an instance of the DataAccessLayer.
        return DataAccessLayer(image_repos, patient_repos, radiomic_feature_repos, roi_repos, series_repos, study_repos)

    @staticmethod
    def load_class_dynamically(file_path: str, module_name: str, parent_class: Any, *args, **kwargs) -> None:
        """
        Loads python script from file path.
        :param file_path: File path to the script to load.
        :param module_name: Name for the model of the script.
        :param parent_class: The parent class of the class that will be loaded.
        :param args: A series of non-named arguments that will be passed to the constructor of the selected strategy.
        :param kwargs: A series of named arguments that will be passed to the constructor of the selected strategy.
        :return: Instance of the loaded class.
        """

        # Loads module from script.
        spec: ModuleSpec = importlib.util.spec_from_file_location(module_name, file_path)
        module: ModuleSpec = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        name: str
        obj: type
        # Loops through all objects that were found.
        for name, obj in inspect.getmembers(module):

            # Checks if object is not a class.
            if not inspect.isclass(obj):
                continue

            # Checks if class is not a subclass of the given parent_class.
            if not issubclass(obj, parent_class):
                continue

            # Checks if class is instance parent_class.
            if name == parent_class.__name__:
                continue

            # The correct class was found. Instantiate class and return instance.
            return obj(*args, **kwargs)


# Checks whether the script was called by the Python interpreter directly or by another script.
if __name__ == "__main__":
    # If script was called by the Python interpreter, create an instance of the Bootstrapper
    bootstrapper = Bootstrapper()

    # Start the tool
    bootstrapper.main()
