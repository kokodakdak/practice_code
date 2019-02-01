#!/usr/bin/env python
#coding: utf8
import os
import sys
import subprocess

def genJpg(src):
	"""	
	경로를 입력받으면 exr파일을 jpg파일로 변환한다.
	"""
	if not os.path.exists(src):
		return "", "파일이 존재하지 않습니다."
	if not os.path.isfile(src):
		return "","파일형태가 아닙니다."
	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick가 설치되지 않았습니다."
	

	for i in os.listdir(src):
		d, f = os.path.split(src)
		notuse, ext = os.path.splitext(f)
		dst = d+"/"+f.replace(ext,".jpg")
		cmds = ["convert",src,dst]
		p = subprocess.Popen(cmds, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
		return p.communicate()
		
		os.system(cmd)

def genMov(src):
	"""
	앞에서 변환한 파일로 Mov파일을 만든다.
	"""
	lf = os.listdir(src)
	lf.sort()
	fnum = lf[0].split(".") - lf[-1].split(".")

	if not os.path.exists("/home/$USER/app/ffmpeg"):
		return "", "ffmpeg가 설치되지 않았습니다."

	for i in os.listdir(src):
		p, fn = os.path.split(src)
		filename, ext = os.path.splitext(fn)
		if ext == "jpg":

cmds = ["-f image2 -start_number" ,filenumber, "-r 24 -i", src, "%",num,"d",

		

def searchItem(root):
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root +"/"+subdir):
			results.append("/".join([root,subdir,f]))			
		shot.sort()	
		seqs.append(shot)
	return seqs


def searchExt(rootpath):
	result = []
	for root, dirs, files in os.walk(rootpath, topdown = True):
		if root == rootpath:
			continue
		if dirs:
			result.append("/".join([root] + dirs + [f]))
		else:
			results.append("/".join([root,f]))
	return results
	
	


def countFile(results):
	snum = []
	for  i in results:
		flist = i.split(".")
		snum.append(flist[1])
		snum.sort()
		howmany = int(snum[-1]) - int(snum[0]) + 1
	return howmany




if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	seqs = searchItem(root)
	for i in seqs:
		print countFile(i)


