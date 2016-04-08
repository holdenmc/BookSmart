# BookSmart

NETS 213 Final Project

_Milestones: Data Collection, Translation, Quality Control, Data Aggregation_

**Data Collection:**

  We will need to get our book data from the Children's Digital Library. For this we will write a python script using things we have done in class previously. 2pts

  Once we have this data we must arrange it in reasonably sized portions to make separate hits as well as keeping them organized in a manner than translates well for our aggregation later on. 1pt

**Translation:**

 Designing the hits, how many people for each, planning all the separate types of hits we may want to add. Also test hits 3pts

 Aggregating the translation data 1pt

**Quality Control:**

  Design quality control--still under progress--(suggestions include multiple translations, checking text similarity, and following quality control methods from class/past assignments)4pts

  Determine quality of workers and maintaining hits, and use highest quality responses. 2pt

**Data Aggregation:**

  Create books from our data. Must keep track of relevant info from translation. (possible Have crouwd workers organize the book for us) 3pts


## Raw Input
- We require books from the booksite http://www.childrenslibrary.org/, in the form of images.
- Each image represents a page.

**Data Retrieval:** We have developed a crawler, currently named "get_links_crawler.py". This crawler is made specifically for the childrenslibrary and can easily be used to pull all books in a specific language. The crawler is nearly complete, all that is necessary at this point is to make sure it ignores books that are already translated into english.
Our raw data can be seen in the form of a list of images in our repo, the folder wilhelm contains a book we gathered with our crawler. We will use this crawler to get the full data set, a certain number of books.


## Data Format
**QC Input**
- The raw data files (.jpg)

**QC Output**
- CrowdFlower report (.csv)
	- including QC Data

**Aggregation Input**
- CSV file with fields fileName (or URL), original, rating, updated
	- original is the translation from the first round HIT
	- rating is a value between 1 and 10 that represents how accurate the 2nd Pass HIT worker thinks the original translation was
	- Updated is the translation provided by the 2nd Pass HIT worker that they believe is more accurate

**Aggregation Output**
- Tab-separated txt file
	- fileName \t most_accurate_translation
	- Here we will have the best translation for each page of each book


## QC Algorithm
- Second Pass HIT
	- Show Worker the picture of the page and the translation provided by a previous worker
	- Ask worker for Rating from 1 to 10 on how accurate that translation is
	- Ask worker for an Updated translation that they believe is more accurate
	- If Rating > 8, keep original translation. Else, take Updated translation
- We will also utilize CrowdFlower's reliability data to weed out bad workers


## Aggregation Algorithm
- Script looks at how workers rated the translations. 
- We choose the highest rating
- In case of a tie, choose the first one
