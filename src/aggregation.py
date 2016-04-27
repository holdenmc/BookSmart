import sys
import csv
import optparse


def compute_and_print_best_versions(file, filename) :

	best_translations = {}
	for row in csv.DictReader(open(file)) :	
		#Filter by URL
		if row['url'] not in best_translations :
			# Each entry in best_translations is tied to a url as a key
			# And then contains the following fields
			# count : The # of rows related to this URL read in so far
			# translation1, translation2, translation3 : The strings of the three translations done on that HIT
			# rawTotal1, rawTotal2, rawTotal3 : The sum of ratings (unweighted) for the first, second and third translation
			# weightedTotal1, 2, 3: The sum of ratings (weighted by workers' _trust) for the first, second and third translation
			# realCount1, 2, 3: The count of actual ratings (not counting those who marked 'no text in picture') for the
			# 		first, second and third translation

			# We later compute averages for each of the three translations as rawTotal/realCount and weightedTotal/realCount
			best_translations[row['url']] = {'count' : 0, 'translation1' : '', 'translation2' : '',
				'translation3' : '', 'rawTotal1' : 0.0, 'rawTotal2' : 0.0, 'rawTotal3' : 0.0,
				'weightedTotal1' : 0.0, 'weightedTotal2' : 0.0, 'weightedTotal3' : 0.0,
				'realCount1' : 0.0, 'realCount2' : 0.0, 'realCount3' : 0.0}
		

		# Start by incrementing the count
		best_translations[row['url']]['count'] += 1

		# Store the current count as a local variable
		count = best_translations[row['url']]['count']

		# For each range of counts modify that translation
		# 1-5 -> translation1
		# 6-10 -> translation2
		# 11-15 -> translation3
		if count >= 1 and count <= 5 :
			# If we don't have a translation stored in best_translations, add it
			if best_translations[row['url']]['translation1'] == '' :
				best_translations[row['url']]['translation1'] = row['translate_the_text_in_the_photo_as_accurately_as_possible']

			# If the worker thinks there is text and they put in a rating ...
			if row['check_this_box_if_there_is_text_in_the_photo'] and row['rate_the_grammarspelling_of_the_translation'] is not '':
				# Update rawTotal by adding the normal value
				best_translations[row['url']]['rawTotal1'] += int(row['rate_the_grammarspelling_of_the_translation'])
				# Update the weightedTotal by adding the normal value multiplied by the worker's trust value
				best_translations[row['url']]['weightedTotal1'] += (float(row['rate_the_grammarspelling_of_the_translation']) * float(row['_trust']))
				# We had a real rating, so incrememnt realCount
				best_translations[row['url']]['realCount1'] += 1

		elif count >= 6 and count <= 10 :
			if best_translations[row['url']]['translation2'] == '' :
				best_translations[row['url']]['translation2'] = row['translate_the_text_in_the_photo_as_accurately_as_possible']

			# Do weighting based on trust
			if row['check_this_box_if_there_is_text_in_the_photo'] and row['rate_the_grammarspelling_of_the_translation'] is not '' :
				best_translations[row['url']]['rawTotal2'] += int(row['rate_the_grammarspelling_of_the_translation'])
				best_translations[row['url']]['weightedTotal2'] += (float(row['rate_the_grammarspelling_of_the_translation']) * float(row['_trust']))
				best_translations[row['url']]['realCount2'] += 1

		elif count >= 11 and count <= 15 :
			if best_translations[row['url']]['translation3'] == '' :
				best_translations[row['url']]['translation3'] = row['translate_the_text_in_the_photo_as_accurately_as_possible']

			# Do weighting based on trust
			if row['check_this_box_if_there_is_text_in_the_photo'] and row['rate_the_grammarspelling_of_the_translation'] is not '' :
				best_translations[row['url']]['rawTotal3'] += int(row['rate_the_grammarspelling_of_the_translation'])
				best_translations[row['url']]['weightedTotal3'] += (float(row['rate_the_grammarspelling_of_the_translation']) * float(row['_trust']))
				best_translations[row['url']]['realCount3'] += 1

	# Print to file best-translations.txt			
	f1 = open('./' + filename + '-raw.txt', 'w+')
	f2 = open('./' + filename + '-weighted.txt', 'w+')
	for key in best_translations :
		# If the first translation received any ratings, compute the averages
		if best_translations[key]['realCount1'] > 0 :
			rawAvg1 = float((best_translations[key]['rawTotal1'] / best_translations[key]['realCount1']))
			weightedAvg1 = float((best_translations[key]['weightedTotal1'] / best_translations[key]['realCount1']))
		else :
			# If the first translation didn't receive any ratings, set averages to zero
			rawAvg1 = 0
			weightedAvg1 = 0
		#Same as code block above
		if best_translations[key]['realCount2'] > 0 :
			rawAvg2 = float((best_translations[key]['rawTotal2'] / best_translations[key]['realCount2']))
			weightedAvg2 = float((best_translations[key]['weightedTotal2'] / best_translations[key]['realCount2']))
		else :
			rawAvg2 = 0
			weightedAvg2 = 0

		#Same as code block above
		if best_translations[key]['realCount3'] > 0 :
			rawAvg3 = float((best_translations[key]['rawTotal3'] / best_translations[key]['realCount3']))
			weightedAvg3 = float((best_translations[key]['weightedTotal3'] / best_translations[key]['realCount3']))
		else :
			rawAvg3 = 0
			weightedAvg3 = 0

		# Determine which of the rawAverages is teh highest and store it in maxRaw
		maxRaw = rawAvg1

		if rawAvg2 > maxRaw :
			maxRaw = rawAvg2

		if rawAvg3 > maxRaw :
			maxRaw = rawAvg3

		# Print out the translation tied to that highest average rating
		if maxRaw == rawAvg1 :
			print >> f1, key, '\t', best_translations[key]['translation1']
		elif maxRaw == rawAvg2 :
			print >> f1, key, '\t', best_translations[key]['translation2']
		elif maxRaw == rawAvg3 :
			print >> f1, key, '\t', best_translations[key]['translation3']

		# See code block above regarding maxRaw, this is the same
		maxWeighted = weightedAvg1

		if weightedAvg2 > maxWeighted :
			maxWeighted = weightedAvg2

		if weightedAvg3 > maxWeighted :
			maxWeighted = 3

		if maxWeighted == weightedAvg1 :
			print >> f2, key, '\t', best_translations[key]['translation1']
		elif maxWeighted == weightedAvg2 :
			print >> f2, key, '\t', best_translations[key]['translation2']
		elif maxWeighted == weightedAvg3 :
			print >> f2, key, '\t', best_translations[key]['translation3']


if __name__ == '__main__':
	# Based this on the sample script from part 2, but only needed the file name option
	optparser = optparse.OptionParser()
	optparser.add_option("-d", dest="data_file", help="Crowdflower csv file.")
	optparser.add_option("-o", dest="output_file", help="File name, no extension")
	
	(opts, _) = optparser.parse_args()

	compute_and_print_best_versions(opts.data_file, opts.output_file)
	
