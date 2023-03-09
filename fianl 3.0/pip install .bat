pip install selenium
pip install pyinstaller
python write_input.py
python create_batch_file.py
pyinstaller --onefile main.py
start pip_install3.bat

@REM setx path "%PATH%;C:\Users\KIIT\Desktop\KIIT Classes\6th sem\New folder"
@REM move new.txt dist
@REM move run_this_file.bat dist
@REM cd dist
@REM attrib +h new.txt
@REM start run_this_file.bat
exit
