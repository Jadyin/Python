# Book_Search
# December, 10th, 2021
# Version 1.0

import csv
import math
from optparse import Values


# Non-Functions
def book_rating_list() -> dict:
    with open("Google_Books_Dataset.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        rating_dictionary = {}
        for line in csv_reader:
            book = [
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            ]
            if rating_dictionary.get(line[3]) is not None:
                rating_dictionary[line[3]] += [book]
            else:
                rating_dictionary[line[3]] = [book]
                return rating_dictionary
x = book_rating_list()



def book_title_list() -> dict:
    with open("Google_Books_Dataset.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        title_dictionary = {}
        for line in csv_reader:
            book = [
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            ]
            if title_dictionary.get(line[1]) is not None:
                title_dictionary[line[1]] += [book]
            else:
                title_dictionary[line[1]] = [book]
                return title_dictionary 
        
y = book_title_list()


def book_author_list() -> dict:
    with open("Google_Books_Dataset.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        publisher_dictionary = {}
        for line in csv_reader:
            book = [
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            ]
            if publisher_dictionary.get(line[2]) is not None:
                publisher_dictionary[line[2]] += [book]
            else:
                publisher_dictionary[line[2]] = [book]
                return publisher_dictionary
        
n = book_author_list()





from csv import reader

def load_dataset(filename: str) -> dict:
            """
            Returns a dictionary containing book genres as keys and a list of
            dictionaries with other related information on the books in filename as
            values. 
            >>>book_category_dictionary_list(Google_Books_Dataset.csv)
            {"Fiction":[{"title":"Antiques Roadkill: A Trash 'n' TreasuresMystery",
            "authors":"Barbara Allan","language ":"English","rating":3.3,"publisher":
            "Kensington Publishing Corp.","pageCount":288},{another element},...]
            "Biography":[{"title":"The Nightshift Before Christmas:
            Festivehospitaldiaries from the author of million-copy hit","authors":
            "Adam Kay","language":"English","rating":4.7,"publisher":"Pan Macmillan",
            "pageCount":112},{another element}...],...}
            """
            infile = open('Google_Books_Dataset.csv')
            csvreader = reader(infile)
            header = next(csvreader)
            books = []
            for row in csvreader:
                books += [row]
            infile.close()
            book_dictionary = {}
            del header[0], header[-2]
            booklist = []
            for lists in books:
                genre = lists[-2]
                if genre != '':
                    del lists[-2], lists[0]
                    one_book = {}
                    if lists[2] == '':
                        lists[2] = 0
                    one_book.setdefault(header[0], lists[0])
                    one_book.setdefault(header[1], lists[1])
                    one_book.setdefault(header[5], lists[5])
                    one_book.setdefault(header[2], float(lists[2]))
                    one_book.setdefault(header[3], lists[3])
                    one_book.setdefault(header[4], int(lists[4]))
                    if one_book.get("generes") == 0:
                        one_book["generes"] = ''
                    if genre not in book_dictionary:
                        book_dictionary.setdefault(genre, (booklist + [one_book]))
                    else: 
                        book_dictionary[genre] = book_dictionary[genre] + [one_book]        
            return book_dictionary

book_dictionary = load_dataset('Google_Books_Dataset.csv')



def book_category_list() -> dict:
    with open("Google_Books_Dataset.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        rating_dictionary = {}
        for line in csv_reader:
            book = [
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            ]
            if rating_dictionary.get(line[6]) is not None:
                rating_dictionary[line[6]] += [book]
            else:
                rating_dictionary[line[6]] = [book]
                return rating_dictionary
        
o = book_category_list()


book_dict = dict()
with open('Google_Books_Dataset.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        data_dict = dict() 
        data_dict['title'] = row[1]     
        data_dict['authors'] = row[2]       
        data_dict['language'] = row[7]        
        data_dict['rating'] = (row[3])  
        data_dict['publisher'] = row[4]       
        data_dict['category'] = row[6]         
        data_dict['pageCount'] = int(row[5])  
        book_dict[int(row[0])] = data_dict 
        
z = book_dict


book_dict_author = dict()
with open('Google_Books_Dataset.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        data_dict_author = dict() 
        data_dict_author['title'] = row[1]     
        data_dict_author['authors'] = row[2]       
        data_dict_author['language'] = row[7]        
        data_dict_author['rating'] = (row[3])  
        data_dict_author['publisher'] = row[4]       
        data_dict_author['category'] = row[6]         
        data_dict_author['pageCount'] = int(row[5])  
        book_dict_author[int(row[0])] = data_dict_author 
        
u = book_dict_author

#Functions




def print_dictionary_category(category:str, booklist:dict)->int:
    """ Returns the number of elements associated with each category in the dictionary, the amount of books it contains and the list of said books.
    print_dictionary_category("Fiction", booklist)
    X,'The category "Fiction" has X books. This is the list of books in the category "Fiction":', {'Fiction': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': '4.8', 'Publisher': 'Hachette UK', 'pagecount': '96'}]
    """
    row[6] = category
    booklist = {row[6]:[{'title':row[1], 'author':row[2], 'language':row[7], 'rating':row[3], 'Publisher':row[4], 'pagecount':row[5]}]  for row in reader}    
    N_of_books = 0
    while row[6] == 'Fiction':
        N_of_books += 1
    print(N_of_books)


def add_book(bookdict:dict, book:tuple)->dict:
    """ Returns the updated dictionary of bookdict after a book has been added to it.
    add_book({}, (title, language, publisher, category, rating, pageCount))
    {'Book': ["Klara and the Sun","Kazuo Ishiguro" "English", "Alfred A. Knopf", "Science Fiction", "3.8", "303"]}
    """
    book = ("Klara and the Sun", "Kazuo Ishiguro", "English", "Alfred A. Knopf", "Science Fiction", "3.8", "303")
    if bookdict == {}:
        title,language,publisher,category,rating,pageCount = book
        bookdict.update({"Book":list(book)})
        print("The book has been added correctly")
    else:
        print("There was an error adding the book")

def remove_book(title:str, category:str, bookdict:dict)->dict:
    """ Returns an updated dictionary after the book is removed using the string values of its title and category.
    remove_book("Le Petit Prince", "Fiction", bookdict)
    {}
    """
    bookdict = {"Fiction":["Le Petit Prince", "Antoine de Saint-Exupery", "French","Harcourt, Inc","Fiction","4.3","96"]}
    book = bookdict.values()
    if book[0] == "Le Petit Prince":
        newdict = bookdict.pop("Fiction")
        print("This book has been removed correctly.")
    else:
        print("There was an error removing the book. Book not found.")
 
 
        
# No Docstring for this code, kept getting Syntax Error, no clue what from, what causes it or what to do about it 
# Syntax Error: (unicode error) 'utf-8' codec can't decode byte 0x94 in position 366: invalid start byte: C:\Users\jadyi\Desktop\T034_data_ananalyzer\T034_P2_search_modify_dataset.py, line 240, pos 1
def get_books_by_rate(rating: float,dictionary: dict) -> list:
        new_rating = [rating+0.1,rating+0.2,rating+0.3,rating+0.4,rating+0.5,rating+0.6,rating+0.7,rating+0.8,rating+0.,rating+1]
        list_of_new_dict = []
        title_list = []
        for rows in x:
            for newrating in new_rating:
                if str(newrating) == rows:
                    for book in x[str(rows)]:
                        if book not in title_list:
                            title_list.append(book)
                
        for i in range(len(title_list)):
            new_dict = [{"title": title_list[i][0],"authors": title_list[i][1],"rating": title_list[i][2], "publisher": title_list[i][3], "pagecount": title_list[i][4], "generes":title_list[i][5]}]
            list_of_new_dict.append(new_dict)
             
         
        return list_of_new_dict
     


def find_books_by_title (title: str,dictionary: dict) ->bool: 
    """
    >>>find_books_by_title("Antiques Roadkill: A Trash 'n' Treasures Mystery",x)
    True
    The book has been found 
    """
    for rows in y:
        if rows == title:
            if rows == title:
                print("The book has been found")
                return True
            elif rows != title: 
                print("The book has NOT been found")
                return False 

        
        

def get_books_by_author (name: str,dictionary: dict) ->list: 
            """
        >>>get_books_by_author("Agatha Christie",x)
        he author "Agatha Christie" has published the following books: 
        1-  The Red Signal: An Agatha Christie Short Story 
        2-  The Mysterious Affair at Styles 
        3-  And Then There Were None
        
        """
            title_books = []
            empty_title_list = []
            empty_list = []
            for rows in n:
                if name == rows:
                    for book in n[rows]:
                        if book not in empty_list:
                            empty_list.append(book)
                            for i in empty_list:
                                titles = [i[0]]
                                if titles not in empty_title_list:
                                    empty_title_list.append(titles)
         
            for i in range(len(empty_title_list)):
                titles_of_books = i,"-",empty_title_list[i]
                title_books.append(titles_of_books)
                
            compile_stuff = "The author",name," has published the following books:"
             
            return compile_stuff,title_books
              
        

def get_books_by_publisher(publisher: str, dictionary: dict) -> list:
            """
            Returns a list with the titles of the books published by the publisher,
            and prints the book information for that publisher in points.
            >>>get_books_by_publisher('Marvel Entertainment', book_dictionary))
            The publisher "Marvel Entertainment" has published the following books:
                    1- Deadpool Kills the Marvel Universe
                    2- Ultimate Spider-Man Vol. 11: Carnage
                    3- Immortal Hulk Vol. 1: Or Is He Both?
                    4- Venomized
                    5- Spider-Man: Anti-Venom
                    6- Spider-Verse: Volume 1
            ['Deadpool Kills the Marvel Universe', 'Ultimate Spider-Man Vol. 11: Carnage', 'Immortal Hulk Vol. 1: Or Is He Both?', 'Venomized', 'Spider-Man: Anti-Venom', 'Spider-Verse: Volume 1']
            """
            publisher_books = []
            print('The publisher "'+ publisher +'" has published the following books:')
            for key in dictionary:
                book1 = dictionary.get(key)
                for book2 in book1:
                    if book2.get("publisher") == publisher:
                        title = book2.get("title")
                        if title not in publisher_books:
                            publisher_books += [title]
            for x in range(len(publisher_books)):
                print("\t" + str(x + 1) + "- " + publisher_books[x])
            return publisher_books
        

def check_category_and_title(category: str, title: str, dictionary: dict)-> bool:
            """
            Returns True if the 'title' exists in the dictionary for the given 'category', otherwise, it returns False. And it prints a statement stating weather or not the 'category' has the 'title'.
            >>>check_category_and_title('Comics', 'Deadpool Kills the Marvel Universe', book_dictionary)
            The category  Comics  has the  book  title  Deadpool Kills the Marvel Universe
            True
            >>>check_category_and_title('Psychology', 'Deadpool Kills the Marvel Universe', book_dictionary)
            The category  Psychology  does not have the  book  title  Deadpool Kills the Marvel Universe
            False
            """
            for book81 in dictionary:
                book82 = dictionary.get(category)
                for outcomes in book82:
                    book81 = outcomes.get('title')
                    if book81 == title:
                        print("The category ", category," has the  book  title ", title)
                        return True
                    print("The category ", category," does not have the  book  title ", title)
                    return False
                        

                        
def all_categories_for_book_title(title: str, dictionary: dict)-> list:
    """
    Returns a list of all the categories for the given 'title', and prints the the title category information in points.
    all_categories_for_book_title('Sword of Destiny: Witcher 2: Tales of the Witcher', book_dictionary))
    The book title "Sword of Destiny: Witcher 2: Tales of the Witcher" has the following catergories:
    1 - Fiction
    2 - Adventure
    3 - Mythical Creatures
    ['Fiction', 'Adventure', 'Mythical Creatures']
    """
    category_list = []
    for category in dictionary:
        for i in dictionary[category]:
            if i['title'] == title:
                category_list += [category]
                print
                break
            print('The book title "', title, '" has the following catergories:', sep = '')
            for i in range(len(category_list)):
                print(i + 1, ' - ', category_list[i], sep = '')
                

        
        

def get_books_by_category(category: str, Dictonary: dict) -> list:
    Books_Category = []
    for rows in o:
        if category == rows:
            for book in o[rows]:
                Books_Category.append(book)
                Category_list = "The category",category," has the following books:"
                return Category_list,Books_Category

               
def get_book_by_category_and_rate(category: str, rating: str, dictonary: dict):
    '''
    '''
    book_list = list()
    for book in z:
        if z[book]['category'] == category and z[book]['rating'] == rating:
            book_list.append(z[book]['title'])
    print(f'The category "{category}" and rate {rating} has the following books:\n')
    for i, book in enumerate(book_list, 1):
        print(f'{i}- {book}')
    return book_list




def get_book_by_category_and_author(category: str, authors: str, dictonary: dict):
    '''
    '''
    book_list = list()
    for book in u:
        if u[book]['category'] == category and u[book]['authors'] == authors:
            book_list.append(u[book]['title'])
    print(f'The author "{authors}" has the following books in the category "{category}":\n')
    for i, book in enumerate(book_list, 1):
        print(f'{i}- {book}')
    return book_list
