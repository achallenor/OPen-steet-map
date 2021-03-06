#!/usr/bin/env python
# coding: utf-8

# In[1]:


osm_file = open("OSM Chester and Tarporley.xml", "r")


# In[2]:


#!/usr/bin/env python
import xml.etree.ElementTree as ET
import pprint
import re


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    """ 
    Count the criteria in dictionary for the content of the tag.
    """
    if element.tag == "tag":
        if lower.search(element.attrib['k']):
            keys['lower'] +=1
        elif lower_colon.search(element.attrib['k']):
            keys['lower_colon']+=1
        elif problemchars.search(element.attrib['k']):
            keys['problemchars']+=1
        else:
            keys['other']+=1
        
    return keys


#shows the number of entries for each type of data
def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertions will be incorrect then.
    keys = process_map(osm_file)
    pprint.pprint(keys)
#     assert keys == {'lower': 5, 'lower_colon': 0, 'other': 2, 'problemchars': 0}


if __name__ == "__main__":
    test()


# In[ ]:




