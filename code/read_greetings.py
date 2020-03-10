import os
from xml.etree import ElementTree

file_name = 'greetings.xml'
full_file = os.path.abspath(file_name)

# Parse the greetings.xml file
dom = ElementTree.parse(full_file)

# Find all the greeting tag
for i in dom.findall('{openstax.org}greeting'):
    # Get prefix's text and target's text in the greeting tag,
    # split by empty space, because we want to make each word
    # capitalized
    prefix = i.find('{openstax.org}prefix').text.split(" ")
    target = i.find('{openstax.org}target').text.split(" ")

    # Make every word in prefix in title case,
    # then turn the list back to a string
    prefix = [p.capitalize() for p in prefix]
    prefix = " ".join(prefix)

    # Make every word in target in title case,
    # then turn the list back to a string
    target = [t.capitalize() for t in target]
    target = " ".join(target)

    # Print the result, put a comma after prefix
    # an exclamation point at the end.
    print(prefix + ", " + target + "!")


