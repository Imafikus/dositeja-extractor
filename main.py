import re


with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
    all_lines = f.readlines()
    
starting_place = 1
ending_place = 2050


# print(all_lines[:200])

current_place = 1


# def extract_info(row):
#     print(row)
#     name = row[1].strip()
#     surname = row[3].strip()
#     level = row[4].strip()
#     for idx, possible_gpa in enumerate(row):
#         if re.match("[0-9],[0-9]{2}", possible_gpa.strip()) is not None:
#             gpa = possible_gpa.strip()
#             break
#         if re.match("[0-9],", possible_gpa.strip()) is not None:
#             gpa = possible_gpa.strip() + row[idx+1].strip()
#             break
    
#     print(f'{name}, {surname}, {level}, {gpa}')
            

# for idx, line in enumerate(all_lines):
#     content = []
    
#     if current_place == ending_place:
#         break
#     if line.strip() == str(current_place):
#         extract_info(all_lines[idx:idx+20])
#         current_place +=1
    
# idx = 0

idx = 0
while idx < len(all_lines):
    if current_place == ending_place:
        break
    tmp = 0
    if all_lines[idx].strip() == str(current_place):
        while all_lines[idx + tmp].strip() != str(current_place + 1):
            tmp += 1
        single_student = all_lines[idx:idx+tmp]
        print(single_student)
    idx += tmp
    current_place += 1