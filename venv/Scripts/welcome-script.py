#!C:\Users\manoj\PycharmProjects\project1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'welcome==0.0.1','console_scripts','welcome'
__requires__ = 'welcome==0.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('welcome==0.0.1', 'console_scripts', 'welcome')()
    )
