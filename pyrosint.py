import re
import sys
import requests
from typing import Dict

class Pyrosint:

    API_HOST = 'https://mediafire.com'
    API_FILE_INFO_ENDPOINT = '/api/1.5/file/get_info.php'

    def get_file_info(self, quick_key: str) -> Dict:
        data = {
            'recursive': 'yes',
            'quick_key': quick_key,
            'response_format': 'json'
        }
        res = requests.post('{0}{1}'.format(self.API_HOST, self.API_FILE_INFO_ENDPOINT), data=data)
        return res.json()

if __name__ == '__main__':
    print('''\033[0;31m
        ⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
        ⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
        ⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
        ⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
        ⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
        ⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
        ⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
        ⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
        ⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
        ⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
    \033[0m''')

    if len(sys.argv) < 2:
        print('Usage: pyrosint.py <quick_key|mediafire_file_url>')
        exit()

    input_data = sys.argv[1]
    result = re.search(r"mediafire\.com\/file\/(\w+)\/", input_data)
    if result == None and '.com' in input_data:
        print('Error: No valid URL provided')
        exit()
    elif result != None and len(result.groups()) > 0:
        quick_key = result.group(1)
    else:
        quick_key = input_data

    pyrosint = Pyrosint()
    result = pyrosint.get_file_info(quick_key)
    if result['response']['result'] == 'Error':
        print('The provided quick key ({0}) does not exists'.format(quick_key))
    else:
        print('\033[0;32mFilename:\033[0m {}'.format(result['response']['file_info']['filename']))
        print('\033[0;32mUploaded:\033[0m {} UTC'.format(result['response']['file_info']['created_utc']))
        if result['response']['file_info']['description'] != '':
            print('\033[0;32mDescription:\033[0m {}'.format(result['response']['file_info']['description']))
        print('\033[0;32mSize:\033[0m {} bytes'.format(result['response']['file_info']['size']))
        print('\033[0;32mHash:\033[0m {}'.format(result['response']['file_info']['hash']))
        print('\033[0;32mOwner:\033[0m {}'.format(result['response']['file_info']['owner_name']))
        print('\033[0;32mLink:\033[0m {}'.format(result['response']['file_info']['links']['normal_download']))