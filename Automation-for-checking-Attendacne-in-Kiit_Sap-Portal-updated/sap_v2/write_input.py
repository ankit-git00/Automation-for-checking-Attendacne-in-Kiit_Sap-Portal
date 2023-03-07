name_of_file = "new.txt"

userid = input("Enter your Roll no :")
pas = input("Enter you Password : ")
# Ask user what the file must store once it's created
# The format is open(filename, mode) and in this case, opens name_of_file in write mode
f = open(name_of_file, 'a')
# Write content_of_file input in file object f from previous command.
f.write(userid)
f.write("\n")
f.write(pas)
# Close the file object after encoding the content_of_file string
f.close()