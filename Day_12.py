# File Operations
# You will want to use veidenbaums.txt for analysis. It is in the class git repository under Day12_File_Operations folder
# You can also download it directly from the following link:
# https://raw.githubusercontent.com/ValRCS/Python_TietoEvry_Sep2021/main/Day12_File_Operations/veidenbaums.txt
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972

print("UZD- 1a.File Operations")


def get_file_len(file_name):
    file_len = 0
    with open(file_name, encoding='UTF-8') as f:
        for _ in f:
            file_len += 1
    return file_len


print(f" The length of the file is: ", (get_file_len('Veidenbaums.txt')))

# 1b -> write the function get_poem_lines (fpath), which returns a list with only those lines that contain poetry.
# So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.
# PS preferably use encoding = "utf-8"

print("UZD- 1b.")


def get_poem_lines(file_name):
    p_lines = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            if line.strip() and "***" not in line:
                p_lines.append(line)
    return p_lines


print(f" The lines that contain poetry: ",(len(get_poem_lines('veidenbaums.txt'))))


# 1c -> write the function save_lines (destpath, lines)
# This function will store all lines into destpath file
# 1d -> call save_lines with destpath being "veid_poems.txt" and lines being the poem lines we cleaned from 1b


print("UZD- 1c/1d.")

def save_lines(file_name):