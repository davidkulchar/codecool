def main() :
    comm = input("Please specify a command [list, add, mark, archive]:  ")
    
    if comm == "add" :
        add()
    if comm == "list" :
        listw()  
    if comm == "mark" :
        mark()
    if comm == "archive" :
        archive()

def listw() :
    fr = open ('todolist', 'r')
    i = 1
    print ('\n')
    for line in fr:
        print (i,". [ ] " + line )
        i = i + 1

def add(): 
    fa = open ('todolist', 'a')
    element = input(('Add an item: '))
    fa.write(element + '\n' )
    print('Item added.')

def mark() :
    f = open('todlist', 'a')
    task = input("Which one you want to mark as completed: ")
    f.write(task +"\n")
    print( task, " is completed")

main()