def eggs(cheese): #that's why it's better to use self, master for def
    cheese.append('Hello') 

spam = list(range(1,4))
eggs(spam) #this method calls on spam list, and appends it
print(spam)
