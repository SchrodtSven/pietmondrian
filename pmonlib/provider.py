# Data provider for Mondrian's paintings
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

class Provider:
    '''
    Data provider for Mondrian's paintings
    '''
    
    entities = ['features', 'info']

    def __init__(self):
        self.features = pd.read_csv('dta/feature.csv')
        self.info = pd.read_csv('dta/info.csv')

    def uniq(self, attr='id', entity='features'):
        '''
         Get a list of uniqe attribute values from entity
        
        :param self: self
        :param attr: attribute 
        :param entity: entity ('features' | 'info') to get attribute list from
        '''

        if entity not in self.entities:
            raise Exception(f'Entity {entity} does not exist!')

        df = self.features if entity == 'features' else self.info
        print([df, attr, entity])
        return df[attr].unique()

    
if __name__ == '__main__':
    p = Provider()
    #print(p.info['id'].unique())
    #print(p.features['id'].unique())
    #print(p.info.describe())
    #print(p.features.describe())

    print(p.uniq(entity='info', attr='title'))