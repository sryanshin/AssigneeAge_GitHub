#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import time
import warnings
warnings.filterwarnings('ignore')

t0=time.time()

srcFiles="../csvResults/rawData/"

# loads assignee dataset and filters for US company or corp (2)
stateless1=pd.read_csv(os.path.join(srcFiles,"finalTestDataset_output_v1_cleaned.csv"),
                       usecols=['ID_from_input_file','name'])
stateless1.rename(columns={'ID_from_input_file':'assignee_id'},inplace=True)
stateless1.name=stateless1.name.str.title()

stateless2=pd.read_csv(os.path.join(srcFiles,"finalTestDataset_output_2nd_cleaned.csv"),
                       usecols=['assignee_id','name'])
stateless2.name=stateless2.name.str.title()

stateless3=pd.read_csv(os.path.join(srcFiles,"lastFirms_output_cleaned.csv"),
                       usecols=['assignee_id','name'])
stateless3.name=stateless3.name.str.title()

stateless4=pd.read_csv(os.path.join(srcFiles,"lastLastFirms_output_cleaned.csv"),
                       usecols=['assignee_id','name'])
stateless4.name=stateless4.name.str.title()


t1=time.time()
total=t1-t0
print("Total time is %4f" % (total/60), "mins\n")

display(stateless1.info(null_counts=True),stateless1.head())
print("\n")
display(stateless2.info(null_counts=True),stateless2.head())
print("\n")
display(stateless3.info(null_counts=True),stateless3.head())
print("\n")
display(stateless4.info(null_counts=True),stateless4.head())


# In[ ]:





# In[2]:


t0=time.time()

combine=pd.concat([stateless1,stateless2,
                   stateless3,stateless4],axis=0).dropna(subset=['name']).drop_duplicates(subset=['assignee_id'],
                                                                                                     keep='first')

t1=time.time()
total=t1-t0
print("Total time is %4f" % (total/60), "mins\n")

display(combine.info(null_counts=True),combine.head())


# In[ ]:





# In[3]:


t0=time.time()

srcFiles1="../csvResults"

xwalk=pd.read_csv(os.path.join(srcFiles1,"xwalkAssignees.csv"))

t1=time.time()
total=t1-t0
print("Total time is %4f" % (total/60), "mins\n")

display(xwalk.info(null_counts=True),xwalk.head())


# In[ ]:





# In[4]:


t0=time.time()

xwalkCombine=combine.merge(xwalk,left_on=['assignee_id'],right_on=['assignee_id2'],how='inner')

t1=time.time()
total=t1-t0
print("Total time is %4f" % (total/60), "mins\n")

display(xwalkCombine.info(null_counts=True),xwalkCombine.head())


# In[ ]:





# In[5]:


t0=time.time()

srcFiles1="../csvResults"

mainFile=pd.read_csv(os.path.join(srcFiles1,"dfFinalDatasetAssignee.csv"),
                     usecols=['ID','assignee','organization'])

t1=time.time()
total=t1-t0
print("Total time is %4f" % (total/60), "mins\n")

display(mainFile.info(null_counts=True),mainFile.head())


# In[ ]:





# In[6]:


t0=time.time()

test3=mainFile.merge(xwalkCombine,left_on=['assignee'],right_on=['assignee_id1'],how='inner')

t1=time.time()
total=t1-t0
print("Total time is %4f" % (total/60), "mins\n")

display(test3.info(null_counts=True),test3.head())


# In[7]:


# test3.to_csv("../csvResults/2022PV50000StatexWalk.csv",index=False)


# In[ ]:




