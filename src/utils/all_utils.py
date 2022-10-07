import yaml
import os


def read_yaml(path_yaml_file:str)->dict:
    with open(path_yaml_file) as yaml_file:
        content = yaml.safe_load(yaml_file)


    return content


def create_directory(dirs:list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)


def save_local_df(data,data_path):

    data.to_csv(data_path,index=False)
    print("Data is saved at {}".format(data_path))



