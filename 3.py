import os
list_files = os.listdir()
list_files = list_files[:-1]

dict1 = {}
for file in list_files:
    if file.endswith('.txt'):
        with open(file) as f:
            counter = 0
            for line in f:
                counter += 1
        dict1[file] = counter

res_file = open('output.txt', 'a')
sorted_ = sorted(dict1.items(), key=lambda item: item[1])
sorted_dict = {k:v for k,v in sorted_}
for file in sorted_dict:
    res = f'{file}\n{dict1[file]}\n'
    res_file.write(res)
    with open(file, 'r') as text:
        for line in text:
            res_file.write(line)
    res_file.write('\n\n')
res_file.close()
