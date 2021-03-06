#!/usr/bin/env python
# coding: utf-8

# In[1]:


osm_file = open("OSM Chester and Tarporley.xml", "r")


# In[3]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re

def get_user(element):
    return


def process_map(filename):
    """
    Count the user id in the filename.
    """
    users = set()
    for _, element in ET.iterparse(filename):
        try:
            users.add(element.attrib['uid'])
        except KeyError:
            continue

    return users


def test():

    users = process_map(osm_file)
    pprint.pprint(users)
#     assert len(users) == 6



if __name__ == "__main__":
    test()


# In[ ]:




