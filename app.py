print("Hello, I can help you find the average of any number you give me")
# creating a function 
def average_tool ():
    # Creating a list where user inputs will be going in 
    numbers = []
    # use a while loop to keep prompting the user if they would like to keep adding to their list
    while True:
        userinput = input('what number will you like to add to your list, when finished type "done"')
        if userinput == 'done':
            break
        else:
          # converts user input into float in case the user enters decimal numbers
            number = float(userinput)
          # adds the current user input to the list of numbers
            numbers.append(number)

  # Creating a variable using the built-in sum function to get the sum of the list 
    total=sum(numbers)
  # Creating a variable that gets the average
    average = total / len(numbers)

    print("the average is:", average)

average_tool()
