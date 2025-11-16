import os
import glob

#カレントディレクトリをmerukariに設定
path = "./"


#############################変えるところ##########################
j = 2004 #開始年度
n = 16 #平成何年か
##################################################################
work_dir = "Problems/"
search_path = os.path.join(path, work_dir, "*実施")
files = glob.glob(search_path)
files.sort()
    
for i, f in enumerate(files):
    
#############################変えるところ##########################
    name_to =  "阪大_問題_" + str(j) + "(" + m + ")年実施"
##################################################################
    os.rename(f, os.path.join(path + work_dir, name_to))
    j += 1
    n += 1
