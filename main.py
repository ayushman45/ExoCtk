from ExoCtk import ExoCtk
from FileHelper import FileHelper
from Converter import Converter

exo_ctk = ExoCtk()

def transform(data_file,temp, g,r_planet,r_star,metallicity, c_o,haze,cloud):
    res=[]
    temp_list=data_file.strip().split('\n')
    for i in temp_list:
        res.append(i.split()[1])

    res+=[temp, g,r_planet,r_star,metallicity, c_o,haze,cloud]
    return ' '.join(res)

def generateData(filename,temp, g, r_planet, r_star, metallicity, c_o, haze, cloud):
    data_file = exo_ctk.generate_values(
        temp, g, r_planet, r_star, metallicity, c_o, haze, cloud
    )
    if data_file:
        vector_file = (',').join(transform(data_file,temp, g,r_planet,r_star,metallicity, c_o,haze,cloud).split())
        folder_path = "data_values"
        FileHelper().insertOne(folder_path, filename, vector_file)
        print("{} generated in {}".format(filename,folder_path))

choice=input("Do you want to delete prev generated data ? (y/n): ")
if(choice=="y"):
    FileHelper().removeAll("data_values")
    print("Deleted all previously generated data")

#dummy values for temperature
temp = ["400","600","700"]

#dummy values for gravity
g = ["5", "10"]

#dummy values for radius of planet
r_planet = ["1","1.5"]

#dummy value for radius of star
r_star = ["0.1","0.9"]

#dummy value for metallicity
metallicity = ["1", "10"]

#dummy value for carbon-oxygen ratio
c_o = ["0.35"]

#dummy value for haze
haze = ["0001"]

#dummy value for cloud
cloud = ["0.00"]

# for i in temp:
#     for j in g:
#         for k in r_planet:
#             for l in r_star:
#                 for m in metallicity:
#                     for n in c_o:
#                         for o in haze:
#                             for p in cloud:
#                                 filename = "{}x{}x{}x{}x{}x{}x{}x{}.csv".format(i,j,k,l,m,n,o,p)
#                                 if(FileHelper().findFile("data_values", filename)):
#                                     print("{} already exists".format(filename))
#                                     continue
#                                 generateData(filename,i, j, k, l, m, n, o, p)
Converter().convert()