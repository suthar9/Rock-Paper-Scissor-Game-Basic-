'''



from  urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')

story_word = []
for line in story:
    line_words = line.decode('utf8').split()
    for words in line_words:
        story_word.append(words)

    story.close()
print(story_word)
'''


list = [1,2,3,4]

def func (x):
    x.append(90)
    print(x)

func(list)

