import re

regex_username = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'
username = input('')
if re.fullmatch(regex_username, username) != None:
    print ('OK')
else:
    print('WRONG')