#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install wordcloud


# In[5]:


pip install pythainlp


# In[6]:


from wordcloud import WordCloud # ใช้ทำ Word Cloud
import pandas as pd # ใช้โหลดข้อมูลและสร้างข้อมูล
import matplotlib.pyplot as plt # ใช้ Visualize Word Cloud
from pythainlp.tokenize import word_tokenize # เป็นตัวตัดคำของภาษาไทย
from pythainlp.corpus import thai_stopwords # เป็นคลัง Stop Words ของภาษาไทย 


# In[9]:


df = pd.read_excel('Durian.xlsx') # โหลดข้อมูลไฟล์ Excel ของเรา
df


# In[13]:


df = df.dropna()


# In[14]:


text = ''
for row in df.Content.values:       # ให้ python อ่านข้อมูลรีวิวจากทุก row ใน columns 'content'
    text = text + row.lower() + ' ' # เก็บข้อมูลรีวิวของเราทั้งหมดเป็น String ในตัวแปร text


# In[15]:


wt = word_tokenize(text, engine='newmm') # ตัดคำที่ได้จากตัวแปร text 


# In[16]:


wordcloud = WordCloud(
                      font_path='MN Pla Krop.ttf', # font ที่เราต้องการใช้ในการแสดงผล เราเลือกใช้ THSarabunNew 
                      stopwords=thai_stopwords(), # stop words ที่ใช้ซึ่งจะโดนตัดออกและไม่แสดงบน words cloud 
                      relative_scaling=0.3,
                      min_font_size=1,
                      background_color = "white",
                      width=1024,
                      height=768,
                      max_words=500, # จำนวนคำที่เราต้องการจะแสดงใน Word Cloud
                      colormap='plasma', 
                      scale=3,
                      font_step=4,
                      collocations=False,
                      regexp=r"[ก-๙a-zA-Z']+", # Regular expression to split the input text into token
                      margin=2
                      ).generate(' '.join(wt)) # input คำที่เราตัดเข้าไปจากตัวแปร wt ในรูปแบบ string


# In[17]:


fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.show()


# In[ ]:




