# File Write


# Write to an Existing File *************************************************************************************************
#  To write to an existing file, you must add a parameter to the open() function:
#       "a" - Append - will append to the end of the file
#       "w" - Write - will overwrite any existing content

#  Example, Open the file "demofile2.txt" and append content to the file:

f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#       open and read the file after the appending:
f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile2.txt", "r")
print(f.read())


# Example, Open the file "demofile3.txt" and overwrite the content:
f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile3.txt", "w") #the "w" method will overwrite the entire file.
f.write("Woops! I have deleted the content!")
f.close()

#   open and read the file after the appending:
f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile3.txt", "r")
print(f.read())



# Create a New File ******************************************************************************************
#  To create a new file in Python, use the open() method, with one of the following parameters:
#       "x" - Create - will create a file, returns an error if the file exist
#       "a" - Append - will create a file if the specified file does not exist
#       "w" - Write - will create a file if the specified file does not exist

# Example, Create a file called "myfile.txt":

f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\myfile.txt", "x") #Result: a new empty file is created!

# Example, Create a new file if it does not exist:

f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\myfile.txt", "w")