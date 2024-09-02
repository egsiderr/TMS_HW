from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from TMS_HW.HM15.create_db import Author, Book, Sale

engine = create_engine("sqlite:///db.sqlite", echo=True)

session_pool = sessionmaker(bind=engine)
session = session_pool()

authors = [
    Author(firstname="Biba", lastname="Bibov"),
    Author(firstname="Boba", lastname="Bobov"),
    Author(firstname="Optimus", lastname="Prime")
]

session.add_all(authors)
session.commit()

books = [
    Book(title="Meow", author_id=1, publication_year=2022),
    Book(title="Gav", author_id=2, publication_year=2012),
    Book(title="Transformation", author_id=3, publication_year=2016)
]

session.add_all(books)
session.commit()

sales = [
    Sale(book_id=1, quantity=345),
    Sale(book_id=2, quantity=234),
    Sale(book_id=3, quantity=228)
]

session.add_all(sales)
session.commit()

# inner_join_query = session.query(Book.title, 
#     Author.firstname, 
#     Author.lastname).join(Author).all()
# print(inner_join_query)

# left_join_query = session.query(
#     Author.firstname, 
#     Author.lastname, 
#     Book.title).outerjoin(Book, Author.id == Book.author_id).all()
# print(left_join_query)

# inner_join_all_query = session.query(
#     Book.title, 
#     Author.firstname, 
#     Author.lastname, 
#     Sale.quantity).join(Author).join(Sale).all()
# print(inner_join_all_query)

# left_join_all_query = session.query(
#     Author.firstname, 
#     Author.lastname, 
#     Book.title, 
#     Sale.quantity).outerjoin(Book, Author.id == Book.author_id).outerjoin(Sale, Book.id == Sale.book_id).all()
# print(left_join_all_query)