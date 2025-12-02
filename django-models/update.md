 update_title= Book.objects.get(title="We do hard things")
>>> update_title.title= "Anything for the soft life"
>>> update_title.save()
>>> print(f"{book1.title} just to get {update_title.title}")
We do hard things just to get Anything for the soft life
