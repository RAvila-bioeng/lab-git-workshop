import pandas as pd
import leer


def get_new_book():
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    year=input("Enter the year of the book: ")
    genre=input("Enter the genre of the book: ")
    rating=input("Enter the rating of the book: ")
    pages=input("Enter the number of pages of the book: ")
    language=input("Enter the language of the book: ")
    country=input("Enter the country of the book: ")
    return title, author, year, genre, rating, pages, language, country


def add_book(df, title, author, year, genre, rating, pages, language, country):
    new_book=pd.DataFrame({'title': [title], 'author': [author], 'year': [year], 'genre': [genre], 'rating': [rating], 'pages': [pages], 'language': [language], 'country': [country]})
    df=pd.concat([df, new_book], ignore_index=True)
    return df

if __name__ == "__main__":
    df = leer.leer_datos('data/books.csv')
    new_title, new_author, new_year, new_genre, new_rating, new_pages, new_language, new_country = get_new_book()
    df = add_book(df, new_title, new_author, new_year, new_genre, new_rating, new_pages, new_language, new_country )
    df.to_csv('data/books.csv', index=False)
    print("Book added successfully")