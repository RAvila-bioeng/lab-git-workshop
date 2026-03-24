import pandas as pd
import leer


def find_author():
    author = input("Write the author you are interested in: ")
    return author


def find_title():
    title = input("Write the title you want to search: ")
    return title


def find_year():
    year = int(input("Write the year the target book was written in: "))
    exact = input("Do you want books from that exact year? YES/NO: ").strip().upper()

    while exact not in ["YES", "NO"]:
        exact = input("Please write YES or NO: ").strip().upper()

    if exact == "YES":
        return year, "EXACT"

    higher = input("Do you want to find more recent books? YES/NO: ").strip().upper()

    while higher not in ["YES", "NO"]:
        higher = input("Please write YES or NO: ").strip().upper()

    if higher == "YES":
        return year, "HIGHER"
    else:
        return year, "LOWER"


def find_book(df):
    criterio = input("What criteria do you want to use? Year / Title / Author: ").strip().capitalize()

    while criterio not in ["Year", "Title", "Author"]:
        criterio = input("Please choose Year, Title or Author: ").strip().capitalize()

    if criterio == "Year":
        year, mode = find_year()

        if mode == "EXACT":
            result = df[df["year"] == year]
        elif mode == "HIGHER":
            result = df[df["year"] > year]
        else:
            result = df[df["year"] < year]

    elif criterio == "Title":
        title = find_title()
        result = df[df["title"].str.contains(title, case=False, na=False)]

    elif criterio == "Author":
        author = find_author()
        result = df[df["author"].str.contains(author, case=False, na=False)]

    return result


# Example of use
df = leer.leer_datos("data/books.csv")
resultado = find_book(df)
print(resultado)