import os
import msvcrt
import sys

name_of_file = "new.txt"

userid = input("Enter your Roll no :")


# pas = input("Enter you Password : ")

def getpass(prompt="Enter password: "):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    password = ""
    while True:
        ch = msvcrt.getch().decode("utf-8")
        if ch == "\r" or ch == "\n":
            sys.stdout.write("\n")
            return password
        elif ch == "\b" or ord(ch) == 127:
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            password += ch
            sys.stdout.write("*")
            sys.stdout.flush()

password = getpass()


# Ask user what the file must store once it's created
# The format is open(filename, mode) and in this case, opens name_of_file in write mode
f = open(name_of_file, 'w')
# Write content_of_file input in file object f from previous command.
f.write(userid)
f.write("\n")
f.close()

f = open(name_of_file, 'a')
f.write(password)
# Close the file object after encoding the content_of_file string
f.close()