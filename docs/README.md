# BookSmart
NETS 213 Final Project
Milestones: Data Collection, Translation, Quality Control, Data Aggregation
Data Collection:

  We will need to get our book data from the Children's Digital Library. For this we will write a python script using things we have done in class previously. 2pts
  
  Once we have this data we must arrange it in reasonably sized portions to make separate hits as well as keeping them organized in a manner than translates well for our aggregation later on. 1pt
  
Translation:

 Designing the hits, how many people for each, planning all the separate types of hits we may want to add. Also test hits 3pts
 
 Aggregating the translation data 1pt
 
Quality Control:

  Design quality control--still under progress--(suggestions include multiple translations, checking text similarity, and following quality control methods from class/past assignments)4pts
  
  Determine quality of workers and maintaining hits, and use highest quality responses. 2pt
  
Data Aggregation:

  Create books from our data. Must keep track of relevant info from translation. (possible Have crouwd workers organize the book for us) 3pts



## Data Format
QC Input
- CSV file with fields fileName (or URL), original, rating, updated
	- original is the translation from the first round HIT
	- rating is a value between 1 and 10 that represents how accurate the 2nd Pass HIT worker thinks the original translation was
	- Updated is the translation provided by the 2nd Pass HIT worker that they believe is more accurate

QC Output
- Tab-separated txt file
	- fileName \t most_accurate_translation

Aggregation Input
- x

Aggregation Output
- x


## QC Algorithm
- Second Pass HIT
	- Show Worker the picture of the page and the translation provided by a previous worker
	- Ask worker for Rating from 1 to 10 on how accurate that translation is
	- Ask worker for an Updated translation that they believe is more accurate
	- If Rating > 8, keep original translation. Else, take Updated translation


## Aggregation Algorithm
- x
