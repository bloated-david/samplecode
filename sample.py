import requests
from collections import Counter
from bs4 import BeautifulSoup
import string
table = str.maketrans(dict.fromkeys(string.punctuation))
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize



link = requests.get("https://en.wikipedia.org/wiki/Olympic_weightlifting") //URL of Wikipedia page
soup = BeautifulSoup(link.content, 'html.parser')

myList = []
section = soup.find_all(['h{}'.format(i) for i in range(2,4)]) //Finding all the sections
for i in section:
    k = i
    if i.find_all('span', {"class":"mw-headline"}):
        string = i.text.replace("[edit]", "")
        print(string) //Printing sections' name
        
        words = k
        nextWords = words.find_next_siblings() //Taking the content into a list format to iterate through  
        para = ""
        for nextWord in nextWords:
            if nextWord.name == 'h3' or nextWord.name == 'h2': //Stopping the loop when we find the next section since we added all the text
                break
            elif nextWord.name == 'p':
                para += nextWord.get_text(strip=True) //Adding each paragraph together under each section
        
        para = para.translate(table) //Taking punctuation out
        paraTokens = word_tokenize(para)
        paraResults = [word for word in paraTokens if not word in stopwords.words()] //Removing stop words
        nonSW = Counter(paraResults) //Counting the frequency of each words in the text
        most = nonSW.most_common(10) //Creating a list of the highest 10 frequency words 
        if most:
            print(most)
        else:
            print("None")
        print() //Spacing for readability
        
        print("hyperlinks for: " + string)
        links = k.find_next_siblings() //Starting at the top under the section to find links
    
        for link in links:
            if link.name == 'ul' or link.name == 'p':
                for hyperL in link.find_all("a"):
                    print(hyperL['href'])
            elif link.name == 'h2' or link.name == 'h3':
                break
        print()
