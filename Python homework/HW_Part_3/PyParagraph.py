# -*- coding: utf-8 -*-
f = open("Lenny.txt", "r", encoding="utf-8").read()

# using split() 
# to count words in string 
total_words = len(f.split()) 

#sentence count (count number of periods)
total_sentences = f.count('.')

#avg number of letters in word
#create dictionary with letters per word
letter_count = {}

for i in f.split():
    letter_count[i] = len(i)

print(letter_count)

#avg values of a dictionary
count = 0
_sum = 0
for key in letter_count:
    count += 1
    _sum += letter_count[key]

avg_letters=round((_sum/count),1)

#avg words per sentence
sents = f.split('.')
avg_len = round(sum(len(x.split()) for x in sents) / len(sents),1)

#string together and print result

str1 = "Paragraph Analysis"
line = "----------------------------"
str2 = ("Approximate Word Count: " + str(total_words))
str3 = ("Approximate Sentence Count: " + str(total_sentences))
str4 = ("Average Letter Count: " + str(avg_letters))
str5 = ("Average Sentence Length: " + str(avg_len))

a = '\n'.join([str1,line,str2,str3,str4,str5])
print(a)

#save results to txt
file = open('results.txt','w') 
 
file.write(a) 

file.close() 

