import os
folder_path="data_values"
files = os.listdir(folder_path)
for file in files:
    file_path = os.path.join(folder_path, file)
    with open(file_path,"r")as f:
        data = f.read().strip().split(' ')
        name=file[:-4]
        with open("csv_data/{}.csv".format(name),"w") as f2:
            f2.write(','.join(data))
        