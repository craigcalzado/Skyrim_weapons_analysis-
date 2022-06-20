import kaggle 
import pandas as pd
import os

def acquire_weapons(use_cache=True):
    '''
    This function utilizes Kaggle API to acquire skyrim weapons.
    Before running this function, you must have a Kaggle API key.
    '''
    filename = 'Skyrim_Weapons.csv'
    if os.path.exists(filename) and use_cache:
        print('Using cached file...')
        return pd.read_csv(filename)
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('elmartini/skyrim-weapons-dataset', path='./' , unzip=True)
    df = pd.read_csv('skyrim_weapons.csv')
    return df