# Book_UI
# December, 10th, 2021
# Version 1.0


from Book_function import load_dataset
from Book_loaddata import load_dataset
from Book_Sorting import sort_books_title, sort_books_ascending_rate, sort_books_pageCount, sort_books_generes, sort_books_publisher
from Book_Search import get_book_by_category_and_author, get_books_by_category, find_books_by_title, all_categories_for_book_title
import csv

x = sort_books_publisher()
dictionary = ""
i = 0
j = 0
z = ''
while i < 20:
    z = input(" 1- Command Line L)oad file \n 2- Command Line A)dd book \n 3- Command Line R)emove book \n 4- Command Line F)ind book by title \n 5- Command Line NC) Number of books in a category \n 6- Command Line CA) Categories for an author \n 7- Command Line CB) Categories for a book title \n 8- Command Line G)et book \n     ZGR)ate   GA)uthor   GP)ublisher   GC)ategory \n    GCT) Category and Title    GCR) Category and Rate \n 9- Command Line S)ort book \n     ST)itle    SR)ate    SP)ublisher    SC)ategory    SPA)ageCount \n 10- Command line Q)uit \n")
    q = (z.upper()) 
    if q == "L":
                file = input("Please enter the file name: ")
                dictionary = load_dataset(file)
                print(dictionary)    
    if q == "G" and q != "":
        w = input("Enter another letter: GR for books rate, GA for books author, GP for books publisher, GC for books category, GCT for books category and title, GCR for category and rate, or Q to quit ") 
        e = (w.upper())
        j += 1
                   
        if e == "GR":
            r = input("Enter a rate ")
            for l in range(len(x)):
                y = x[l]
                if y["rating"] == r:
                    print(y)
                else:
                    print("No book was found to have that exact rating \n taking you back to the start now:")
                    break
                    
        if e == "GA":
            a = input("Enter a author ")
            for l in range(len(x)):
                y = x[l]
                if y["authors"] == a:
                    print(y)
                else:
                    print("No author was found under that name \n taking you back to the start now:")
                    break
                    
        if e == "GP":
            p = input("Enter a publisher ")
            for l in range(len(x)):
                y = x[l]
                if y["publisher"] == p:
                    print(y)
                else:
                    print("No publisher found under that name \n taking you back to the start now:")
                    break
                    
        if e == "GC":
            c = input("Enter a category ")
            for l in range(len(x)):
                y = x[l]
                if y["generes"] == c:
                    print(y)
                else:
                    print("No category found under that name \n taking you back to the start now:")
                    break
                    
        if e == "GCT":
            ct = input("Enter a category ")
            ct2 = input("Enter a title ")
            for l in range(len(x)):
                y = x[l]
                if y["generes"] == ct and y["title"] == ct2:
                    print(y)
                else:
                    print("No combination of that category and title found \n taking you back to the start now:")
                    break
                
        if e == "GCR":
            cr = input("Enter a category ")
            cr2 = input("Enter a rate ")
            for l in range(len(x)):
                y = x[l]
                if y["generes"] == cr and y["rating"] == cr2:
                    print(y)
                else:
                    print("No combination of that category and rating found \n taking you back to the start now:")
                    break
    
    if q == 'NC' and dictionary != "":
                                string = input("please enter the category to be searched: \n")
                                dictionary = input("please enter the book dictionary: \n")
                                update = get_books_by_category(string, dictionary)
                                print(update)
                                
    if q == 'CA'and dictionary != "":
                                string = input("please enter the genre to be searched: \n")
                                author1 = input("please enter an author to be searched in the genre: \n")
                                dictionary = input("please enter the book dictionary: \n")
                                dictionary1 = load_dataset(dictionary)
                                update = get_book_by_category_and_author(string, author1, dictionary1)
                                print(update)
                                
    if q == 'CB'and dictionary != "":
                                title = input("please enter the title to be searched")
                                dictionary = input("please enter the book dictionary: \n")
                                update = all_categories_for_book_title(title,dictionary)
                                print(update)
    if q == "S":
        q = input("Welcome to Sort: \n Please enter another command again \n ST - To sort by Title \n SR - To sort by Incresing Rate \n SP - To sort by Publisher \n SC - To sort by Category \n SPA - To sort by PageCount \n")
        
        if q == "ST":
            print("Thank you for selecting sort by title \n This will sort the google books by their title in alphabetical order \n ")
            commandtitle = sort_books_title("Google_Books_Dataset")
            printcommand = commandtitle
            print(printcommand)
                            
        if q == "SR":
            print("Thank you for selecting sort by rate \n This will sort the google books by ascending rate \n ")
            commandrate = sort_books_ascending_rate("Google_Books_Dataset")
            printcommand = commandrate
            print(printcommand)
                                
        if q == "SP":
            print("Thank you for selecting sort by publisher \n This will sort the google books by their publisher in alphabetical order \n ")
            commandpub = sort_books_publisher()
            printcommand = commandpub
            print(printcommand)
        
        if q == "SC":
            print("Thank you for selecting sort by category \n This will sort the google books by their genre \n ")
            commandgenre = sort_books_generes()
            printcommand = commandgenre
            print(printcommand)
                    
        if q == "SPA":
            print("Thank you for selecting sort by pagecount \n This will sort the google books by their pagecount in ascending rate \n ")
            commandpage = sort_books_pageCount("Google_Books_Dataset",'r')
            printcommand = commandpage
            print(printcommand)
            
        if q.upper() == "L":
            load_file_command = input("Please enter a file to load(ex. google_file)")
            if load_file_command == "Google_Books_Dataset.csv":
                print("Google_Books_Dataset.csv")
            elif load_file_command != "Google_Books_Dataset.csv":
                print("No file loaded")
        if q.upper() == "A":
                title = input("Enter a title(ex. Life of Pi):")
                author = input("Enter an author(ex. Yann Martel):")
                rating = input("Enter a rating between 0 and 5(ex. 3.9):")
                publisher = input("Enter a publisher(ex. Seal Books):")
                pagecount = input("Enter the pagecount(ex. 460):")
                generes = input("Enter the generes(ex. Fiction)")
                new_book = {"title": title,"authors": author,"rating": rating, "publisher": publisher, "pagecount": pagecount, "generes": generes}
                if new_book not in "Google_Books_Dataset.csv":
                    'Google_Books_Dataset'.csv.append(new_book)
                    print("Google_Books_Dataset.csv")
        if q.upper() == "R":
                title = input("Enter a title(ex. The Infinite Game):")
                author = input("Enter an author(ex. Simon Sinek):")
                rating = input("Enter a rating between 0 and 5(ex. 3.8):")
                publisher = input("Enter a publisher(ex. Penguin):")
                pagecount = input("Enter the pagecount(ex. 272):")
                generes = input("Enter the generes(ex. Business)")
                old_book = {"title": title,"authors": author,"rating": rating, "publisher": publisher, "pagecount": pagecount, "generes": generes}
                if old_book in "Google_Books_Dataset.csv":
                    'Google_Books_Dataset'.csv.remove(old_book)
                    print("Google_Books_Dataset.csv")
        if q.upper() == "F":
                title = input("Enter a title(ex. The Mysterious Affair at Styles):")
                for i in range(len("Google_Books_Dataset.csv")):
                    t = "Google_Books_Dataset.csv"[i]
                    if t["title"] == title:
                        print(t)
    if q != 'L' and q != 'A' and q != 'R' and q != 'F' and q != 'NC' and q != 'CA' and q != 'CB' and q != 'G' and q != 'GR' and q != 'GA' and q != 'GP' and q != 'GC' and q != 'GCT' and q != 'GCR' and q != 'S' and q != 'ST' and q != 'SR' and q != 'SP' and q != 'SC' and q != 'SPA' and q != 'Q':
        print("Invalid command please try again.\n")
    
    if q == "Q":
        i += 20                 
            
print("Thank you for running this code have a nice day")    



 
