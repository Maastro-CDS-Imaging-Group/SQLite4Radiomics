"""
This module inherits from the boostrapper module, but does not run on CLI. Instead, it has its own main method, but
takes advantage of the objects instantiation and other methods present in the bootsrapper module.
This module gets its input from a query and performs the feature extraction on the results.
"""

import sqlite3
from typing import Any
import time

from src.bootstrapper.radiomic_feature_extraction_pipeline_bootstrapper import Bootstrapper

class Calculator(Bootstrapper):



    def __init__(self) -> None:
        """
        Constructor of the Calculator.
        Variable as declared as well for use in the several functions
        """
        super().__init__()

        self.instances = []
        self.finished = 0
        self.cancelled: bool = False
        self.query_type = 'recalculate'
        self.progress = ''

    def main(self) -> None:
        self.get_progress()
        self.progress = 'Starting Calculation'
        self.get_progress()
        self.execute_calculation()
        time.sleep(3)
        self.progress = 'No process running or the process has finished'
        time.sleep(7)
        self.reset_variables()
        return


    def get_query_result(self) -> Any:
        """ create a database connection to the SQLite database and send the results
        for calculation
        """
        db_file = "../Conquest/data/dbase/conquest.db3"
        query_file = ''
        if self.query_type == 'recalculate':
            query_loc = "resources/queries/sqlite/get_sop_from_series.sql"
        
        elif self.query_type == 'update':
            query_loc = "resources/queries/sqlite/get_sop_from_pat_not_calculated.sql"

        with open(query_loc, 'r') as q:
            query_file = q.read()
        with sqlite3.connect(db_file) as conn:
            dbcursor = conn.cursor()
            rows = dbcursor.execute(query_file)
            id_data = dbcursor.fetchall()
            for row in id_data:
                self.instances.append(row[0])
        conn.close()
        self.progress = f'{self.finished} out of {len(self.instances)} finished'
        self.get_progress()



    def execute_calculation(self) -> Any:
        """ get the query results and perform feature extraction on each value.
        If the process is cancelled, first finish current calculation, and then stop
        """
        self.get_query_result()

        if len(self.instances) > 0:
            for value in self.instances:
                if not self.cancelled:
                    self.call_function(value)
                else:
                    self.set_cancelled()
                    self.progress = 'Process cancelled'
                    self.get_progress()
                    time.sleep(5)
                    return
        else:
            self.progress = 'No RTSTRUCT found! There are either no uncalculated RTSTRUCTs or there is no RTSTRUCT in your database.'
            self.get_progress()
            time.sleep(5)
            return

    def call_function(self, value) -> Any:
        """ Calls the feature extraction function and sets the progress value
        """
        self.logic.extract_features(value)
        self.finished += 1
        self.progress = f'{self.finished} out of {len(self.instances)} finished'
        self.get_progress()

    def set_cancelled(self) -> bool:
        """ Sets calculation process state to cancelled
        """
        self.cancelled = True
        return self.cancelled
    
    def set_not_cancelled(self) -> bool:
        """ Sets calculation process state to NOT cancelled
        """
        self.cancelled = False
        return self.cancelled

    def get_command(self) -> bool:
        """ Return the current state of the calculation process
        """
        return self.cancelled

    def reset_variables(self) -> Any:
        """ Resets the values of used variables
        """
        self.progress = ''
        self.finished = 0
        self.instances = []
        if self.cancelled:
            self.set_not_cancelled()

    def get_progress(self) -> str:
        """ Return progress value
        """
        print(self.progress)
        return self.progress

    def set_query_type_default(self) -> str:
        """ Sets query_type value for recalculation process.
        This uses a query to perform feature extraction on all data stored
        """
        self.query_type = 'recalculate'

    def set_query_type_update(self) -> str:
        """ Sets query_type value for recalculation process.
        This uses a query to perform feature extraction only on data with no calculation yet performed.
        This will usually be newly stored data
        """
        self.query_type = 'update'

    def set_csv_save_to_dump_all(self):
        self.data_access_layer.radiomic_feature_repos.set_to_dump_all()

    def set_csv_save_to_dump_individual(self):
        self.data_access_layer.radiomic_feature_repos.set_to_dump_individual()


if __name__ == "__main__":
    # If script was called by the Python interpreter, create an instance of the Calculator
    calculator = Calculator()

    # Start the calculation
    calculator.main()
