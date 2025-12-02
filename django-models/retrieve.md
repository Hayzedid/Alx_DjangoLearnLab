 retrieve_book1= Book.objects.get(published_year= 2025)
>>> print(f"{book1.title} 'at' {book1.author} 'in' {book1.published
_year}")
We do hard things 'at' ALX 'in' 2025
>>> print(f"{book1.title} at {book1.author} in {book1.published_yea
r}")
We do hard things at ALX in 2025
