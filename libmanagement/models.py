from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name  # Simplified, f-string not needed here

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('SCI', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('BIO', 'Biography'),
        ('HOR', 'Horror'),
        ('ROM', 'Romance'),
        ('THR', 'Thriller'),
        ('MYS', 'Mystery'),
    ]
    
    genre = models.CharField(
        max_length=3,
        choices=GENRE_CHOICES,
        default='FIC',  
    )
    
    def __str__(self):
        return self.title 

class BookLend(models.Model):  
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lend_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} returned {self.book} (Date: {self.return_date})" if self.is_returned else f"{self.student} borrowed {self.book} (Due: {self.return_date})"
