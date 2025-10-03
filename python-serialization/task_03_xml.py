#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    my_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for x in root:
        child = x.tag
        my_dict[x.tag] = x.text
    return my_dict
