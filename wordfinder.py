"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """
>>> wf = WordFinder("words.txt")
235886 words read

>>> len(wf.words) == 235886
    True

>>> random_word = wf.random()
>>> random_word in wf.words
    True
    """

    def __init__(self, file_path):
        """Reads a file_path with a list of words, making attribute of list of those words,
        counts how many words read"""
        self.words = self.read_file(file_path)
        print(f'{len(self.words)} words read')

    def __repr__(self):
        """Shows better representation in terminal"""
        return f"WordFinder(file_path='{self.file_path}')"

    def read_file(self, file_path):
        """reads the file_path"""
        file = open(file_path, 'r')
        content = file.read()
        words = content.split()
        file.close()
        return words

    def random(self):
        """picks a random word from the list of words"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

  >>> swf = SpecialWordFinder("complex.txt")
  3 words read

  >>> swf.random() in ["pear", "carrot", "kale"]
  True

  >>> swf.random() in ["pear", "carrot", "kale"]
  True

  >>> swf.random() in ["pear", "carrot", "kale"]
  True
  """

    def read_file(self, file_path):
        file = open(file_path, 'r')
        return [word.strip() for word in file
                if word.strip() and not word.startswith("#")]
