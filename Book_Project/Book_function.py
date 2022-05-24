# Book_Function
# December, 10th, 2021
# Version 1.0
import csv 


def book_dictionary_publisher_list(filename:str)->dict:     
    file = open(filename, mode = 'r')
    reader = csv.reader(file)
    header = next(reader)  
    publisher_list = {rows[4]:[{'title':rows[1], 'author':rows[2], 'language':rows[7], 'rating':rows[3], 'category':rows[6], 'pagecount':rows[5]}]for rows in reader}
    
    return publisher_list

bookFile = open("Google_Books_Dataset.csv")
Booklist = csv.reader(bookFile)



def book_category_dictionary_list(google_book:dict)->dict:
    """ Returns a dictionary of the stored data with the keys being the different genres found in the data set. 
    >>> 
    >>>
    """
    my_file =open(google_book, mode = 'r')
    x = csv.reader(my_file)
    next(x)
    booklist = {rows[6]:[{'title':rows[1], 'author':rows[2], 'rating':rows[3], 'publisher':rows[4], 'pagecount':rows[5], 'languge':rows[7]}]for rows in x}
    print(booklist)

bookFile = open("Google_Books_Dataset.csv",)
Booklist = csv.reader(bookFile)



def book_list_dictionary(Google_Books_Dataset: dict) -> list:
    """
    The function takes the dictionary information given to it
    in the form of the bookFile and unpacks it and then repacks it into 
    a list format, while keeping the information the same 
    
    book_list("Google_Books_Dataset.csv")
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'authors': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page_count': '288', 'generes': 'Fiction', 'language': 'English\n'}]
    
    
    """
    for Bookinfo in bookFile:
        #title, author, rating, publisher, page_count, generes, language = Bookinfo
        Book_Temp_List = Bookinfo.split(",")
        bookDict = [{"title":Book_Temp_List[1] , "authors": Book_Temp_List[2], "rating": Book_Temp_List[3], "publisher": Book_Temp_List[4], "page_count": Book_Temp_List[5], "generes": Book_Temp_List[6], "language":Book_Temp_List[7]}]
        print(bookDict)
    
my_file = open("Google_Books_Dataset.csv","r")
x = csv.reader(my_file)



def book_tuple_dictionary(Google_Books_Dataset: dict) -> tuple:
    """
    >>>book_tuple_dictionary(Google_Books_Dataset.csv)
    ({"title":"Antiques Roadkill: A Trash 'n' Treasures Mystery",
    "authors": " Barbara Allan",
    "language ": "English",
    "rating": 3.3,
    "publisher": " Kensington Publishing Corp.",
    "category": " Fiction",
    "pageCount": 288})
    {another element}
    """
    book_tuple = tuple()
    my_file =open(Google_Books_Dataset, mode = 'r')
    x = csv.reader(my_file)
    next(x)
    for row in x:
        Bookinfo = dict()
        Bookinfo['title'] = row[1]
        Bookinfo['authors'] = row[2]
        Bookinfo['title'] = row[3]
        Bookinfo['title'] = row[4]
        Bookinfo['title'] = row[5]
        Bookinfo['title'] = row[6]
        Bookinfo['title'] = row[7]
        
        book_tuple += (Bookinfo,)
        
    return book_tuple


x = book_tuple_dictionary("Google_Books_Dataset.csv")
print(x)