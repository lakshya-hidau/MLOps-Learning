import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # Extract the traceback information
    _, _, exc_tb = error_detail.exc_info()

    # Get the filename and line number where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # Log the error message
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """
    Custom exception class that extends the base Exception class.
    It captures detailed error information upon initialization.
    """
    def __init__(self, error: Exception, error_detail: sys):
        """
        Initializes the MyException instance with detailed error information.

        :param error: The exception that occurred.
        :param error_detail: The sys module to access traceback details.
        """
        # Get the detailed error message using the helper function
        self.error_message = error_message_detail(error, error_detail)
        super().__init__(self.error_message)

    def __str__(self) -> str:
        """
        Returns the string representation of the MyException instance.

        :return: The detailed error message.
        """
        return self.error_message