print("Please enter the complete file path:")
input_path = input()
path_file = input_path.replace('\\','\\\\')
print(path_file)
path_file = open(path_file, 'r')

print(path_file.read())
