lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    '1234': 'number',
    3: 'number',
    91234: 'number'
    }

 

def scan(sentence): #no need to go all in and overflow your code with classes and objects , just go with a simple function  

    words = sentence.split() #gets every item (word) one , by one from the lexicon.scan in the test
                             #remember that an empty space will mark the beggining of new item(3 91234 is "3" and "91234")
    result = [] # this is the tuple in the list that the test is looking for, and the function will return it after appending.
    
    for word in words:
        check_string = convert_numbers(word) # we need this to convert (if it can) a string to integer with conver_numbers() function
                                             
        
        if word in lexicon: 
            
            check_number = convert_numbers(word) 
            # we need this one for examples like assert_equal(lexicon.scan("1234"), [('number', 1234)])
            #if there is an integer in the tuple ,instead of a string like most of them in the exercise(a little 'trap' by Zed)
            #in the convert_numbers() funtion if the string cant be return as int it will be return as string again so no worries.
            pair = (lexicon[word], check_number) #pairs the two final words in a tuple ...
            result.append(pair) #...so that it can return the tuple in a list.
				
        
        elif type(check_string) == type(1): #we check if the type of the variable check_string is int ,and if it is then we proceede.
            
            number = convert_numbers(word)
            if number:
                
                pair = ('number' , number) #pretty much the same as above only here we put the string 'number' directly in the tuple
                result.append(pair)
        else:
          #this is the tricky part(not hard tho) this final if-statement looks if a word is missing from our dict
          #and if it is missing it counts as error
            error_word = word
            pair = ('error', error_word)
            result.append(pair)
                
    return result
    
def convert_numbers(s):
  '''This is our simple convertor, who checks if a string can be retunred as int and if it can't it moves on as string again'''
  try:
        return int(s)
  except ValueError:
        return s
        