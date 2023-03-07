pip install selenium
pip install pyinstaller
python write_input.py
pyinstaller --onefile main.py
move new.txt dist
move run_this_file.bat dist
cd dist
start run_this_file.bat
