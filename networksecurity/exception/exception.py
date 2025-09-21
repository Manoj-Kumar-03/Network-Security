import os
import sys
from networksecurity.logging.logger import logging

def get_error_message_deatails(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] and error is [{2}]".format(
        file_name,exc_tb.tb_lineno,error
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message = get_error_message_deatails(error=error_message,error_details=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        logging.info("code has stated")
        a = 25/5
        logging.info(f"a values is {a}")
        b = 5/0
        logging.info("Not print")
    except Exception as e:
        raise CustomException(e,sys)