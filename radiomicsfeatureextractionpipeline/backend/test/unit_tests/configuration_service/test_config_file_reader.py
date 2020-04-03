import os
import types
import unittest
from configparser import ConfigParser

from configuration_service.config_file_reader import ConfigFileReader
from configuration_service.configuration_error import ConfigurationError


class TestConfigFileReader(unittest.TestCase):

    def setUp(self) -> None:
        self.config_file_path = 'test.ini'

        if os.path.exists(self.config_file_path):
            os.remove(self.config_file_path)

        self.config_file_reader = ConfigFileReader(self.config_file_path)

    def tearDown(self) -> None:
        if os.path.exists(self.config_file_path):
            os.remove(self.config_file_path)

    def test_read_property_file_not_existing(self):
        self.file_not_existing_test(self.config_file_reader.read_property, 'test', 'test')

    def test_read_property_section_not_existing(self):
        section = 'test'
        option = 'test'

        self.section_not_existing_test(self.config_file_reader.read_property, section, section, option)

    def test_read_property_option_not_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'
        value = 'value'
        config_parser = ConfigParser()
        config_parser.add_section(section)
        config_parser.set(section, option, value)
        config_parser.write(open(self.config_file_path, 'a'))

        try:
            self.config_file_reader.read_property(section, 'test')
            self.fail("A ConfigurationError was expected but wasn't raised")
        except ConfigurationError as error:
            self.assertEqual(
                "The configuration file didn't have an option called {} within section {}".format("test", section),
                error.args[0])

    def test_read_property_section_and_option_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'
        value = 'value'

        with open(self.config_file_path, 'a') as config_file:
            config_parser = ConfigParser()
            config_parser.add_section(section)
            config_parser.set(section, option, value)
            config_parser.write(config_file)

        print(self.config_file_reader.config_parser.has_section(section))
        print(config_parser.has_section(section))

        self.config_file_reader.add_section('chapter')
        print(self.config_file_reader.config_parser.has_section('chapter'))
        print(config_parser.has_section('chapter'))

        config_file_reader_2 = ConfigFileReader(self.config_file_path)
        config_file_reader_2.add_section('sect')
        print(self.config_file_reader.config_parser.has_section('sect'))

        self.assertEqual(value, self.config_file_reader.read_property(section, option))

    def test_save_property_file_not_existing(self):
        self.file_not_existing_test(self.config_file_reader.save_property, 'test', 'test', 'test')

    def test_save_property_section_not_existing(self):
        section = 'test'
        option = 'test'
        value = 'test'

        self.section_not_existing_test(self.config_file_reader.save_property, section, section, option, value)

    def test_save_property_empty_value(self):
        open(self.config_file_path, 'x')

        section = 'section'
        config_parser = ConfigParser()
        config_parser.add_section(section)
        config_parser.write(open(self.config_file_path, 'a'))
        print(config_parser.has_section(section))

        try:
            self.config_file_reader.save_property(section, 'option', '')
            self.fail("A ConfigurationError was expected but wasn't raised")
        except ConfigurationError as error:
            self.assertEqual("Configuration file received an invalid property value", error.args[0])

    def test_save_property_create_new_option(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'
        value = 'value'

        config_parser = ConfigParser()
        config_parser.add_section(section)
        config_parser.write(open(self.config_file_path, 'a'))

        self.config_file_reader.save_property(section, option, value)
        self.assertTrue(config_parser.has_option(section, option))
        self.assertEqual(value, config_parser.get(section, option))

    def test_save_property_override_option(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'
        oldvalue = 'old'
        newvalue = 'new'

        config_parser = ConfigParser()
        config_parser.add_section(section)
        config_parser.set(section, option, oldvalue)
        config_parser.write(open(self.config_file_path, 'a'))

        self.config_file_reader.save_property(section, option, newvalue)
        self.assertTrue(config_parser.has_option(section, option))
        self.assertEqual(newvalue, config_parser.get(section, option))

    def test_add_section_file_not_existing(self):
        self.file_not_existing_test(self.config_file_reader.add_section, 'test')

    def test_add_section_that_already_exists(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'
        value = 'value'

        config_parser = ConfigParser()
        config_parser.add_section(section)
        config_parser.set(section, option, value)
        config_parser.write(open(self.config_file_path, 'a'))

        self.config_file_reader.add_section(section)

        self.assertTrue(config_parser.has_section(section))
        self.assertTrue(config_parser.has_option(section, option))
        self.assertEqual(value, config_parser.get(section, option))

    def test_add_section_not_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'

        self.config_file_reader.add_section(section)

        config_parser = ConfigParser()
        config_parser.read(self.config_file_path)

        self.assertTrue(config_parser.has_section(section))

    def test_get_all_properties_from_section_file_not_existing(self):
        self.file_not_existing_test(self.config_file_reader.get_all_properties_from_section, 'test')

    def test_get_all_properties_from_section_section_not_existing(self):
        section = 'test'
        self.section_not_existing_test(self.config_file_reader.get_all_properties_from_section, section, section)

    def test_get_all_properties_from_section_no_options(self):
        self.get_all_properties_form_section_test([])

    def test_get_all_properties_from_section_one_option(self):
        self.get_all_properties_form_section_test([('option1', 'value1')])

    def test_get_all_properties_from_section_multiple_options(self):
        self.get_all_properties_form_section_test([('option1', 'value1'), ('option2', 'value2'), ('option3', 'value3')])

    def test_section_exists_file_not_existing(self):
        section = 'test'
        self.file_not_existing_test(self.config_file_reader.section_exists, section)

    def test_section_exists_section_not_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'

        self.assertFalse(self.config_file_reader.section_exists(section))

    def test_section_exists_section_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'
        with open(self.config_file_path, 'a') as config_file:
            config_parser = ConfigParser()
            config_parser.add_section(section)
            config_parser.write(config_file)

        self.assertTrue(self.config_file_reader.section_exists(section))

    def test_option_exists_file_not_existing(self):
        self.file_not_existing_test(self.config_file_reader.option_exists, 'section', 'option')

    def test_option_exists_section_not_existing(self):
        self.section_not_existing_test(self.config_file_reader.option_exists, 'section', 'option')

    def test_option_exists_option_not_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'

        with open(self.config_file_path, 'a') as config_file:
            config_parser = ConfigParser()
            config_parser.add_section(section)
            config_parser.write(config_file)

        self.assertFalse(self.config_file_reader.option_exists(section, option))

    def test_option_exists_option_existing(self):
        open(self.config_file_path, 'x')

        section = 'section'
        option = 'option'
        value = 'value'

        with open(self.config_file_path, 'a') as config_file:
            config_parser = ConfigParser()
            config_parser.add_section(section)
            config_parser.set(section, option, value)
            config_parser.write(config_file)

        self.assertTrue(self.config_file_reader.option_exists(section, option))

    def file_not_existing_test(self, method: classmethod, *args):
        try:
            method(*args)
            self.fail("A ConfigurationError was expected but wasn't raised")
        except ConfigurationError as error:
            self.assertEqual("The configuration file {} couldn't be found or accessed!".format(self.config_file_path),
                             error.args[0])

        self.assertFalse(os.path.exists(self.config_file_path))

    def section_not_existing_test(self, method: classmethod, section: str, *args):
        open(self.config_file_path, 'x')

        try:
            method(*args)
            self.fail("A ConfigurationError was expected but wasn't raised")
        except ConfigurationError as error:
            self.assertEqual("The configuration file didn't have a section called {}".format(section), error.args[0])

    def get_all_properties_form_section_test(self, options_and_values):
        open(self.config_file_path, 'x')
        section = 'section'
        config_parser = ConfigParser()
        config_parser.add_section(section)
        for option, value in options_and_values:
            config_parser.set(section, option, value)
        config_parser.write(open(self.config_file_path, 'w'))

        properties = self.config_file_reader.get_all_properties_from_section(section)

        self.assertCountEqual(options_and_values, properties)

        i = 0
        for option, value in properties:
            self.assertEqual(options_and_values[i][0], option)
            self.assertEqual(options_and_values[i][1], value)
            i += 1