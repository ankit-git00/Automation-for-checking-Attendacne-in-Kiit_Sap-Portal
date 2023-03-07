"""
In this, there would be a .bat file containing main.py  .  As we run the .bat file, main.py will execute which will create a new 'pip install.bat' file containig updated 
"""
import os
chromedir = """set path "%PATH%;""" + os.path.dirname(__file__) + """\chromedrivers" """

print("Current working directory:", chromedir)

f=open("pip_install2.bat",'w')
f.write(chromedir)
f.write("\nmove new.txt dist\nmove run_this_file.bat dist\ncd dist\nstart run_this_file.bat\n")
f.close()