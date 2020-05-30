#!/usr/bin/env python
# coding: utf-8

# In[2]:


osm_file = open("OSM Chester and Tarporley.xml", "r")


# In[3]:


# %%writefile mapparser.py
#!/usr/bin/env python
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    """count tags in filename.
    
    Init 1 in dict if the key not exist, increment otherwise."""
    tags = {}
    for ev,elem in ET.iterparse(filename):
        tag = elem.tag
        if tag not in tags.keys():
            tags[tag] = 1
        else:
            tags[tag]+=1
    return tags

def test():

    tags = count_tags(osm_file)
    pprint.pprint(tags)

if __name__ == "__main__":
    test()


# In[ ]:




