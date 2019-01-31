#!/usr/bin/env python
#coding: utf8
import os
import sys
import subprocess

def genThumb(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick이 설치되지 않았습니다."

	d, f = os.path.split(src)
	notuse, ext = os.path.splitext(f)
	dst = d+"/"+f.replace(ext,".jpg")
	size = "360x240"
#	cmd = "convert {src} -thumbnail {size} -background black -grvity center -extent {size}{dst}".format(src = src,dst = dst,size = "360x240")
	cmds = ["convert",src,"-thumbnail",size, "-background","black","-gravity","center","-extent",size,dst]
	p = subprocess.Popen(cmds, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	return p.communicate()

	os.system(cmd)

if __name__ =="__main__":
	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0h.78727.exr"
	stdOut, stdErr = genThumb(src)
	if stdErr:
		sys.stderr.write(stdErr)
	sys.stdout.write(stdOut)
	genThumb(filepath)






#	size = "360x240"
#	change_ext = "jpg"
#	filename_with_ext = os.path.basename(filepath)
#	filename, first_ext = os.path.splitext(filename_with_ext)

#	for i in os.listdir(filepath):
#		for j in os.listdir(filepath+"/"+i):
#			for k in os.listdir(filepath+"/"+i+"/"+j):
#				target = "/".join([filepath,i,j,k])
#				result = "/".join([filepath,i,j,k.replace(".dpx",".jpg").replace(".exr",".jpg")])
#				cmd = "convert %s -thumbnail %s -background black -gravity center -extent %s %s" % (filename_with_ext,size, size, result.replace(first_ext,change_ext))



#filepath = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.exr"

#p= "/project/circle/in"

#for i in os.listdir(p):
#	for j in os.listdir(p+"/"+i):
#		for k in os.listdir(p+"/"+i+"/"+j):
#			target = "/".join([p,i,j,k])
#			result = "/".join([p,i,j,k.replace(".dpx",".jpg").replace(".exr",".jpg")])
#			cmd = "convert %s -thumbnail 360x240 -background black -gravity center -extent 360x240 %s" % (target, result)
#			print target
#			print result
#			print cmd
