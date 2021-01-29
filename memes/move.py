import os  
import shutil  

cur_dir = os.getcwd()
print(cur_dir)
list_dir = os.listdir(cur_dir)
print(list_dir)
dest = os.path.join(cur_dir,'/Users/rachel/Documents/greenturtle/memes/man-fuck-me-up') 
print(dest)

fin = open(os.getcwd() + '/m.csv',"r")
LL = [i for i in fin.read().split("\n") if i!= ""] 

for sub_dir in LL:
    if sub_dir in list_dir:
        dir_to_move = os.path.join(cur_dir, sub_dir)
        shutil.move(dir_to_move, dest)



