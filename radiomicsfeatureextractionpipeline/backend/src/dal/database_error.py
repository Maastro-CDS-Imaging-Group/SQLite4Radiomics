"""
Used for passing custom exceptions from the dal to the rest of the application.
"""

class DatabaseError(Exception):
    """
    Raised when error occurred while connecting to database or querying the data of the Database.
    """
    pass
