from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///db.sqlite", echo=True)

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"Authors(id={self.id}, firstname={self.firstname}, lastname={self.lastname})"
    
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    publication_year = Column(String)
    author = relationship("Author", back_populates="books")
    sales = relationship("Sale", back_populates="book")

    def __repr__(self):
        return f"Books(id={self.id}, title={self.title}, author_id={self.author_id}, publication_year={self.publication_year})"

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True) 
    book_id = Column(Integer, ForeignKey("books.id"))
    quantity = Column(Integer)
    book = relationship("Book", back_populates="sales")

    def __repr__(self):
        return f"Sales(id={self.id}, book_id={self.book_id}, quantity={self.quantity})"

metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)

