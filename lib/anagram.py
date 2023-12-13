# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        # Convert the input word to lowercase and sort its characters
        sorted_word = sorted(self.word)

        # Using a list comprehension to filter possible anagrams
        matches = [anagram for anagram in possible_anagrams if self.is_anagram(anagram, sorted_word)]

        return matches

    def is_anagram(self, candidate, sorted_word):
        # Check if the candidate word is not the same as the original word and if the sorted characters of both words match
        return candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word

word = 'listen'
possible_anagrams = ['enlists', 'google', 'inlets', 'banana']

anagram = Anagram(word)
result = anagram.match(possible_anagrams)

print(result)