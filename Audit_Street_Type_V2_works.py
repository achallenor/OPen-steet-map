#!/usr/bin/env python
# coding: utf-8

# In[17]:


#osm_file = open("OSM Chester and Tarporley.xml", "r")


# In[1]:


import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict

FILENAME = "OSM Chester and Tarporley.xml"

st_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


# List of expected street types
expected_st_types = ['Avenue', 'Boulevard', 'Court', 'Place','Square', 'Trail', 'Parkway', 'Commons','Terrace', 'Broadway', 'Center', 'Circle', 'Expressway', 'Way']


# Define the function to audit street type
def audit_st_type(st_types, st_name):
    m = st_type_re.search(st_name)
    if m:
        st_type = m.group()
        if st_type not in expected_st_types:
            st_types[st_type].add(st_name)



# Define the function to audit street names
def audit_st(filename):
    st_types = defaultdict(set)
    for event, elem in ET.iterparse(filename, events=('start',)):
        if elem.tag == "way" or elem.tag == 'node':
            for tag in elem.iter('tag'):
                if tag.attrib['k'] == 'addr:street':
                    audit_st_type(st_types, tag.attrib['v'])
    return st_types

#print the street types in the osm file
st_types = audit_st(FILENAME)
pprint.pprint(dict(st_types))

#mapping dictionary
mapping = {'St': 'Street',
           'St.': 'Street',
           'Ave': 'Avenue',
           'Rd.': 'Road',
           'Trl': 'Trail',
           'Ct': 'Court',
           'Dr': 'Drive',
           'Street': 'Street',
           'Lane': 'Lane',
           'Road': 'Road',
           'Bypass' : 'By-pass',
           'green' : 'Green',
           'lane' : 'Lane'
            }

#function to update the street names.
def update_name(name):
    for old_type in mapping:
        if name.endswith(old_type):
            new_type = mapping[old_type]
            name = name[:(len(name) - len(old_type))] + new_type
    return name

# show the updated street names
for st_type, ways in st_types.items():
    for name in ways:
        better_name = update_name(name)
        if better_name != name:
            print (name, "=>", better_name)


# In[ ]:




