import requests
from collections import Counter
from bs4 import BeautifulSoup
import string
table = str.maketrans(dict.fromkeys(string.punctuation))
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize



link = requests.get("https://en.wikipedia.org/wiki/Olympic_weightlifting")
soup = BeautifulSoup(link.content, 'html.parser')
"""
section = soup.find_all('span', {"class":"mw-headline"})

print(section[0])
for tag in section:
    print(tag.text)
    print(tag.get('id'))
    print("hyperlinks for: " + tag.text)
    for link in tag.select("a"):
        print(link['href'])
"""
myList = []
section = soup.find_all(['h{}'.format(i) for i in range(2,4)])
for i in section:
    k = i
    if i.find_all('span', {"class":"mw-headline"}):
        string = i.text.replace("[edit]", "")
        print(string)
        
        words = k
        nextWords = words.find_next_siblings()
        para = ""
        for nextWord in nextWords:
            if nextWord.name == 'h3' or nextWord.name == 'h2':
                break
            elif nextWord.name == 'p':
                para += nextWord.get_text(strip=True)
        
        para = para.translate(table)
        paraTokens = word_tokenize(para)
        paraResults = [word for word in paraTokens if not word in stopwords.words()]
        nonSW = Counter(paraResults)
        most = nonSW.most_common(10)
        if most:
            print(most)
        else:
            print("None")
        print()
        
        #print(nextWords.get_text(strip=True).strip())
        print("hyperlinks for: " + string)
        links = k.find_next_siblings()
    
        for link in links:
            if link.name == 'ul' or link.name == 'p':
                for hyperL in link.find_all("a"):
                    print(hyperL['href'])
            elif link.name == 'h2' or link.name == 'h3':
                break
        print()
