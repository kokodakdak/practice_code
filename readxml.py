#!/usr/bin/env python
import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("test.xml")

for e in root.findall("shots"):
	for sube in e.findall("item"):
		print sube.findtext("name")
