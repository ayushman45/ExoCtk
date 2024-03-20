from ExoCtk import ExoCtk
from Random import Random
from FileHelper import FileHelper

exo_ctk = ExoCtk()


def generateData(temp, g, r_planet, r_star, metallicity, c_o, haze, cloud):
    data_file = exo_ctk.generate_values(
        temp, g, r_planet, r_star, metallicity, c_o, haze, cloud
    )
    if data_file:
        folder_path = "data_values"
        filename = "{}.txt".format(Random().generate(10))
        FileHelper().insertOne(folder_path, filename, data_file)


FileHelper().removeAll("data_values")
temp = [400]
for i in range(6, 27):
    temp.append(i * 100)
g = [5, 10, 20, 50]
r_planet = [5]
r_star = [3]
metallicity = ["0.0", "1.0", "1.7", "2.0", "2.3"]
c_o = ["0.35", "0.56", "0.70", "1.00"]
haze = ["0001", "0010", "0100", "1100"]
cloud = ["0.35", "0.56", "0.70", "1.00"]

for i in temp:
    for j in g:
        for k in r_planet:
            for l in r_star:
                for m in metallicity:
                    for n in c_o:
                        for o in haze:
                            for p in cloud:
                                generateData(i, j, k, l, m, n, o, p)
