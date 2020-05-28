# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:28:37 2020

@author: rahma
"""

import pandas as pd

df = pd.read_csv('glassdoor_dejobs.csv')

 


#Salary Parsing
df = df[df['Salary Estimate'] != '-1']
df = df[df['Founded'] != -1]
df = df[df['Rating'] != -1]
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$','')) 

df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['Company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field
#df['job_state'] = df['Location'].apply(lambda x: x.split(",")[1] if  len(x.split(",")) == 2 else x.split(",")[0])
df['Job_State'] = df['Location'].apply(lambda x: x.split(',')[-1])
#df['Job_City'] = df['Location'].apply(lambda x: x.split([0]) 
df.Job_State.value_counts()

df['Same_State'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of Company
 df['Company_Age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#Parsing of job description ( python, Hadoop, Spark, AWS, CLOUD)
 df['Job Description'][1]
 #Python
 df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 df.python_yn.value_counts()
 #SQL
 df['SQL_yn'] = df['Job Description'].apply(lambda x: 1 if 'SQL' in x.lower() else 0)
 df.SQL_yn.value_counts()
 #Hadoop
 df['Hadoop_yn'] = df['Job Description'].apply(lambda x: 1 if 'Hadoop' in x.lower() else 0)
 df.Hadoop_yn.value_counts()
 #Spark
 #Hive
 #ETL
 #R Studio
 #Scala
 #AWS
 df['AWS_yn'] = df['Job Description'].apply(lambda x: 1 if 'AWS' in x.lower() else 0)
 df.AWS_yn.value_counts()

df.to_csv('glassdoor_cleandedata.csv', index = False)

pd.read_csv('glassdoor_cleandedata.csv')