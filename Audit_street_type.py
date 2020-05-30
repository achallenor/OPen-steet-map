#!/usr/bin/env python
# coding: utf-8

# In[12]:


osm_file = open("OSM Chester and Tarporley.xml", "r")


# In[13]:



import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

#OSMFILE = "example.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]


mapping = { "St": "Street",
            "St.": "Street",
            "Ave" :"Avenue",
            "St.": "Street",
            "Rd." : "Road",
            "N.":"North",
            "E." : "East",
            "S." : "South",
            "W." : "West"
        
            }

#look to see if street type is in the expected variable list. If not display later in scrip.
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

#get data from above function
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    #osm_file = open(osm_file, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

#use mapping variable to update abreviations
def update_name(name, mapping):
    dict_map = sorted(mapping.keys(), key=len,)
    for key in dict_map:

            if name.find(key):          
                name = name.replace(key,mapping[key])
                return name


    return name


def test():
    st_types = audit(osm_file)
    #assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()


# In[ ]:




