import sys
import csv
import optparse


def compute_and_print_best_versions(file) :

	best_translations = {}
	for row in csv.DictReader(open(file)) :	
		#Filter by URL
		if row['url'] not in best_translations :
			best_translations[row['url']] = {'count' : 0, 'translation1' : '', 'translation2' : '',
				'translation3' : '', 'rawTotal1' : 0.0, 'rawTotal2' : 0.0, 'rawTotal3' : 0.0,
				'weightedTotal1' : 0.0, 'weightedTotal2' : 0.0, 'weightedTotal3' : 0.0,
				'realCount1' : 0.0, 'realCount2' : 0.0, 'realCount3' : 0.0}
		

		best_translations[row['url']]['count'] += 1

		count = best_translations[row['url']]['count']

		if count >= 1 and count <= 5 :
			if best_translations[row['url']]['translation1'] == '' :
				best_translations[row['url']]['translation1'] = row['translate_the_text_in_the_photo_as_accurately_as_possible']

			# Do weighting based on trust
			if row['check_this_box_if_there_is_text_in_the_photo'] and row['rate_the_grammarspelling_of_the_translation'] is not '':
				best_translations[row['url']]['rawTotal1'] += int(row['rate_the_grammarspelling_of_the_translation'])
				best_translations[row['url']]['weightedTotal1'] += (float(row['rate_the_grammarspelling_of_the_translation']) * float(row['_trust']))
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
	avgEverything = 0;
	avgBest = 0;
	base_li = []
	best_base_li = []
	avgEverythingWeighted = 0;
	avgBestWeighted = 0;
	weighted_li = []
	best_weighted_li = []
	for key in best_translations :
		if best_translations[key]['realCount1'] > 0 :
			rawAvg1 = float((best_translations[key]['rawTotal1'] / best_translations[key]['realCount1']))
			weightedAvg1 = float((best_translations[key]['weightedTotal1'] / best_translations[key]['realCount1']))
		else :
			rawAvg1 = 0
			weightedAvg1 = 0

		if best_translations[key]['realCount2'] > 0 :
			rawAvg2 = float((best_translations[key]['rawTotal2'] / best_translations[key]['realCount2']))
			weightedAvg2 = float((best_translations[key]['weightedTotal2'] / best_translations[key]['realCount2']))
		else :
			rawAvg2 = 0
			weightedAvg2 = 0

		if best_translations[key]['realCount3'] > 0 :
			rawAvg3 = float((best_translations[key]['rawTotal3'] / best_translations[key]['realCount3']))
			weightedAvg3 = float((best_translations[key]['weightedTotal3'] / best_translations[key]['realCount3']))
		else :
			rawAvg3 = 0
			weightedAvg3 = 0

		li1 = [rawAvg1, rawAvg2, rawAvg3]

		for i in li1:
			if i > 1:
				base_li.append(i)
		if max(li1) > 1:
			best_base_li.append(max(li1))


		li2 = [weightedAvg1, weightedAvg2, weightedAvg3]
		for i in li2:
			if i > 1:
				weighted_li.append(i)
		if max(li2) > 1:
			best_weighted_li.append(max(li2))
	print file
	print "all non weighted " + str(sum(base_li)/len(base_li))
	print "best non weighted " + str(sum(best_base_li)/len(best_base_li))
	print "all weighted " + str(sum(weighted_li)/len(weighted_li))
	print "best weighted " + str(sum(best_weighted_li)/len(best_weighted_li))



if __name__ == '__main__':
	# Based this on the sample script from part 2, but only needed the file name option
	optparser = optparse.OptionParser()
	optparser.add_option("-d", dest="data_file", help="Crowdflower csv file.")
	
	(opts, _) = optparser.parse_args()

	compute_and_print_best_versions(opts.data_file)
	
