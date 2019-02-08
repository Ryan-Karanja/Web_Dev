from nose.tools import *

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

 

def scan(sentence): 

    words = sentence.split() 
    result = [] 
    
    for word in words:
        check_string = convert_numbers(word) 
                                             
        
        if word in lexicon: 
            
            check_number = convert_numbers(word) 
            
            pair = (lexicon[word], check_number) 
            result.append(pair) 
				
        
        elif type(check_string) == type(1):
            
            number = convert_numbers(word)
            if number:
                pair = ('number' , number) 
                result.append(pair)
        else:
            error_word = word
            pair = ('error', error_word)
            result.append(pair)
                
    return result

def convert_numbers(s):
	
    try:
        return int(s)
    except ValueError:
        return s