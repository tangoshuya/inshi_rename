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


    # if j == 2020:
    #     j = j + 1
    #     n = n + 1
    
    if n <= 30:
        m = "H" + str(n)
    if n == 31:
        m = "H31·R1"
    if n >= 32:
        m = "R" + str(n - 30)

    
#############################変えるところ##########################
    name_to =  "阪大_問題_" + str(j) + "(" + m + ")年実施"
##################################################################
    os.rename(f, os.path.join(path + work_dir, name_to))
    j += 1
    n += 1
