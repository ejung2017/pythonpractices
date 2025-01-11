bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

# .splitlines() is a function within sys module that separates the string per line and returns those line of strings in a list 

message = ''
message = input("Enter the message you want to display: \n")
    
for line in bitmap.splitlines(): 
    for index, char in enumerate(line): 
        if char == " ": 
            print(" ", end="")
        else: 
            print(message[index % len(message)], end="") 
    print()