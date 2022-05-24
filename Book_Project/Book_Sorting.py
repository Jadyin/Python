# Book_Sorting
# December, 10th, 2021
# Version 1.0

import csv
from csv import reader


# Sorting the CSV file 
file = open("Google_Books_Dataset.csv",'r')
reader = csv.reader(file)
header = next(reader)

books = []

# Function to_list
with open("Google_Books_Dataset.csv") as file:
    new_book = csv.reader(file)
    header = next(new_book)
    for row in new_book:
        new_dic = {}
        new_dic['title'] = row[1]
        new_dic['author'] = row[2]
        new_dic['rating'] = row[3]
        new_dic['publisher'] = row[4]
        new_dic['genres'] = row[5]
        new_dic['language'] = row[6]

        books.append(new_dic)



def sort_books_title (google_book:dict)->list:
    """ Returns a list with the the book data stored in google_book is sorted alphabetically by title.
    """
    book = []
    for line in reader:
        lst = [line[1], line[2], line[3], line[4], line[5], line[6]]
    book.append(lst)
    length = len(book)
    for i in range(length):
        bookdict = {"title": book[i][0],"authors": book[i][1],"rating": book[i][2], "publisher": book[i][3], "pagecount": book[i][4], "generes": book[i][5]}
    booklist = list(bookdict)
    n = len(booklist)
    for i in range(n):
        for j in range(0, n-i-1):
            if booklist[j][0] > booklist[j+1][0]:
                booklist[j], booklist[j+1] = booklist[j+1], booklist[j]
    return booklist    



def sort_books_ascending_rate(Google_book: dict) -> dict:
    """
    Takes the Google Book List or any dict value that books 
    has been assigned to and then sorts them in acending order 
    of the assinged rating 
    
    
    
    
    
    """
    for i in range(len(books) - 1):
        for j in range(len(books) - 1):
            if books[j]['rating'] > books[j+1]['rating']:
                temp = books[j]
                books[j] = books[j+1]
                books[j+1] = temp

    for i in range(len(books)):
        for key, value in books[i].items():
            print(key + ": " + str(value))
        
    return books


def sort_books_descending_rate(Google_book: dict) -> dict:
    """
    Takes the Google Book List or any dict value that books 
    has been assigned to and then sorts them in decending order 
    of the assigned rating 
    
    
    
    
    
    """
    for i in range(len(books) - 1):
        for j in range(len(books) - 1):
            if books[j]['rating'] < books[j+1]['rating']:
                temp = books[j]
                books[j] = books[j+1]
                books[j+1] = temp

    for i in range(len(books)):
        for key, value in books[i].items():
            print(key + ": " + str(value))
        

    return books


def sort_books_publisher() -> dict:
 with open("Google_Books_Dataset.csv", "r") as file:
  csv_reader = csv.reader(file)
  header = next(csv_reader) 
  unsorted_list = []
  sorted_list = []
  for line in csv_reader:
    book = [
    line[1],
    line[2],
    line[3],
    line[4],
    line[5],
    line[6],
    ]
    unsorted_list.append(book)
  
  length = len(unsorted_list)
  for i in range(length-1):
   Book_list = {"title": unsorted_list[i][0],"authors": unsorted_list[i][1],"rating": unsorted_list[i][2], "publisher": unsorted_list[i][3], "pagecount": unsorted_list[i][4], "generes":unsorted_list[i][5]}
   sorted_list.append(Book_list)
    
  n = len(sorted_list)
  for i in range(n):
   for j in range(0, n-i-1):
    if sorted_list[j]["publisher"] > sorted_list[j+1]["publisher"]:
     sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
     
    if sorted_list[j]["publisher"] == sorted_list[j+1]["publisher"]:
     if sorted_list[j]["title"] > sorted_list[j+1]["title"]:
      sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
  
  return sorted_list



def sort_books_pageCount(dic: dict)-> list:
    """
    Returns a list with the book data stored as a dictionary book where the books are sorted by page count in ascending order. If two books have the same page count, it sorts them alphabetically according to the title.
    """
    var1 = []
    title = []
    for key in dic:
        var2 = dic[key]
        for data in var2:
            title1 = data.get('title')
            if title1 not in title:
                title += [title1]
                data.setdefault('genre', key)
                var1 += [data]
            else:
                for sametitle in var1:
                    if sametitle.get('title') == title and key not in sametitle["genre"]:
                        sametitle["genre"] = sametitle["genre"] + ", " + key
    n = len(var1)
    for i in range(n):
        for j in range(0, n-i-1):
            if var1[j].get('page_count') > var1[j+1].get('page_count'):
                var1[j], var1[j+1] = var1[j+1], var1[j]
            elif var1[j].get('page_count') == var1[j+1].get('page_count'):
                if var1[j].get('title') > var1[j+1].get('title'):
                    var1[j], var1[j+1] = var1[j+1], var1[j]
    for u in var1:
        print(u, sep='\t')

    return var1


def sort_books_generes() -> dict:
    with open("Google_Books_Dataset.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        unsorted_list = []
        sorted_list = []
        for line in csv_reader:
            book = [
                line[1],
                line[2],
                line[3],
                line[4],
                line[5],
                line[6],
            ]
            unsorted_list.append(book)
            length = len(unsorted_list)
            
            
            for i in range(length-1):
                Book_list = {"title": unsorted_list[i][0],"authors": unsorted_list[i][1],"rating": unsorted_list[i][2], "publisher": unsorted_list[i][3], "pagecount": unsorted_list[i][4], "generes":unsorted_list[i][5]}
                sorted_list.append(Book_list)
                
                
                n = len(sorted_list)
                for i in range(n):
                    for j in range(0, n-i-1):
                        if sorted_list[j]["generes"] > sorted_list[j+1]["generes"]:
                            sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                            
                            
                            
                            
                            if sorted_list[j]["generes"] == sorted_list[j+1]["generes"]:
                                if sorted_list[j]["title"] > sorted_list[j+1]["title"]:
                                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                                    
                                    
                                    return sorted_list