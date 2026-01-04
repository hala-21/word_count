'''
with open ("story.txt","r",encoding="utf-8", errors="ignore") as file:

     words = file.read().split()

word_count = len(words)

count = {"word_count" : word_count}


def num():
    return count.items()

print (num())


'''
with open ("story.txt","r",encoding="utf-8", errors="ignore") as file:

     words = file.read().split()
   
word_count = {}

for word in words: 
    if word in word_count:
            word_count[word]+=1
    else:
            word_count[word]=1

print (word_count)
