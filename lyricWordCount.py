song = """Elvira
Elvira
My heart's on fire for Elvira
With eyes that look like heaven
Lips like cherry wine
That girl can sure enough make my little light shine
I get a funny feelin' up and down my spine
'Cause I know that my Elvira's mine
Elvira
Elvira
My heart's on fire for Elvira
Giddy up, um-poppa-um-poppa, mow, mow
Giddy up, um-poppa-um-poppa, mow, mow
High-ho silver, away
Tonight I'm gonna meet her at the hungry house café
I'm gonna give her all the love I can
Yes, I am
She's gonna jump and holler
I've saved up my last two dollar
We're gonna search and find that preacher man
Then I'll be singin'
Elvira
Elvira
My heart's on fire for Elvira
Giddy up, um-poppa-um-poppa, mow, mow
Giddy up, um-poppa-um-poppa, mow, mow
High-ho silver, away
Elvira
Elvira
My heart's on fire for Elvira
Giddy up, um-poppa-um-poppa, mow, mow
Giddy up, um-poppa-um-poppa, mow, mow
High-ho silver, away
Elvira (yeah)
Elvira
My heart's on fire for Elvira
Giddy up, um-poppa-um-poppa, mow, mow
Giddy up, um-poppa-um-poppa, mow, mow
High-ho silver, away
Play again
Whoo!"""

remove_chars = [';',':','!',"*","(",")",","]

def count_lyrics(song):
    word_list = []
    for i in remove_chars:
        song = song.replace(i,'')
    for words in song.split():
        word_list.append(words)
    
    unique_words_list = []
    for word in word_list:
        if word not in unique_words_list:
            unique_words_list.append(word)

    unique_words_count = []
    for i in unique_words_list:
        unique_words_count.append(word_list.count(i))
    
    combined_list = []
    iteration = 0
    while iteration < len(unique_words_list):
        combined_list.append((unique_words_list[iteration],unique_words_count[iteration]))
        iteration += 1
    
    sorted_list = sorted(combined_list, key = lambda x: (x[1]),reverse=True)
    print("Here are the word counts from the song provided:")
    for values in sorted_list:
        print(values[0],": ",values[1],",")



count_lyrics(song)