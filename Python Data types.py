#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Do functions have a data type? 
def test():
    return print('testing')


# In[2]:


test()


# In[4]:


type(test())


# In[7]:


#Examples of the Integer Data type.
print("The following data types:")
print(type(2))

#int values can be very long.
print(type(648165234234234234363466184))

#int values can be assigned to variables
var = 5489
print(type(var))


# In[8]:


#Examples of the Float Data type.
print(type(2.58))

#float values can use e for scientific notation.
var_float = 578.34e10
print(type(var_float))


# In[15]:


#Examples of the complex Data type.
print(type(4j))

#float values can also be used in complex numeric data types
var_complex = 45 + 5.5j
print(type(var_complex))


# In[17]:


#Examples of Boolean data type. Boolean is either True or False.
print(type(True))
print(type(False))

#Boolean data type can return when evaluating an expression too.
var_bool = 4==4
print(type(var_bool))

var2_bool = 4==5
print(type(var2_bool))


# In[24]:


#Example of string (str) data types. 
print(type('single quotes'))
print(type("double quotes"))
print(type('''triple quotes'''))

#We can access a particular position in the string by calling its index value.
string = 'CareerFoundry.com rocks!'

#this will return the 3rd character in a string.
print(string[2])

#A range of values can be returned.
print(string[0:6])

#Negative numbers can be used to return the end of the string first. 
#-1 would return the last character in the string
print(string[-1])

#You can even print a string in reverse!
print(string[::-1])


# In[26]:


#Example of Python data type list
print(type([1,3,'g', 5, 'z']))

#you can have lists within lists!
print(type(['a', 'b', 3, [123, 9, 2], 'y']))


# In[33]:


#lists have indexes
var_list = ['a', 'b', 3, [123, 9, 2], 'y']
print(var_list[0])

#The sublist index can be accessed with an additional []
print(var_list[3][1])


# In[34]:


#Example of Python data type tuple
print(type((1,3,'g', 5, 'z')))

#you can have tuples within tuples!
print(type(('a', 'b', 3, (123, 9, 2), 'y')))


# In[36]:


#Example of Python data type set
var_set_list = [1,1,2,3,4,4,5,'a','a','b','c']
var_set = set(var_set_list)

print(type(var_set))
print(var_set)


# In[38]:


#Example of Python data type dictionary
var_dictionary = {'person1':'Eric', 'person2':'Kristen'}

print(type(var_dictionary))
print(var_dictionary)


# In[44]:


print(var_dictionary.keys())
print(var_dictionary.values())
print(var_dictionary['person1'])
print(var_dictionary['person2'])


# In[ ]:




