# Data provider for Mondrian's paintings
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd


class Provider:
    """
    Data provider for Mondrian's paintings
    """

    entities = ["features", "info"]

    
    attrz = {
        "features": ["id", "shape", "x", "y", "w", "h", "col", "rgb"],
        "info": ["id", "year", "title", "w", "h", "complexity"],
    }

    def __init__(self):
        '''
        Initialize lists, data frames etc
        
        :param self
        '''
        self.features = pd.read_csv("dta/feature.csv")
        self.info = pd.read_csv("dta/fullinfo.csv")

    def uniq(self, attr="id", entity="features"):
        """
         Get a list of uniqe attribute values from entity

        :param self: self
        :param attr: attribute
        :param entity: entity ('features' | 'info') to get attribute list from
        """

        if entity not in self.entities:
            raise Exception(f"Entity {entity} does not exist!")

        df = self.features if entity == "features" else self.info
        print([df, attr, entity])
        return df[attr].unique()

    def row(self, id, attr=None):
        '''
        Getting row from info data frame
        
        :param self
        :param id: id of painting
        :param attr: optional attribute(s) to retrieve only
        '''
        if attr == None:
            return self.info.query("id == @id")
        else:
            return self.info.query("id == @id")[attr]


    
    def info_attr_by_id(self, id, attr):
        '''
        Retrieving certain attribute from info entity by given id
        
        :param self: 
        :param id: ID of row from entity
        :param attr: name of attribute to get
        '''
        return self.info.query("id == @id")[attr].item()


if __name__ == "__main__":
    p = Provider()
    # print(p.info['id'].unique())
    # print(p.features['id'].unique())
    # print(p.info.describe())
    # print(p.features.describe())

    # print(p.uniq(entity="info", attr="id"))

    print(p.row(id="b105", attr="title"))
