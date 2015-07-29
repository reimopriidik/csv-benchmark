#!/usr/bin/env python

#from os import chdir
import csv
import timeit
import json
from numpy import genfromtxt, loadtxt
from pandas import read_csv, read_table

#chdir('/home/r/python')
inputFile = ('rand100,5.csv')

def avamistaimer(avamisviis, alh):
	result=[]
	for _ in range(99):
		start=timeit.default_timer()
		if alh=='ava':
			avamisf(avamisviis)
		elif alh=='loop':
			loopf(avamisviis)
		elif alh=='header':
			headerf(avamisviis)
		end=timeit.default_timer()
		result.append(round((end - start), 7))
	open(inputFile,'r').close()
	kirj(alh, result)

def kirj(alh, result):
	if alh=='ava':
		with open('avamine_ajad.json', 'a') as outfile:
			json.dump(result, outfile)
	elif alh=='loop':
		with open('loop_ajad.json', 'a') as outfile:
			json.dump(result, outfile)
	elif alh=='header':
		with open('header_ajad.json', 'a') as outfile:
			json.dump(result, outfile)

def avamisf(avamisviis):
	if avamisviis==csv.reader or avamisviis==csv.DictReader:
		with open(inputFile,'r') as csvfile:
			avamisviis(csvfile);pass
	elif avamisviis==genfromtxt or avamisviis==loadtxt:
		with open(inputFile, 'r') as csvfile:
			avamisviis(csvfile, dtype = str)
	elif avamisviis==read_csv or avamisviis==read_table:
		with open(inputFile, 'r') as csvfile:
			avamisviis(csvfile, index_col=False, header=0);pass

def loopf(avamisviis):
	if avamisviis==csv.reader or avamisviis==csv.DictReader:
		with open(inputFile, 'r') as csvfile:
			for row in avamisviis(csvfile):
				pass
	elif avamisviis==genfromtxt or avamisviis==loadtxt:
		with open(inputFile, 'r') as csvfile:
			for row in avamisviis(csvfile, dtype = str):
				pass

def headerf(avamisviis):
	if avamisviis==csv.reader or avamisviis==csv.DictReader:
		with open(inputFile, 'r') as csvfile:
			r1=(avamisviis(csvfile))
			r1.next()
			pass
	elif avamisviis==genfromtxt or avamisviis==loadtxt:
		with open(inputFile, 'r') as csvfile:
			avamisviis(csvfile, dtype = str)['0']
			pass
	elif avamisviis==read_csv or avamisviis==read_table:
		with open(inputFile, 'r') as csvfile:
			l1 = read_csv(csvfile, delimiter=(','), header=0)
			list(l1.columns.values)
			pass

avamistaimer(avamisviis=csv.reader, alh='ava')
avamistaimer(avamisviis=csv.DictReader, alh='ava')
avamistaimer(avamisviis=genfromtxt, alh='ava')
avamistaimer(avamisviis=loadtxt, alh='ava')
avamistaimer(avamisviis=read_csv, alh='ava')
avamistaimer(avamisviis=read_table, alh='ava')

avamistaimer(avamisviis=csv.reader, alh='loop')
avamistaimer(avamisviis=csv.DictReader, alh='loop')
avamistaimer(avamisviis=genfromtxt, alh='loop')
avamistaimer(avamisviis=loadtxt,alh='loop')

avamistaimer(avamisviis=csv.reader, alh='header')
avamistaimer(avamisviis=csv.DictReader, alh='header')
avamistaimer(avamisviis=genfromtxt, alh='header')
avamistaimer(avamisviis=loadtxt, alh='header')
avamistaimer(avamisviis=read_csv, alh='header')
avamistaimer(avamisviis=read_table, alh='header')
