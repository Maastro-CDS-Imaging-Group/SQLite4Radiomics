from abc import ABC
import unittest
from typing import Callable, Any, List, Tuple, Optional, Dict


class MockedUnitTester(ABC, unittest.TestCase):

    def load_test_setup(
            self,
            method_to_test: Callable[[Any], Any],
            expected_outputs: List[Any],
            inputs: List[Any],
            validation_methods: Dict[Callable[[None], List[Dict[Optional[str], Any]]], List[Dict[Optional[str], Any]]],
            return_values_mocked_methods: List[Tuple[Callable[[Any], None], Any]]):

        iteration = 0

        test_data = []
        for index in range(len(expected_outputs) + len(inputs)):
            if len(inputs) != 0 and len(expected_outputs) != 0:
                # validations_per_iteration = int(len(validation_methods) / len(expected_outputs) / len(inputs))
                return_values_mocked_methods_per_iteration = int(len(return_values_mocked_methods)
                                                                 / len(expected_outputs) / len(inputs))
                test_data.append((
                    expected_outputs[index // len(inputs)],
                    inputs[index % len(inputs)],
                    # validation_methods[validations_per_iteration * iteration:
                    #                    validations_per_iteration * (iteration + 1)],
                    return_values_mocked_methods[return_values_mocked_methods_per_iteration * iteration:
                                                 return_values_mocked_methods_per_iteration * (iteration + 1)]))

            elif len(expected_outputs) != 0:
                # validations_per_iteration = int(len(validation_methods) / len(expected_outputs))
                return_values_mocked_methods_per_iteration = int(len(return_values_mocked_methods)
                                                                 / len(expected_outputs))
                test_data.append((
                    expected_outputs[index % len(expected_outputs)],
                    (),
                    # validation_methods[validations_per_iteration * iteration:
                    #                    validations_per_iteration * (iteration + 1)],
                    return_values_mocked_methods[return_values_mocked_methods_per_iteration * iteration:
                                                 return_values_mocked_methods_per_iteration * (iteration + 1)]))
            elif len(inputs) != 0:
                # validations_per_iteration = int(len(validation_methods) / len(inputs))
                return_values_mocked_methods_per_iteration = int(len(return_values_mocked_methods) / len(inputs))
                test_data.append((
                    None,
                    inputs[index % len(inputs)],
                    # validation_methods[validations_per_iteration * iteration:
                    #                    validations_per_iteration * (iteration + 1)],
                    return_values_mocked_methods[return_values_mocked_methods_per_iteration * iteration:
                                                 return_values_mocked_methods_per_iteration * (iteration + 1)]))

            else:
                test_data.append((None, (), validation_methods, return_values_mocked_methods))
            iteration += 1

        for data in test_data:
            self.template_for_load_property_tests(method_to_test, data[0], data[1], data[2])

        for validation_method, validation_results in validation_methods.items():
            for index, validation_result in enumerate(validation_results):
                print(index)
                self.assertEqual(validation_result, validation_method()[index])

    def template_for_load_property_tests(
            self, method_to_test: Callable[[Any], Any],
            expected_output: Any,
            input: Tuple[Any],
            # validation_methods: List[Tuple[Any, Callable[[None], Any]]],
            return_values_mocked_methods: List[Tuple[Callable[[Any], None], Any]]):

        for return_value_mocked_method in return_values_mocked_methods:
            return_value_mocked_method[0](return_value_mocked_method[1])

        return_value = method_to_test(*input)

        self.assertEqual(expected_output, return_value)

        # print(validation_methods)

        # for validation_method in validation_methods:
        #     print(validation_method)
        #     self.assertEqual(validation_method[0], validation_method[1]())