from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid

class Genre(models.Model):
    name = models.CharField(max_length = 200, help_text = "Enter a game genre here:")
    
    def __str__(self):
        return self.name
class Game(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    summary = models.TextField(max_length = 1000, help_text = 'Enter a short description of the game.')
    isbn = models.CharField('ISBN', max_length = 13, help_text = "Enter 13-character ISBN number")
    genre = models.ManyToManyField(Genre, help_text = "Select a genre")
    language =  models.ForeignKey("Language", on_delete = models.SET_NULL, null = True)
    def display_genre(self):
        return ','.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = "Genre"
    def get_absolute_url(self):
        return reverse('game-detail', args = [str(self.id)])
    def __str__(self):
        return self.title
class GameInstance(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, help_text="Unique ID")
    game = models.ForeignKey('Game', on_delete = models.SET_NULL, null = True)
    creation = models.CharField(max_length = 100)
    due_back = models.DateField(null=True, blank = True)
    LOAN_STATUS = {
        ('A','Available'),
        ('X','Archived'),
        ('C','Cancelled'),
        ('N','Not created yet'),
    }
    status = models.CharField(max_length = 1, choices = LOAN_STATUS, blank=True, default = 'm', help_text = "Game aviability:")
    borrower = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set game as returned"),)
    def __str__(self):
        return ""+str(self.id)+" ("+str(self.game.title)+")"
class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    birth_date = models.DateField(null = True, blank = True)
    death_date = models.DateField("Died ", null = True, blank = True)
    class Meta:
        ordering = ['first_name', 'last_name']
    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
    def __str__(self):
        return ""+str(self.last_name)+", "+str(self.first_name)

class Language(models.Model):
    name = models.CharField(max_length = 50, help_text = "Enter original game language. Not programming one.")
    def __str__(self):
        return ""+str(self.name)

    # Create your models here.
