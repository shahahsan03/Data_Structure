# # Decimal to Binary

# class Stack:
#     def __init__(self):
#         self.items = [] #create new list with no items
#     def __repr__(self):
#         return repr(self.items) #define what to return is the stackname is called
#     def isEmpty(self):
#         return self.items == [] #check whether list if empty and return T or F
#     def size(self):
#         return len(self.items) #return size of stack (= length of list)
#     def push(self,val):
#         self.items.append(val) #add the argument pass to the end of list
#     def pop(self):
#         return self.items.pop() #return the last item in list because index not specified
#     def peek(self):
#         return self.items[-1] #return last item (-1 because from right indices are negative)

# NumDec=0    #initialize as int
# NumBin=''   #initialize as string

# NumDec=int(input("Please enter the integer to convert : ")) #assign the Number to variable
# print ("Decimal Number = ",NumDec)

# thestack=Stack()    #create the stack

# while NumDec>0 :    #loop till the number we divide is 1 or 0
#     thestack.push(NumDec%2) #add the remainder when divide by 2 to stack
#     NumDec=NumDec//2    #change the number to be divide to the whole number when divided by 2

# while thestack.isEmpty()==False:    #loop till stack become empty
#     NumBin=NumBin+str(thestack.pop())   #add the item to string
# print("Binary Number = ",NumBin)



# Reverse a String:

# def reverse_string(input_string):
#     stack = []
#     for char in input_string:
#         stack.append(char)
#     reversed_string = "".join(stack)
#     return reversed_string[::-1]

# input_string = input("Enter text: ")
# reversed = reverse_string(input_string)
# print(reversed, "<-- Reversed Input")


def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

input_string = input("Enter text: ")
reversed = reverse_string(input_string)
print(reversed, "<-- Reversed Input")