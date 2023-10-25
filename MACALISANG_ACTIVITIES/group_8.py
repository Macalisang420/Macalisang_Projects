user1 = 'ian'
pass1 = 'ian123'

max_attempts = 5
score = 0

def quiz (sas):

       for x in sas:

            answer_key = sas[x]
            print(x)

            answer = input('Input your answer: ')

            if (answer.lower() == answer_key.lower()):
                print("Correct!")
                score += 1

sas11 = {'1. This anables a particular set of conditions to je executed repeatedly until a condition is satisfied.':'For Loop',
         '2. This function either takes a single number and behaves like a list of numbers going from zero until the number before the one specified.':'Range' ,
         '3. This is running a loop inside another loop.':'Nested loop' ,
         '4. A loop that is never finished. ':'Infinite loop' ,
         '5. For loops are used for _______ traversal.':'Sequential' ,
         '6. If a sequence contains an expression list, it is evaluated _______.':'First' ,
         '7. An alternative way of iterating through each item is by _________ into the sequence itself.':'Index offset' ,
         '8. If the else statement is used with a _________, the else statement is executed when the loop has exhausted the iterating the list.':'For loop' ,
         '9. If the else statement is used with a ________, the else statement is executed until the condition becomes false.':'While loop',
         '10. This is iterating through each item by index off setting as an alternative.':'Iterating by sequence index'}
sas12 = {'1. These alter the execution in a loop.':'Loop control statements',
         '2. This statement is used to exit out of the loop.':'Break' ,
         '3. This statement allows you to bypass the current iteration of any loop.':'Continue ' ,
         '4. This statement is also considered as a non-operation statement.':'Pass' ,
         '5. Whenever the controller encounters a _____ statement, it comes out of that loop immediately.':'Break' ,
         '6. When this statement is encountered in a loop, the Python interpreter ignores the rest of the loop statements for the current iteration.':'Continue' ,
         '7. This statement is generally used to indicate "null" or unimplimented functions and loops.':'Pass' ,
         '8.  This statement is much like a comment but is executed by the Python interpreter like valid python statements.':'Pass' ,
         '9. This statement does not end the loop but rather moves to the next iteration.':'Continue',
         '10. This statement is useful when we want to terminate the loop as soon as the condition is fulfilled.':'Break'}
sas13 = {'1. These are used on conditional statements that yield a result of either true or false value.':'Logical operators',
         '2. This operator is used if the operation is TRUE if both the operands are true.':'Logical AND' ,
         '3. This operator is used if the operation is TRUE if either of the operands are true.':' Logical OR' ,
         '4. This operator is used if the operation is TRUE if the operand is false.':'Logical NOT' ,
         '5. This is Python evaluating logical operators in the order they are listed when you mix them in an expression.':'Operator precedence' ,
         '6. The precedence of logical NOT.':'High' ,
         '7. The precedence of logical OR.':'Low' ,
         '8. The precedence of logical AND.':'Medium' ,
         '9. In case an expression has several operators with the same precedence, Python will evaluate them from ______________.':'Left to right' ,
         '10. Python will group the operator with the ___________ precedence first.':'Highest' }

while max_attempts > 0:

    user = input('Input your username: ')
    password = input('Input your password: ')

    if user1 == user and password == pass1:
        print('login successful')

        quiz(sas11)
        quiz(sas12)
        quiz(sas13)
        
        break
    elif user1 != user and pass1 != password:
        print('try again')
        max_attempts -= 1
    elif user1 != user and pass1 == password:
        print('try again')
        max_attempts -= 1
    elif user1 == user and pass1 != password:
        print('try again')
        max_attempts -= 1
    
if max_attempts == 0:
    print('You reached the max attempts!')

if score >= 15 and score <= 20:
    print('You passed!')
elif score >= 20 and score <=25:
    print('Greate score')
elif score == 30:
    print('perfect')
else:
    print('You failed!')



print('Average: ', score/3)
print('Score: ',score)




        
    
    


