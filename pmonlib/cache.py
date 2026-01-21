# Data provider for Caching Mondrian's paintings' (meta) data & static files
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-21

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from typing import Self, Any

class Cache:
    '''
    Local Cache for painting (meta) data
    '''

    # list of indices
    idc = [ 'b104', 'b105', 'b106', 'b107', 'b108', 'b109', 'b113', 'b114', 'b115', 'b116',
            'b117', 'b120', 'b121', 'b122', 'b123', 'b125', 'b126', 'b128', 'b129', 'b130',
            'b131', 'b132', 'b133', 'b134', 'b135', 'b136', 'b137', 'b138', 'b139', 'b141',
            'b142', 'b143', 'b144', 'b145', 'b146', 'b147', 'b150', 'b159', 'b160', 'b162',
            'b163', 'b170', 'b172', 'b182', 'b183', 'b185', 'b187', 'b188', 'b189', 'b190',
            'b191', 'b192', 'b193', 'b194', 'b195', 'b196', 'b197', 'b198', 'b199', 'b200',
            'b201', 'b203', 'b204', 'b206', 'b207', 'b208', 'b209', 'b210', 'b212', 'b213',
            'b214', 'b215', 'b216', 'b217', 'b219', 'b220', 'b221', 'b222', 'b223', 'b224',
            'b225', 'b226', 'b227', 'b228', 'b230', 'b231', 'b232', 'b233', 'b234', 'b235',
            'b236', 'b237', 'b238', 'b239', 'b240', 'b243', 'b244', 'b245', 'b252', 'b253',
            'b254', 'b255', 'b256', 'b257', 'b259', 'b260', 'b261', 'b262', 'b263', 'b264',
            'b265', 'b266', 'b267', 'b268', 'b269', 'b271', 'b272', 'b273', 'b274', 'b275',
            'b276', 'b277', 'b279', 'b280', 'b281', 'b283', 'b284', 'b285', 'b286', 'b287',
            'b288', 'b292', 'b293', 'b294', 'b295', 'b296']
    
    @staticmethod
    def path_by_id(idx):
        return  f'assets/img/{idx}.svg'