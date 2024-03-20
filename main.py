from ExoCtk import ExoCtk
from Random import Random
from FileHelper import FileHelper
exo_ctk=ExoCtk()
def generateData(temp,g,r_planet,r_star):
    data_file=exo_ctk.generate_values(temp,g,r_planet,r_star)
    if data_file:
        folder_path="data_values"
        filename = '{}.txt'.format(Random().generate(10))
        FileHelper().insertOne(folder_path,filename,data_file)

FileHelper().removeAll("data_values")
temp=[400,500,600]
g=[5,10,15]
r_planet=[5,4,6]
r_star=[3,5,6,100]
for i in temp:
    for j in g:
        for k in r_planet:
            for l in r_star:
                generateData(i,j,k,l)