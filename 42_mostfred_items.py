from collections import Counter

text = ' We hope to one day become the world leader in free, the educational resources. We are constantly discovering and adding more free content'

words = text.split()


#print(words)

counter = Counter(words)

top_three = counter.most_common(3)
print(top_three)