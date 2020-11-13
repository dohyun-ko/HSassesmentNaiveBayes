
# coding: utf-8

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# 
# cred = credentials.Certificate('naivebayse-firebase-adminsdk-000gp-b8b078b25c.json')
# firebase_admin.initialize_app(cred,{'databaseURL' : 'https://naivebayse.firebaseio.com/'})

# In[1]:


oorx = [[1, -1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, -1, 1],
        [1, 1, 0, 0, 1],
        [1, -1, 1, -1, 1]
        ]
#correct = 1, wrong = 0, null = -1


# In[ ]:


def newQst():
    for i in range(0, len(oorx)):
        oorx[i].append(-1)


# In[ ]:


def solveQst(usr,qstA, answer):
    oorx[usr][qstA] = answer


# In[2]:


def probofQst(qstA):
    #P(qstA)
    numofUsr = 0
    numofO = 0
    
    for i in range(0, len(oorx)):
        if(oorx[i][qstA] != -1):
            numofUsr += 1
            if(oorx[i][qstA] == 1):
                numofO += 1

    return numofO / numofUsr


# In[3]:


def probofQstAB(qstA, qstB, boolofqstB):
    #P(qstB|qstA)
    numofUsr = 0
    numofSame = 0
    
    for i in range(0, len(oorx)):
        if(oorx[i][qstA] == 1):
            numofUsr += 1
            if(oorx[i][qstB] == boolofqstB):
                numofSame += 1
    return numofSame / numofUsr


# In[4]:


def probbyNaive(usr, qstA):
    #
    value = probofQst(qstA)
    
    for i in range(0, len(oorx[usr])):
        if(oorx[usr][i] != -1):
            value *= probofQstAB(qstA, i, oorx[usr][i])

    return value


# In[5]:


def recommend(usr):
    
    proper = -1
    properP = 1
    
    for i in range(0, len(oorx[usr])):
        if(oorx[usr][i] == -1):
            temp = probbyNaive(usr, i)
            if(temp < properP):
                proper = i
                properP = temp
    
    return proper


# In[6]:


user = int(input())


# In[7]:


print(recommend(user))

