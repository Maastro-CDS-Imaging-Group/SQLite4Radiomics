"""
Used for passing custom exceptions form the configuration_service to the rest of the application.
"""

class ConfigurationError(Exception):
    """Raised when error occurred while loading or saving properties"""
    pass
