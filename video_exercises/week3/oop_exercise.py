import string

class TextContainer():


 def __init__(self, my_text):
     self.my_text = my_text



def count_words_in_text(self):
    words = self.my_text.split()
    return len(words)


def count_chars_in_text(self):
    words = self.my_text
    return len(words)


def count_only_ascii(self):
    count = 0
    for char in self.my_text:
     if char in string.ascii_letters:
        count += 1
    return count

 
def remove_punc(self):
    new_string = self.my_text.translate(str.maketrans(",", string.punctuation))
    return new_string
    #https://datagy.io/python-remove-punctuation-from-string/


tc = TextContainer("my_text!! dwaf wafawf awf awfs fd df 42")
print(count_words_in_text(tc))
print(count_chars_in_text(tc))
print(count_only_ascii(tc))
print(remove_punc(tc))



"""Create a Python module, which consists of a class TextContainer. The class must have a constructor which allow objects to be initialized with a text
 ala: tc = TextContainer(my_text). The class must implement the following methods for computing statistics on texts.

    Counting the amount of words used in a text.
    Counting the amount of chars used in a text.
    Counting the amount of letters, where letters are all ASCII letter characters, see

    import string
    string.ascii_letters  # returns 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    Remove all punctuation characters, see

    import string
    string.punctuation  # returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

"""