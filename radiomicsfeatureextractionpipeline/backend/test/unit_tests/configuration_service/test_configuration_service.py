from configuration_service.configuration_service import ConfigurationService
from test.mock_ups.configuration_service.config_file_reader import ConfigFileReaderMockUp
from test.unit_tests.mocked_unit_tester import MockedUnitTester


class TestConfigurationService(MockedUnitTester):

    def setUp(self) -> None:
        self.config_file_reader_mock_up = ConfigFileReaderMockUp('')
        self.configuration_service = ConfigurationService(self.config_file_reader_mock_up)

    def test_save_database_settings(self):
        method_to_test = self.configuration_service.save_database_settings
        outputs = []
        inputs = [('Input 1',), ('Input 2',)]
        validation_methods = {
            self.config_file_reader_mock_up.get_add_section_called_with_parameters: [
                {
                    'section_name': 'sscscp'
                },
                {
                    'section_name': 'sscscp'
                }
            ],
            self.config_file_reader_mock_up.get_save_property_is_called_with_parameters: [
                {
                    'section_name': 'sscscp',
                    'property_name': 'SQLServer',
                    'property_value': 'Input 1'
                },
                {
                    'section_name': 'sscscp',
                    'property_name': 'SQLServer',
                    'property_value': 'Input 2'
                }
            ]
        }
        return_values_mocked_methods = []

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_values_mocked_methods)

    def test_load_database_settings(self):
        method_to_test = self.configuration_service.load_database_settings
        outputs = ["TestConnectionString", "ConnectionStringTest"]
        inputs = []
        validation_methods = {
            self.config_file_reader_mock_up.get_read_property_called_with_parameters: [
                {
                    'section_name': 'sscscp',
                    'property_name': 'SQLServer'
                },
                {
                    'section_name': 'sscscp',
                    'property_name': 'SQLServer'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1])]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_save_data_directory(self):
        method_to_test = self.configuration_service.save_data_directory
        outputs = []
        inputs = [('Input 1',), ('Input 2',)]
        validation_methods = {
            self.config_file_reader_mock_up.get_add_section_called_with_parameters: [
                {
                    'section_name': 'sscscp'
                },
                {
                    'section_name': 'sscscp'
                }
            ],
            self.config_file_reader_mock_up.get_save_property_is_called_with_parameters: [
                {
                    'section_name': 'sscscp',
                    'property_name': 'MAGDevice0',
                    'property_value': 'Input 1'
                },
                {
                    'section_name': 'sscscp',
                    'property_name': 'MAGDevice0',
                    'property_value': 'Input 2'
                }
            ]
        }
        return_value_mocked_methods = []

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_load_data_directory(self):
        method_to_test = self.configuration_service.load_data_directory
        outputs = ['TestDataDirectory', 'DataDirectoryTest']
        inputs = []
        validation_methods = {
            self.config_file_reader_mock_up.get_read_property_called_with_parameters: [
                {
                    'section_name': 'sscscp',
                    'property_name': 'MAGDevice0'
                },
                {
                    'section_name': 'sscscp',
                    'property_name': 'MAGDevice0'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1])]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_load_roi_selector_properties(self):
        method_to_test = self.configuration_service.load_roi_selector_properties
        outputs = [{}, {'Prop1': 'Val1'}, {'PropA': 'Val1', 'PropB': 'Val2', 'PropC': 'Val3'}]
        inputs = []
        validation_methods = {
            self.config_file_reader_mock_up.get_get_properties_from_section_called_with_parameters: [
                {
                    'section_name': 'Region of interest selector properties'
                },
                {
                    'section_name': 'Region of interest selector properties'
                },
                {
                    'section_name': 'Region of interest selector properties'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_get_properties_from_section_return_value,
                                        outputs[0]),
                                       (self.config_file_reader_mock_up.set_get_properties_from_section_return_value,
                                        outputs[1]),
                                       (self.config_file_reader_mock_up.set_get_properties_from_section_return_value,
                                        outputs[2])]
        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_load_strategy_selection(self):
        method_to_test = self.configuration_service.load_strategy_selection
        outputs = ['StrategySelectionTestType', 'TestStrategySelectionType']
        inputs = [('StrategyTest',), ('TestStrategy',)]
        validation_methods = {
            self.config_file_reader_mock_up.get_read_property_called_with_parameters: [
                {
                    'section_name': 'StrategyTest',
                    'property_name': 'Selected strategy'
                },
                {
                    'section_name': 'TestStrategy',
                    'property_name': 'Selected strategy'
                },
                {
                    'section_name': 'StrategyTest',
                    'property_name': 'Selected strategy'
                },
                {
                    'section_name': 'TestStrategy',
                    'property_name': 'Selected strategy'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1])]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_load_strategy(self):
        method_to_test = self.configuration_service.load_strategy
        outputs = ['TestStrategyPath', 'StrategyTestPath']
        inputs = [('TestStrategy', 'Strategy1'), ('TestStrategy', 'Strategy2'), ('StrategyTest', 'Strategy1'),
                  ('StrategyTest', 'Strategy2')]
        validation_methods = {
            self.config_file_reader_mock_up.get_read_property_called_with_parameters: [
                {
                    'section_name': 'TestStrategy strategies',
                    'property_name': 'Strategy1'
                },
                {
                    'section_name': 'TestStrategy strategies',
                    'property_name': 'Strategy2'
                },
                {
                    'section_name': 'StrategyTest strategies',
                    'property_name': 'Strategy1'
                },
                {
                    'section_name': 'StrategyTest strategies',
                    'property_name': 'Strategy2'
                },
                {
                    'section_name': 'TestStrategy strategies',
                    'property_name': 'Strategy1'
                },
                {
                    'section_name': 'TestStrategy strategies',
                    'property_name': 'Strategy2'
                },
                {
                    'section_name': 'StrategyTest strategies',
                    'property_name': 'Strategy1'
                },
                {
                    'section_name': 'StrategyTest strategies',
                    'property_name': 'Strategy2'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1])]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_load_radiomics_params_file(self):
        method_to_test = self.configuration_service.load_radiomics_params_file
        outputs = ['TestParameterFilePath', 'ParameterFilePath']
        inputs = []
        validation_methods = {
            self.config_file_reader_mock_up.get_read_property_called_with_parameters: [
                {
                    'section_name': 'Radiomics',
                    'property_name': 'Parameter file location'
                },
                {
                    'section_name': 'Radiomics',
                    'property_name': 'Parameter file location'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1])]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_load_database_type(self):
        method_to_test = self.configuration_service.load_database_type
        outputs = ['TestDatabaseType', 'DatabaseTypeTest']
        inputs = []
        validation_methods = {
            self.config_file_reader_mock_up.get_read_property_called_with_parameters: [
                {
                    'section_name': 'Database',
                    'property_name': 'type'
                },
                {
                    'section_name': 'Database',
                    'property_name': 'type'
                }
            ]
        }
        return_value_mocked_methods = [(self.config_file_reader_mock_up.set_read_property_return_value, outputs[0]),
                                       (self.config_file_reader_mock_up.set_read_property_return_value, outputs[1])]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)
