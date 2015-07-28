#!/usr/bin/env python

#from os import chdir
import csv
import timeit
import json
from numpy import genfromtxt, loadtxt
from pandas import read_csv, read_table

#chdir('/home/r/python')
inputFile = ('rand100,5.csv')

def avamistaimer(a, e):
	result=[]
	f=open(inputFile,'r')
	for _ in range(99):
		start=timeit.default_timer()
		if e=='ava':
			avamisf(a)
		elif e=='loop':
			loopf(a)
		elif e=='header':
			headerf(a)
		end=timeit.default_timer()
		result.append(round((end - start), 7))
	f.close()
	kirj(e, result)

def kirj(e, result):
	if e=='ava':
		with open('avamine_ajad.json', 'a') as outfile:
			json.dump(result, outfile)
	elif e=='loop':
		with open('loop_ajad.json', 'a') as outfile:
			json.dump(result, outfile)
	elif e=='header':
		with open('header_ajad.json', 'a') as outfile:
			json.dump(result, outfile)

def avamisf(a):
	if a==csv.reader or a==csv.DictReader:
		with open(inputFile,'r') as csvfile:
			a(csvfile);pass
	elif a==genfromtxt or a==loadtxt:
		with open(inputFile, 'r') as csvfile:
			a(csvfile, dtype = str)
	elif a==read_csv or a==read_table:
		with open(inputFile, 'r') as csvfile:
			a(csvfile, index_col=False, header=0);pass

def loopf(a):
	if a==csv.reader or a==csv.DictReader:
		with open(inputFile, 'r') as csvfile:
			for row in a(csvfile):
				pass
	elif a==genfromtxt or a==loadtxt:
		with open(inputFile, 'r') as csvfile:
			for row in a(csvfile, dtype = str):
				pass

def headerf(a):
	if a==csv.reader or a==csv.DictReader:
		with open(inputFile, 'r') as csvfile:
			r1=(a(csvfile))
			r1.next()
			pass
	elif a==genfromtxt or a==loadtxt:
		with open(inputFile, 'r') as csvfile:
			a(csvfile, dtype = str)['0']
			pass
	elif a==read_csv or a==read_table:
		with open(inputFile, 'r') as csvfile:
			l1 = read_csv(csvfile, delimiter=(','), header=0)
			list(l1.columns.values)
			pass

avamistaimer(a=csv.reader, e='ava')
avamistaimer(a=csv.DictReader, e='ava')
avamistaimer(a=genfromtxt, e='ava')
avamistaimer(a=loadtxt, e='ava')
avamistaimer(a=read_csv, e='ava')
avamistaimer(a=read_table, e='ava')

avamistaimer(a=csv.reader, e='loop')
avamistaimer(a=csv.DictReader, e='loop')
avamistaimer(a=genfromtxt, e='loop')
avamistaimer(a=loadtxt,e='loop')

avamistaimer(a=csv.reader, e='header')
avamistaimer(a=csv.DictReader, e='header')
avamistaimer(a=genfromtxt, e='header')
avamistaimer(a=loadtxt, e='header')
avamistaimer(a=read_csv, e='header')
avamistaimer(a=read_table, e='header')
