import sys
import optparse
import re
import os

'''
Prints average 

'''

def make_book(file) :
	file_object = open(file, 'r')
	reg = re.compile("\/[a-zA-Z|_|']*\d+\.jpg")
	reg_link = re.compile("https.*\.jpg")
	reg_num = re.compile('\d+')
	d = {}
	curr_key = ""
	for i in file_object.readlines():
		matches = reg.findall(i)
		if len(matches) > 0:
			page = reg_num.findall(matches[0])[0]
			curr_key = matches[0]
			''' all this stuff is to ensure
			pages are numbered and ordered correctly '''
			page_char = str(unichr(int(page) + 65))
			curr_key = curr_key.replace(page, page_char)
			old = reg_link.findall(i)[0]
			d[curr_key] = i.replace(old, "")
		else:
			d[curr_key] = d[curr_key] + ' ' + i
	file_object.close()
	li = d.keys()
	li.sort()
	'''sorts the pages for us'''
	breaks = [0]
	books = []
	curr_name = li[0][0:4]
	for i,x in enumerate(li):
		if curr_name not in x:
			breaks.append(i)
			curr_name = x[0:4]
	books = ["" for i in breaks]
	curr_name = li[0][0:4]
	counter = 0
	''' adds each page to a string for the respective book '''
	for x in li:
		if curr_name not in x:
			curr_name = x[0:4]
			counter += 1
		books[counter] = books[counter] + d[x]
	''' writes the book'''
	for i,book in enumerate(books):
		title = li[breaks[i]]
		direct = 'student_text_files'
		if not os.path.exists(direct):
			os.makedirs(direct)
		fi = open(direct + "/" + title[1:len(title)-4] + '.txt', 'w+')
		fi.write(book)
		print title





	



if __name__ == '__main__':
	# Based this on the sample script from part 2, but only needed the file name option
	optparser = optparse.OptionParser()
	optparser.add_option("-d", dest="data_file", help="Crowdflower csv file.")
	
	(opts, _) = optparser.parse_args()

	make_book(opts.data_file)
	
