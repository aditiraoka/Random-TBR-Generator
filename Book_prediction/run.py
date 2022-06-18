from app import *
from app import list_books
#from openpyxl import load_workbook
import random, copy

def sort(book_list,n):
    i=0
    my_list=book_list[:]
    print("************************\n")
    print("Here is the random list\n")
    while(i!=n):
        random_ch=random.choice(my_list)
        print(random_ch)
        my_list.remove(random_ch)        
        i+=1
    print("************************\n")
    

print("You want to:\n1. Import from Goodreads\n2. Enter manually")
x = int(input())

if x==1:
    print("Importing from Goodreads Owned Shelf")
    books, book_count = list_books.get_list()
    print("You have ",book_count," unread/owned books.\n")
    sort(books, int(input("How many random books do you want?: ")))
    while(input("Do you want to sort again? (Y/N)").lower() != 'n'):
        sort(books, int(input("How many random books do you want?: ")))

elif x==2:
    print("Enter the choices (enter x to exit):")
    books=[]
    ch='y'
    while(ch!='x'):
        ch=input("Book Title: ")
        if ch!='x':
            books.append(ch)
    print("Your list is:\n",books)
    sort(books,len(books))
    while(input("Do you want to sort again? (Y/N)").lower() != 'n'):
        sort(books,len(books))
