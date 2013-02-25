#!/usr/bin/python

## Help with:
## 1. Can you show me how to install the requests module via git hub? http://kennethreitz.org/exposures/requests
## 2. What is the best way of doing HTTP requests in Python anyways?
## 3. What is the point of having xcode. Can it compile python?
## 4. Think I know enought that I'll be okay during the comp?


###
## Question 2: FizzBuzz ##############################################################################
###

def fizzbuzz():
    ## iterate through numbers 1 to 100
    for i in range(1,101):
        
        # if the remainder when divided by three and by five is 0, then it is a multiple of both of them.
        # alternatively could use if i%15 == 0:
        if i%3 == 0 and i%5 == 0: 
            print 'FizzBuzz'
        # if the remainder when divided by five is 0, it is a multiple of 5.
        elif i%5 == 0:
            print 'Buzz'
        # if the remainder when divided by three is 0, it is a multiple of 3.
        elif i%3 == 0:
            print 'Fizz'
        # if the number is not a multiple of 3 or 5, just print it.
        else:
            print i

###
## Question 3: swapchar ##############################################################################
###

def swapchars(string):
    
    ### Check if the input is indeed a string.
    if not isinstance(string,str):
        return None
    
    else:
        
        ### Goes through the string, counts each letter.
        frequency = {}
        for i in string.lower():
            if i.isalpha():
                if i in frequency:
                    frequency[i] = frequency[i] + 1
                else:
                    frequency[i] = 1

        ### Picks which letter is the most frequent, which is the least frequent
        most = 0
        most_letter = ''
        least = 1000
        least_letter = ''
        for i in frequency:
            if frequency[i] > most:
                most = frequency[i]
                most_letter = i
            if frequency[i] < least:
                least = frequency[i]
                least_letter = i

        ### Replaces the least common with a filler
        string1 = string.replace(least_letter,'xxxxx')
        string2 = string1.replace(least_letter.upper(),'XXXXX')

        ### Replaces the most common with the least
        string3 = string2.replace(most_letter, least_letter)
        string4 = string3.replace(most_letter.upper(), least_letter.upper())

        ### Replaces filler with the most common
        string5 = string4.replace('xxxxx',most_letter)
        string6 = string5.replace('XXXXX',most_letter.upper())

        ### Returns the result
        return string6

###
## Question 4: sortcat ##############################################################################
###

def sortcat(n,*args):
    
    ## ensure the proper form of n
    if not isinstance(n,int):
        print 'Please enter swapchar(int >= -1,str,str,...)'
        return None
    if n < -1:
        print 'Please enter swapchar(int >= -1,str,str,...)'
        return None
    
    ## go through, make sure every other input is a string
    for e in args:
        if not isinstance(e,str):
            print 'Please enter swapchar(int >= -1,str,str,...)'
            return None

    ## sort the list from longest to shortest
    s = sorted(args,key=len,reverse=True)

    ## initialize variables
    counter = 0
    output = ''

    ## case where n is -1, concatenate all present items
    if n == -1:
        for e in s:
            output = output + e
    ## case where n is a number, concatenate the proper number in order from longest to shortest
    else:
        for e in s:
            if counter < n:
                output = output + e
                counter = counter + 1
            else:
                break

    ## return the output
    return output

###
## Question 5: Look Away ##############################################################################
###

import random

## To run use function 'look_away' with input 'number' = the amount of trials to be run.
def look_away(number):
    
    ## check if number of trials requested is actually a valid number
    if not isinstance(number,int):
        return None
    if number < 1:
        return None
    
    else:
        ## initializing variables
        luigi_wins = 0
        team_wins = 0
        
        
        ## looping through trials the proper amount of times
        for i in range(1,number+1):
            
            ## Need to reinitialize players every time
            player1 = 1
            player2 = 1
            player3 = 1
            
            ## each game lasts 5 rounds
            for i in range(0,5):
                
                ## assign remaining players a random number to simulate looking in a direction
                if player1:
                    player1 = random.randint(1,5)
                if player2:
                    player2 = random.randint(1,5)
                if player3:
                    player3 = random.randint(1,5)
                
                ## if the numbers match looking forward (matching luigi), then they are eliminated
                if player1 == 1:
                    player1 = None
                if player2 == 1:
                    player2 = None
                if player3 == 1:
                    player3 = None
                
                ## this eliminates unnecessary interations through the loop
                if not player1 and not player2 and not player3:
                    break

            ## this keeps track of the number of wins by each team
            if not player1 and not player2 and not player3:
                luigi_wins = luigi_wins + 1
            else:
                team_wins = team_wins + 1
        
        return float(luigi_wins)/(luigi_wins+team_wins)

### 5.c
## an indiviual team member has a (4/5) chance of surviving each round, so in 5 rounds, they have a (4/5)^5 chance of surviving. This means that they have a 1-(4/5)^5 chance of dying.
## since all team members must die in order for luigi to win by looking forward, all three team members must die. Thus Luigi's chance of winning is (1-(4/5)^5)^3. This is about .304, which is
## indeed the result of running to program through many many trials.

###
## Question 8: API Shuttleboy ##############################################################################
###


print('I love the Crimson tech department!')

