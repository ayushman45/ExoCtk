from tqdm import tqdm
import os

class Converter: 
    def convert(self):
        folder_path = "data_values"
        csv_file_path = "csv_data/data.csv"
        files = os.listdir(folder_path)
        n = len(files)
        with tqdm(total=n) as pbar:
            for file in files:
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r") as f:
                    data = f.read().strip().split()
                    with open(csv_file_path, "a") as f2:
                        f2.write(','.join(data))
                        f2.write('\n')
                pbar.update(1)
        print("Conversion Completed.")

if __name__=="__main__":
    Converter().convert()