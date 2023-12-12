#!/usr/bin/env python
# coding: utf-8

# In[2]:


def function_name():
    return("hello python")

x=function_name()

    
    
print(x)  
    


# In[10]:


def say_hello(name):
    
    print(f"hello {name}")
say_hello("mohamed")


# In[14]:


def addit(n1,n2):
    if type(n1) == int and type(n2)== int:
        print(n1+n2)
    else:
                    print("only ints allowed")
    
addit(200,"300")


# In[30]:


def full_name(first,middle,last):
    
           print(f"hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")
    
full_name("mohamed","khaled","elsaryaosi")


# In[35]:


def my_plane(first,article,middle,last):
     
        print(f"{first.capitalize()} {article.lower()} {middle.capitalize()} {last.capitalize()}")
        
my_plane("being","a","data","analyst")
    


# In[38]:


def times(n1,n2,n3,n4,n5):
    if n5 != 2002:
        print("unclear info")
    else:
        print("100% accurate")
        
times(1984,1986,1993,1996,2002)
    


# In[53]:


def say_hello(*people):
    
    for name in people:
        
        print(f"Hello {name}")
say_hello("mohamed","khadija","safia","dareen","zeinab")
        
        


# In[60]:


def show_details(name,*skills):
    
    print(f"hello mohamed your skills are:")
    
    for skill in skills:
        print(skill)
    
    print(f"{skill1}")
    print(f"{skill2}")
    print(f"{skill3}")
    
show_details("python","dashboards")
    
    


# In[1]:


def my_kids(*kid):
    
    for baby in kid:
        print(kid)
   
my_kids("khadija","safia")


# In[4]:


def my_dreams(*d):
    print("my dream is:")
    
    for ach in d:
        print(ach)
    print(f"{d1}")
    print(f"{d2}")
    print(f"{d3}")
    print(f"{d4}")
my_dreams("being","a","data","analyst","soon")


# In[19]:


def info(name , age , country="unknown"):
    
    print(f"Hello {name.upper()}: your age is {age} years old and your country is {country}")
info("mohamed",33,"egypt")
info('abdelaziz',30,"ksa")
info("abo bakr",39)


# In[2]:


def brand(*w):
    
    
    for word in w:
        print(word)

brand("arabian","oud","perfumes",900,"branches")


# In[25]:


def giza(*city):
    
    print("cities in giza are:")
    
    for new in city:
        
        print(new)
       
giza("badrasheen","ayatt","oseem","boulaq-aldakror","kerdasa")


# In[43]:


def canada(*c):
    
    print("provinces in canda are:")
    
    for prov in c:
        
        print(prov)   
canada("New brunswick","Quebec","Alberta","Ottwa")


# In[45]:


def Qalyobia(*c):
    
    for new in c:
        print(new)
Qalyobia("Banha","Qlyob","Qeha","shobra alkhima")


# In[ ]:




