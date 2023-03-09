set path "%PATH%;C:\Users\ankit\Desktop\final 2.0 - Copy - Copy (2)\chromedrivers" 
move new.txt dist
move run_this_file.bat dist
cd dist
attrib +h new.txt
start run_this_file.bat
exit