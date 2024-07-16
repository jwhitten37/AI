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

# This variable contains symbols to remove that may appear in song lyrics
remove_chars = [';',':','!',"*","(",")",","]

# This function creates a sorted list of words and thier word counts
def count_lyrics(song):
    word_list = []

    # These 'for' loops iterate through the lyrics, removing symbols and splitting on whitespace
    for i in remove_chars:
        song = song.replace(i,'')
    for words in song.split():
        word_list.append(words)
    
    # This 'for' loop creates the unique word list
    unique_words_list = []
    for word in word_list:
        if sum(x.count(word) for x in unique_words_list) == 0:
            word_count = word_list.count(word)
            unique_words_list.append([word,word_count])
    
    # The following sorts the list in reverse order based on the word count
    sorted_list = sorted(unique_words_list, key = lambda x: (x[1]),reverse=True)

    # Next, we print the outcome of the sorted list in a structured manner
    print("Here are the word counts from the song provided:")
    for values in sorted_list:
        print(values[0]+":",values[1])

# Call the function
count_lyrics(song)