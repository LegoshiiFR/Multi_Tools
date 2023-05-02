REM pip install pyinstaller
pyinstaller --onefile --icon=icon_v0_1.ico main.py
REM pip install cx_Freeze
python setup.py build
pause