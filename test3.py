import re

input_string = "DICT-DNDFC_221_FT_DCNG_Lab01GrpA/1"

def extract_info(input_string):
    match = re.match(r'([^_]+)_(.+?)/', input_string)
    if match:
        module_code = match.group(1)
        session_name = match.group(2)
        return module_code, session_name
    
    else:
        return None, None

extract_info(input_string)

