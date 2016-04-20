import argparse
import csv
#import os
parser = argparse.ArgumentParser(description='Process arguments. Fetch source file, Destination folder, column names')
parser.add_argument('--src',help='give fully classified path of source file')
parser.add_argument('--des',help='give destination folder')
parser.add_argument('--col',help='specifiy col name Note: first id column name, second symptom column name')
args = parser.parse_args()


DESIRED_COLUMNS = ('vaers_id','symptom_text')

#f = open(args.src)
f = open("Y:\SJSU_Studies\Sem5_CS298\Project_data\Autism\Yearwise_Data_Autism\Autism_2014.csv")
reader = csv.reader(f)

headers = None
results = []
for row in reader:
    if not headers:
        headers = []
        for i, col in enumerate(row):
        	if col in DESIRED_COLUMNS:
            		# Store the index of the cols of interest
            		headers.append(i)

    else:
        results.append(tuple([row[i] for i in headers]))

count = 0

for r in results:
	print r
#	print "--------------------------------"
	
#	print "id-> ",r[0]," symptoms-> ",r[1],"\n" 
	count = count + 1 
	#fname = "neg"+r[0]+".txt"
	#print "fname:",fname
	#filename = os.path.join("Y:\","SJSU_Studies","Sem5_CS298","Project_data","Text_files2","Neg","Autism1991")
	#print filename
	filename = "Y:\SJSU_Studies\Sem5_CS298\Project_data\Text_files2\Pos\Autism2014\pos"+r[0]+".txt"
	f1 = open(filename,"wb")
 	f1.write(r[1])
	f1.close()
f.close()	
		

