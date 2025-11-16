import os
import glob

#カレントディレクトリをmerukariに設定
path = "./"

#############################変えるところ##########################
folder = "Answers/" #フォルダ名
j = 2005 #開始年度
n = 17 #平成何年か
##################################################################
search_path = os.path.join(path, folder, "*.pdf")

files = glob.glob(search_path)
files.sort()
print(len(files))

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
    name_to =  "東大_解答（こぱんざめ）_" + str(j) + "(" + m + ")年実施.pdf"
##################################################################
    os.rename(f, os.path.join(path + folder, name_to))
    j += 1
    n += 1
    