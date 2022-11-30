import os 
import sys

class HousingException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.my_error_message = error_message
    
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        _,_,exec_traceback = error_detail.exc_info()
        linenumber = exec_traceback.tb_frame.f_lineno
        filename = exec_traceback.tb_frame.f_code.co_filename

        message = f"Error is occured here DumbAss [{filename}] in the line [{linenumber}] the exception is [{error_message}]"

        return message
    
    def __str__(self) -> str:
        return self.my_error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
        