import os, click
from flask import cli
from flask.cli import AppGroup
import requests

blueprint = AppGroup('google')

@blueprint.command("search")
@click.argument('book_name')
def create(book_name):
  """Use the Google Books API to search for a book title, author, etc."""
  data = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_name}').json()['items'][:5]
  try:
    # print(data)
    book_list = []
    for book in data:
      # print(book['id'])
      # print(book['volumeInfo']['authors'])
      # print(book['volumeInfo']['title'])
      # print(book['volumeInfo']['publisher'])
      # break
      new_book = {
        'id': book['id'],
        'title': book['volumeInfo']['title']
      }
      # print(new_book)
      if book['volumeInfo'].get('publisher'):
        new_book.update(publisher=book['volumeInfo']['publisher'])
      if book['volumeInfo'].get('authors'):
        new_book.update(authors=book['volumeInfo']['authors'])
      book_list.append(new_book)
    
    done = False
    while not done:
      print([{ 'id': b['id'], 'title': b['title'] } for b in book_list])
      input("Here are your list of books. Press any key to continue")
      done = True
  except Exception as error:
    print(f"Something went wrong with creating the blueprint")
    print(error)
  return print("Blueprint created successfully")