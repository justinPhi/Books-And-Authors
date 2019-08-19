from django.db import models


class Books(models.Model):
    booksTitle = models.CharField(max_length=45)
    booksDescription = models.CharField(max_length=255)
    booksCreatedAt = models.DateTimeField(auto_now_add=True)
    booksCreatedAt = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    authFirstName = models.CharField(max_length=45)
    authLastName = models.CharField(max_length=45)
    authNotes = models.CharField(max_length=255)
    authCreatedAt = models.DateTimeField(auto_now_add=True)
    authUpdatedAt = models.DateTimeField(auto_now=True)
    authBooksManyCon = models.ManyToManyField(Books, related_name="publisher")



    
