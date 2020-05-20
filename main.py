# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:15:50 2020

@author: rahma
"""

import glassscrap as gs
import pandas as pd

path = "C:/Users/rahma/Documents/ds_salry_proj/chromedriver"

df = gs.get_jobs('data engineer',15, False, path, 15) #this will scrap 20 fields 