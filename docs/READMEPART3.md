**how the code runs:** 
crawler:
The crawler is what we run to get our books from the childrenslibrary website. It has not been optimized to take in inputs but it can be done. As of now I just need to change the specified language in main and the script handles getting all of the links to the book pages and downloads all of the images in each book, numbering them by page. More specifically, it uses beautifulsoup4 and urllib libraries to work with the requests and html, with the son library to help parsing. It is optimized for the childrenslibrary website.

qc:
Reads the csv from the QC hit and then decides based on how high the translation was rated whether or not to use the original translation  or a new one.

**translaion hits:**
Currently our only hits available are spanish, have more books in different languages but have been testing on the crowd to see what kinds of responses we get. It’s obvious that translating from certain languages is much easier and we are hoping to ensure that we get good accuracy by choosing languages that can be well translated with crowd flower.

The hits themselves are relatively simple.You are given first given an image with a yes or no question, is there text in this image? This is necessary because many children books just have art and no text on some pages. If you go with no, then the hit is done, if there is text on the page you are asked to translate and transcribe it to the given text box that appears.

**step by step(Videos Included)**
https://vimeo.com/163340024
1: Go to this link https://tasks.crowdflower.com/assignments/8f8bda7d-53ce-4276-a306-491b8db99db0?cf_internal=true
2: Decide if the image has text or not and respond appropriately
3: If no then done, else translate the text from the image into the given textbox
QC Hits:
https://vimeo.com/163342015
1: Go to this link:https://l.facebook.com/l.php?u=https%3A%2F%2Ftasks.crowdflower.com%2Fchannels%2Fcf_internal%2Fjobs%2F897501%2Fwork%3Fsecret%3DdSJ%252FhvhHXV1SMpX7PPxqYZ%252FzrXt3qxgRnjT5eWhfKdvf&h=0AQFuG_Ve
2: Decide if the image has text or not and respond appropriately
3: If no then done, else decide how well the text was translated, based on how much you can understand it. 

Contact any or all of these emails if any issues occur: ovallej@seas.upenn.edu holdenmc@seas.upenn.edu selzern@sas.upenn.edu

With these hits you are given 5 pages of already translated hits. The same yes or no question is applied to make sure that there is text on the page. If the answer is yes then you are supposed to rate the translation given by understandability with a scale from 1 to 10.
