from collections import defaultdict
fname=input('enter file name')
file=open(fname,'r')
lines=0
words=0
char=0
Uniquewords = defaultdict(int)
for line in file:
    wordslist=line.split()
    lines=lines+1
    words=words+len(wordslist)
    char=char+len(line)
for word in open(fname).read().split():
	Uniquewords[word] += 1
print('lines are:'+str(lines))
print('words are:'+str(words))
print('chars are:'+str(char))
print('the unique words are:',Uniquewords)







