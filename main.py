import pandas as pd 

with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
    all_lines = f.readlines()
    
starting_place = 1
ending_place = 2050



current_place = 1

idx = 0

all_students = []
while idx < len(all_lines):
    if current_place == ending_place:
        break
    tmp = 0
    if all_lines[idx].strip() == str(current_place):
        while all_lines[idx + tmp].strip() != str(current_place + 1):
            tmp += 1
        single_student = all_lines[idx:idx+tmp]
        all_students.append(single_student)
    idx += tmp
    current_place += 1
    
prepared_students = []
for student in all_students:
    prepared_students.append(f'{student[1].strip()}, {student[3].strip()}, {student[4].strip()}, {student[-1].strip()}')

for student in prepared_students:
    print(student)