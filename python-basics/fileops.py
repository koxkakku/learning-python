# to create a file
# _file = open("file_output\\test_file.txt", 'x')
# _file.close()


# write to a file. this operation creates a new file if it doesnot exist
# _write_file = open("file_output\\test_file.txt", 'a')
# _write_file.write("\nMy name is python. \n I am high level programming language")
# _write_file.flush()
# _write_file.close()

# overwrite contents of file. this operation creates a new file if it doesnot exist
# _overwrite_file = open("file_output\\test_file.txt", 'w')
# _overwrite_file.write("\nI am overwritten")
# _overwrite_file.flush()
# _overwrite_file.close()

# read a file
# _read_file = open("file_output\\test_file.txt", 'r')
# print(_read_file.read())
# _read_file.close()

# read binary content
# _read_bin_file = open("file_input\\Screenshot.png", 'rb')
# bin_content = _read_bin_file.read()
# _read_bin_file.close()

# _create_new_file = open("file_output\\newimg.png", 'x')
# _create_new_file.close()

# write binary content. it creates a new file if it does not exist
# _write_bin_content = open("file_output\\newimg.png", 'wb')
# _write_bin_content.write(bin_content)
# _write_bin_content.flush()
# _write_bin_content.close()

# copy contents of one file to another without new lines
input_file = open("file_input\\input.txt")
input_txt = input_file.read()
input_file.close()
print(len(input_txt.split()))
output_txt = input_txt.replace("\n", ' ')
output_file = open("file_output\\output.txt", 'w')
output_file.write(output_txt)
output_file.flush()
output_file.close()
