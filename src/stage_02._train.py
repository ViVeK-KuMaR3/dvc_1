from src.utils.all_utils import read_yaml, create_directory , save_local_df
import pandas as pd
import argparse
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet



def train_and_test(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    artifacts_dir = config['artifacts']['artifacts_dir']


    split_data_dir = config['artifacts']['split_data_dir']
    train_data_file_name = config['artifacts']['train']
    test_data_file_name = config['artifacts']['test']

    train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_file_name)
    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_file_name)

    train_data=pd.read_csv(train_data_path)

    train_X=train_data.drop('quality',axis=1)
    train_y=train_data["quality"]

    random_state = params['base_params']['random_state']
    l1_ratio=params['model_params']['ElasticNet']['params']['l1_ratio']
    alpha = params['model_params']['ElasticNet']['params']['alpha']

    lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)
    lr.fit(train_X,train_y)








if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config','-c',default='D:/Interview_prep/dvc/dvc_1/config/config.yaml')
    args.add_argument('--params', '-p', default='D:/Interview_prep/dvc/dvc_1/params.yaml')

    parsed_args= args.parse_args()

    train_and_test(config_path=parsed_args.config,params_path=parsed_args.params)

