from typing import Collection


def word_check(text):
    good_words = []
    corrected_words =[]
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = text.split()
    word_dictionary = {}
    ######### Remove bad Words from String
    
    for word in words:
        bad_letter  = 0 
        for letter in word:
            if letter not in alphabet:
                bad_letter += 1
        if bad_letter/len(word) < 0.5 : 
            #####change string to lower case 
            good_words.append(word.lower()) 
            
    ######## Remove Bad Letters from words
    
    for word in good_words:
        new_word = ''
        for letter in word:
            if letter in alphabet:
               new_word += letter
        corrected_words.append(new_word)
        
    ##### Captalize corrected words  and print correct string
    
    final_words = [word.capitalize() for word in corrected_words]
    print(' '.join(final_words))
    
    ###########find count of each word in stirg  and update dictionary 
    
    for word in final_words:
        count = 0
        for repeat in final_words:
            if word ==repeat:
                count += 1
        comb = {word:count}
        word_dictionary.update(comb)
    print(word_dictionary)
            
            
            
string = '"hEllO My FriEnDs!!! thIS i$s A tE%sT For your  #p#r#o#b#l#e#m a'
word_check(string)