# File Operations
# You will want to use veidenbaums.txt for analysis. It is in the class git repository under Day12_File_Operations folder
# You can also download it directly from the following link:
# https://raw.githubusercontent.com/ValRCS/Python_TietoEvry_Sep2021/main/Day12_File_Operations/veidenbaums.txt
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972

print("UZD- 1.File Operations")

def get_file_len(file_name):
    file_len = 0
    with open(file_name, encoding='UTF-8') as f:
        for _ in f:
            file_len += 1
    return file_len


print(f" The length of the file is: ", (get_file_len('Veidenbaums.txt')))


