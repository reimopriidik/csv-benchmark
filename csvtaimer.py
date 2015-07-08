#!/usr/bin/env python

from os import chdir
import csv
import timeit
import json
from numpy import genfromtxt, loadtxt
from pandas import read_csv, read_table

chdir('/home/r/python') 	#Teistes arvutistes tuleb siit kausta asukohta muuta
							#V6i see funktsioon p2ris eemaldada ja .py koos .csv failiga samasse kasuta asetada
inputFile = ('rand100000,7.csv')	#Siia kirjuta faili nimi

"""
Faili avamine
"""
#csv.reader
result_csvreader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		csv.reader(csvfile)
	end = timeit.default_timer()
	result_csvreader.append(round((end - start), 7)) #Listi asetamine ja Umardamine

#Listi v2ljutamine .json failina
with open('avamine_ajad.json', 'w') as outfile:
	json.dump(result_csvreader, outfile)


#csv.DictReader
result_csvDictReader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		csv.DictReader(csvfile)
	end = timeit.default_timer()
	result_csvDictReader.append(round((end - start), 7))

with open('avamine_ajad.json', 'a') as outfile:
	json.dump(result_csvDictReader, outfile)

#numpy.genfromtxt
result_numpygenfromtxt = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		genfromtxt(csvfile, dtype = str)
	end = timeit.default_timer()
	result_numpygenfromtxt.append(round((end - start), 7))

with open('avamine_ajad.json', 'a') as outfile:
	json.dump(result_numpygenfromtxt, outfile)

#numpy.loadtxt
result_numpyloadtxt = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		loadtxt(csvfile, dtype = str)
	end = timeit.default_timer()
	result_numpyloadtxt.append(round((end - start), 7))

with open('avamine_ajad.json', 'a') as outfile:
	json.dump(result_numpyloadtxt, outfile)

#pandas.read_csv
result_pandasreadcsv = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		read_csv(csvfile, delimiter=(','))
	end = timeit.default_timer()
	result_pandasreadcsv.append(round((end - start), 7))

with open('avamine_ajad.json', 'a') as outfile:
	json.dump(result_pandasreadcsv, outfile)

#pandas.read_table
result_pandasreadtable = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		read_table(csvfile, delimiter=(','))
	end = timeit.default_timer()
	result_pandasreadtable.append(round((end - start), 7))

with open('avamine_ajad.json', 'a') as outfile:
	json.dump(result_pandasreadtable, outfile)

"""
Loopimine
"""
#csv.reader
result_csvreaderloop = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		for row in csv.reader(csvfile):
			pass
	end = timeit.default_timer()
	result_csvreaderloop.append(round((end - start), 7))

with open('loopimine_ajad.json', 'w') as outfile:
	json.dump(result_csvreaderloop, outfile)

#csv.DictReader
result_csvDictReaderloop = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		for row in csv.DictReader(csvfile):
			pass
	end = timeit.default_timer()
	result_csvDictReaderloop.append(round((end - start), 7))

with open('loopimine_ajad.json', 'a') as outfile:
	json.dump(result_csvDictReaderloop, outfile)

#numpy.genfromtxt
result_numpygenfromtxtloop = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		for row in genfromtxt(csvfile, dtype = str):
			pass
	end = timeit.default_timer()
	result_numpygenfromtxtloop.append(round((end - start), 7))

with open('loopimine_ajad.json', 'a') as outfile:
	json.dump(result_numpygenfromtxtloop, outfile)

#numpy.loadtxt
result_numpyloadtxtloop = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		for row in loadtxt(csvfile, dtype = str):
			pass
	end = timeit.default_timer()
	result_numpyloadtxtloop.append(round((end - start), 7))

with open('loopimine_ajad.json', 'a') as outfile:
	json.dump(result_numpyloadtxtloop, outfile)

"""
Headeri otsimine
"""
#csv.reader
result_csvreaderheader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		r1=(csv.reader(csvfile))
		r1.next()
		pass
	end = timeit.default_timer()
	result_csvreaderheader.append(round((end - start), 7))

with open('header_ajad.json', 'w') as outfile:
	json.dump(result_csvreaderheader, outfile)

#csv.DictReader
result_csvDictReaderheader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		r2=csv.DictReader(csvfile)
		r2.next()
		pass
	end = timeit.default_timer()
	result_csvDictReaderheader.append(round((end - start), 7))

with open('header_ajad.json', 'a') as outfile:
	json.dump(result_csvDictReaderheader, outfile)

#numpy.genfromtxt
result_numpygenfromtxtheader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		genfromtxt(csvfile, dtype = str)['0']
		pass
	end = timeit.default_timer()
	result_numpygenfromtxtheader.append(round((end - start), 7))

with open('header_ajad.json', 'a') as outfile:
	json.dump(result_numpygenfromtxtheader, outfile)

#numpy.loadtxt
result_numpyloadtxtheader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		loadtxt(csvfile, dtype = str)['0']
		pass
	end = timeit.default_timer()
	result_numpyloadtxtheader.append(round((end - start), 7))

with open('header_ajad.json', 'a') as outfile:
	json.dump(result_numpyloadtxtheader, outfile)

#pandas.read_csv
result_pandasreadcsvheader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		l1 = read_csv(csvfile, delimiter=(','), header=0)
		list(l1.columns.values)
		pass
	end = timeit.default_timer()
	result_pandasreadcsvheader.append(round((end - start), 7))

with open('header_ajad.json', 'a') as outfile:
	json.dump(result_pandasreadcsvheader, outfile)

#pandas.read_table
result_pandasreadtableheader = []
for _ in range(100):
	start = timeit.default_timer()
	with open(inputFile, 'r') as csvfile:
		l2 = read_table(csvfile, delimiter=(','), header=0)
		list(l2.columns.values)
		pass
	end = timeit.default_timer()
	result_pandasreadtableheader.append(round((end - start), 7))

with open('header_ajad.json', 'a') as outfile:
	json.dump(result_pandasreadtableheader, outfile)