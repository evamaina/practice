import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
        print('You typed ' + response + '.')

        """you can cause the program to terminate, or exit, by
calling the sys.exit() function. Since this function is in the sys module, you
have to import sys before your program can use it.This program has
 an infinite loop with nobreak statement inside. The only way this
  program will end is if the user entersexit , causing sys.exit()
  to be called. When response is equal to exit , the pro-gram ends.
   Since the response variable is set by the input() function, the user
must enter exit in order to stop the program"""
