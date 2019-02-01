#!/usr/bin/env python
#coding: utf8
import os
import sys
import subprocess

def genJpg(path):
	newroot = []
	ext = ".jpg"
	p,filename_ext = os.path.split(path)
	filename,ext_t = os.path.splitext(filename_ext)
	proxyDir = "/tmp/proxy/" +p
	if not os.path.exists(proxyDir):
		os.makedirs(proxyDir)

	target = p + "/" + filename+ext_t
	result = proxyDir + "/" + filename + ext
	newroot.append(result)
	cmd  = "convert {target} {result}".format(target = target, result = result)
	os.system(cmd)
	print newroot


def genMov(path):
	ext = ".mov"
	p,filename_ext = os.path.split(path)
	filename,ext_t = os.path.splitext(filename_ext)
	proxyDir = "/tmp/results/" +p
	if not os.path.exists(resultDir):
		os.makedirs(resultDir)
	target = p + "/" + filename+ext_t
	result = resultDir + "/" + filename + ext







def searchItem(root):
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root +"/"+subdir):
			shot.append("/".join([root,subdir,f]))			
		shot.sort()	
		seqs.append(shot)
	return seqs

def searchExt(rootpath):
	results = []
	for root, dirs, files in os.walk(rootpath, topdown = True):
		if root == rootpath:
			continue
		if dirs:
			result.append("/".join([root]+dirs+[f]))
		else:
			results.append("/".join([root,f]))
	return results
			



def countFile(results):
	snum = []
	for i in results:
		flist = i.split(".")
		snum.append(flist[1])
		snum.sort()
		howmany = int(snum[-1]) -int(snum[0]) + 1
	return howmany



if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	seqs = searchItem(root)
	for i in seqs:
		for j in i:
			genJpg(j)
		print countFile(i)



