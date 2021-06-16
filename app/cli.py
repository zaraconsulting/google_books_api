import os, click
from flask import cli
from flask.cli import AppGroup
import requests
from app.blueprints.main.models import Book, Author
from app import db

blueprint = AppGroup('google')

@blueprint.command("search")
@click.argument('book_name')
def create(book_name):
  """Use the Google Books API to search for a book title, author, etc."""
  data = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_name}').json()['items'][:5]
  try:
    book_list = []
    selection_id = 0
    for book in data:
      selection_id+=1
      new_book = {
        'selection_id': selection_id,
        'id': book['id'],
        'title': book['volumeInfo']['title']
      }
      if book['volumeInfo'].get('publisher'):
        new_book.update(publisher=book['volumeInfo']['publisher'])
      if book['volumeInfo'].get('authors'):
        new_book.update(authors=book['volumeInfo']['authors'])
      book_list.append(new_book)
    
    possible_choices = list(range(1, 6))
    done = False
    while not done:
      for idx, book in enumerate(Book.query.all()):
        print(f'{idx+1}: [{book.book_id}] {book.title}')
      
      print('='*40)
      option = input("Here is your current shortlist. Press any key to continue, or type 'quit' to exit program. ").lower()
      if option == 'quit':
        break
      for idx, book in enumerate(book_list):
        print(f"{idx+1}: [{book['id']}] {book['title']} by {book['authors']}")
      choice = int(input("\nHere are your list of books. Type one of options 1-5 to select a book to add to your shortlist. \n"))
      if choice in possible_choices:
        for i in book_list:
          if choice == i['selection_id']:
            b = Book(book_id=i['id'], title=i['title'], publisher=i['publisher'])
            db.session.add(b)
            for n in i['authors']:
              a = Author(name=n, book_id=i['id'])
              db.session.add(a)
        db.session.commit()
  except Exception as error:
    print(f"Something went wrong with creating the blueprint")
    print(error)
  return print("Application Exited")