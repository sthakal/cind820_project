
# coding: utf-8

# In[33]:


import pandas as pd


# In[93]:


bank_full=pd.read_csv("C://Users//sthakal//OneDrive - George Weston Limited-6469347-MTCAD//Psnal//Ryerson_Big_Data Certification_Final_Project//Data Set//bank-additional-full.csv",sep = ";")


# In[94]:


bank_full.head(15)


# In[96]:


bank_full.describe(include='all')


# In[97]:


bank_full.corr()


# In[98]:


bank_full.info()


# In[99]:


bank_full.hist('age')


# In[100]:


job_cnt=bank_full['job'].value_counts()
print(job_cnt)


# In[101]:


bank_full['marital'].value_counts()


# In[102]:


bank_full['education'].value_counts()


# In[103]:


bank_full['month'].value_counts()


# In[104]:


#understanding the count of the Predictor variable

bank_full['y'].value_counts()


# In[105]:


bank_full['default'].value_counts()

