sentences = [
    "I love Spark",
    "Spark is fast",
    "Big Data"
]

words = []

for sentence in sentences:
    split_words = sentence.split(" ")
    words.append(split_words)

print(words)