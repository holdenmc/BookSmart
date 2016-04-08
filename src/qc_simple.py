import sys
import csv
import optparse

# Set 8 as the minimum value at which we consider the original translation good 
min_good = 8

def compute_and_print_best_versions(file) :

	best_translations = {}
	for row in csv.DictReader(open(file)) :	
		if (int(row['rating']) >= min_good) :
			best_translations[row['fileName']] = row['original']
		else :
			best_translations[row['fileName']] = row['updated']

	# Print to file best-translations.txt			
	f1 = open('./best-translations.txt', 'w+')
	for key in best_translations :
		print >> f1, key, '\t', best_translations[key]


if __name__ == '__main__':
	# Based this on the sample script from part 2, but only needed the file name option
	optparser = optparse.OptionParser()
	optparser.add_option("-d", dest="data_file", help="Crowdflower csv file.")
	
	(opts, _) = optparser.parse_args()

	compute_and_print_best_versions(opts.data_file)
	