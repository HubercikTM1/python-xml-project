#metoda ElementTree

import xml.etree.ElementTree as ET

tree = ET.parse('xmlproject.xml')
root = tree.getroot()

print(ET.tostring(root))
