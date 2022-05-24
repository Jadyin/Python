# Book_Search
# December, 10th, 2021
# Version 1.0

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
    infile = open(filename)
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
