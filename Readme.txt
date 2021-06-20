Read me file
# how to make a python program executable for Linux
  step 1 -> pip install pyinstaller
  step 2-> pyinstaller --onefile <your_script_name>.py will generate a single execuable file for linux

#how to make a python program executable on a mac
  step 1 -> pip install py2app
  step 2-> create a setup.py file for your project in the same directory
           from setuptools import setup
           APP = ['your python file name.py']
           OPTIONS = {
               'argv_emulation': True,
           }
           setup(
             app=APP,
             options={'py2app':OPTIONS},
             setup_requires = ['py2app']
           )

  step 3-> python3 setup.py py2app
  
  #how to make a python program executable on windows
  step-1 -> pip install auto-py-to-exe
  step-2 ->type auto-py-to-exe and use the GUI application to make your python file into an executable for windows operating system
