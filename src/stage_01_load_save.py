from src.utils.all_utils import read_yaml, create_directory , save_local_df
import pandas as pd
import argparse
import os
from sklearn.model_selection import train_test_split



def split_and_save(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    remote_data_path= config['data_set']
    df=pd.read_csv(remote_data_path,sep=';')
    #print(df.head())


    artifacts_dir=config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']




    split_ratio=params['base_params']['test_size']
    random_state = params['base_params']['random_state']




    raw_local_path=os.path.join(artifacts_dir,raw_local_dir)
    create_directory([raw_local_path])
    raw_local_file_path=os.path.join(raw_local_path,raw_local_file)

    df.to_csv(raw_local_file_path, sep=',', index=False)

    df=pd.read_csv(raw_local_file_path)
    df.to_csv(raw_local_file_path, sep=',', index=False)

    train,test= train_test_split(df,test_size=split_ratio,random_state=random_state)

    split_data_dir = config['artifacts']['split_data_dir']
    train_data_file_name= config['artifacts']['train']
    test_data_file_name = config['artifacts']['test']
    create_directory([split_data_dir])

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_file_name)
    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_file_name)

    for data, data_path in (train, train_data_path), (test,test_data_path):
        save_local_df(data, data_path)




    #print(raw_local_file_path)





if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config','-c',default='D:/Interview_prep/dvc/dvc_1/config/config.yaml')
    args.add_argument('--params', '-p', default='D:/Interview_prep/dvc/dvc_1/params.yaml')

    parsed_args= args.parse_args()

    split_and_save(config_path=parsed_args.config,params_path=parsed_args.params)

