file_path = 'input.txt'
n=0
with open(file_path, 'r') as file:
    file_content = file.readlines()
while(n<len(file_path)):
     print(file_content[n])
     n+=1