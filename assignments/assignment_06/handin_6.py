"""Create a module containing a class: TextComparer with the following methods:

    __init__(self, url_list)
    download(url,filename) that stores the file on disk and raises NotFoundException when url returns 404
    multi_download() uses threads to download multiple urls as text and stores filenames on a property of the TextComparer class object (Hint: use the download() method and create the filenames from the url or from the response object)
    __iter__() returns an iterator
    __next__() returns the next filename (and stops when there are no more)
    urllist_generator() returns a generator to loop through the urls
    avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
    hardest_read() reads all text from files in filenames and returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
"""
from xml.dom import NotFoundErr
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

class TextComparer:
    
    def __init__(self, url_list):
        self.url_list = url_list
        self.file_list = [url.split('/')[-1] for url in url_list]
    
    def download(self, url, filename):
        response = requests.get(url, allow_redirects=True)
        if(response.status_code != 200):
          print('URL didnt work')
        open(filename, 'wb').write(response.content)
        
        
    def multi_download(self):
      with ThreadPoolExecutor(len(self.url_list)) as ex:
        ex.map(self.download, self.url_list, self.file_list)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.file_list):
            file = self.file_list[self.current_index]
            self.current_index += 1
            return file
        raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, filename):
        with open(filename) as text:
            total_vowels = 0
            total_chars = 0
            total_words = 0
            lines = list(line for line in (l.strip() for l in text) if line)
            for line in lines:
                for word in line.split(' '):
                    total_words += 1
                    for char in word:
                        total_chars += 1
                        if char in "aeiouAEIOU":
                            total_vowels += 1
        return total_vowels / total_words

    
    def hardest_read(self, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            response = ex.map(self.avg_vowels, self.file_list)
            return list(response)




textComp = TextComparer(['https://www.gutenberg.org/files/11/11-0.txt', 'https://www.gutenberg.org/files/1342/1342-0.txt', 'https://www.gutenberg.org/files/345/345-0.txt'])
iterator = iter(textComp)

#textComp.multi_download()

#print(next(iterator))

#tmp_url = textComp.urllist_generator()
#print(next(tmp_url))

#print(textComp.avg_vowels(textComp.file_list[0]))

#print(textComp.hardest_read())