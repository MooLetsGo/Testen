import base64
import pyperclip

OKGREEN    = '\033[92m'
ENDC       = '\033[0m'

excelfile_path = "C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\VSCode\\Testen\\xlsxToB64\\Konrad_Moritz_2023-10-10_11-47.xlsx"


prefix = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
postfix = "\n"

with open(excelfile_path, 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    
    data_url = prefix + base64_encoded_data.decode('utf-8') + postfix

pyperclip.copy(data_url)
print(f"{OKGREEN}\r\n*** B64 block successfully copied to clipboard !!! ***\r\n{ENDC}")
