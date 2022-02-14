
# coding: utf-8

# In[33]:


import pandas as pd


# In[93]:


bank_full=pd.read_csv("C://Users//sthakal//OneDrive - George Weston Limited-6469347-MTCAD//Psnal//Ryerson_Big_Data Certification_Final_Project//Data Set//bank-additional-full.csv",sep = ";")


# In[94]:


bank_full.head(15)


# In[114]:


bank_full.isna().count()


# In[115]:


bank_full.corr()


# In[111]:


bank_full.shape


# In[99]:


bank_full.hist('age')


# In[116]:


job_cnt=bank_full['job'].value_counts()
print(job_cnt)


# In[117]:


bank_full['marital'].value_counts()


# In[120]:


bank_full['education'].value_counts()


# In[121]:


bank_full['month'].value_counts()


# In[122]:


#understanding the count of the Predictor variable

bank_full['y'].value_counts()


# In[105]:


bank_full['default'].value_counts()

