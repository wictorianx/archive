import os
root = os.getcwd()
final_files = {}
dirs_pass = [root]
while(True):
    files = []
    dirs = []
    if len(dirs_pass) == 0:
        break
    rt = dirs_pass[0]
    dirs_pass.pop(0)
    content = os.listdir(rt)
    for i in content:
        try:
            os.listdir(i)
            dirs.append(i)
        except:
            files.append(i)
    final_files[root] = files
    for a_dir in dirs:
        dirs_pass.append(a_dir)
print(final_files)
