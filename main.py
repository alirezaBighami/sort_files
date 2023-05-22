import sys
import os
import time

def copy_to_file(file1, file2):
    with open(file1,'rb') as firstfile, open(file2,'wb') as secondfile:
        for line in firstfile:
            secondfile.write(line)

src_folder_path, dst_folder_path = sys.argv[1:]
all_flies = list(os.walk(src_folder_path))

os.makedirs(dst_folder_path, exist_ok=True)

for i in range(all_flies.__len__()):
    for file_name in all_flies[i][2]:
        first_file_path = all_flies[i][0] + os.sep + file_name
        created_at = time.ctime(os.path.getmtime(first_file_path))[-4 :]
        flag = False
        
        suffixes = [['.jpg', '.jpeg', '.png'], ['.mp4', '.avi', '.3gp', '.mpeg', '.mkv', '.wmv', '.mov']]
        if any(suffix in file_name.lower() for suffix in suffixes[0]):
            final_file_path = os.path.join(dst_folder_path , created_at , 'photos')
            flag = True
            
        elif any(suffix in file_name.lower() for suffix in suffixes[1]):
            final_file_path = os.path.join(dst_folder_path , created_at , 'videos')
            flag = True                
            
        if flag == True:
            if not os.path.exists(os.path.join(dst_folder_path , created_at)):
                os.makedirs(os.path.join(dst_folder_path , created_at), exist_ok=True)
            if not os.path.exists(final_file_path):
                os.makedirs(final_file_path, exist_ok=True)
            copy_to_file(first_file_path, os.path.join(final_file_path, file_name))

