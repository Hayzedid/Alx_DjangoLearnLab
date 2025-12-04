 delete_book1= Book.objects.get(title="Anything for the soft lif
e")
>>> delete_book1.delete()
(1, {'bookshelf.Book': 1})
