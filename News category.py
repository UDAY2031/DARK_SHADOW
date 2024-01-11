#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
nltk.download()


# In[3]:


import pandas as pd 
fake=pd.read_csv("Fake.csv")
genuine=pd.read_csv("True.csv")


# In[4]:


display(genuine.info())
display(fake.info())
display(genuine.head(10))
display(fake.subject.value_counts())


# In[5]:


fake['target']=0
genuine['target']=1


# In[6]:


data=pd.concat([fake,genuine],axis=0)


# In[7]:


date=data.reset_index(drop=True)
data =data.drop(['subject','date','title'],axis=1)


# In[8]:


from nltk.tokenize import word_tokenize


# In[9]:


data['text']=data['text'].apply(word_tokenize)


# In[10]:


print(data.head(10))


# In[11]:


from nltk.stem.snowball import SnowballStemmer
porter=SnowballStemmer("english")


# In[12]:


def stem_it(text):
    return [porter.stem(word) for word in text]


# In[13]:


data['text']=data['text'].apply(stem_it)


# In[14]:


print(data.head(10))


# In[15]:


from nltk.corpus import stopwords


# In[16]:


def stop_it(t):
    dt=[word for word in t if len(word)>2]
    return dt


# In[17]:


data['text']=data['text'].apply(stop_it)


# In[18]:


print(data.head(10))


# In[19]:


data['text']=data['text'].apply(' '.join)


# In[28]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data['text'],data['target'])
display(x_train.head())
print('\n')
display(y_train.head())


# In[30]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[31]:


vectorizer = TfidfVectorizer(max_df=0.7, stop_words="english") 

tfidf_train = vectorizer.fit_transform(x_train)

tfidf_test = vectorizer.transform(x_test)


# In[32]:


print(tfidf_train)


# # Logistic Regression

# In[34]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[36]:


model_1=LogisticRegression(max_iter=900)
model_1.fit(tfidf_train,y_train)
pred_1=model_1.predict(tfidf_test)
cr1=accuracy_score(y_test,pred_1)
print(cr1*100)


# # Passive Aggressive Classifier

# In[37]:


from sklearn.linear_model import PassiveAggressiveClassifier


# In[39]:


model=PassiveAggressiveClassifier(max_iter=50)
model.fit(tfidf_train,y_train)
y_pred=model.predict(tfidf_test)
accs=accuracy_score(y_test,y_pred)
print("The accuracy of the prediction is",accs*100)


# 

# In[ ]:





# In[50]:





# In[ ]:




