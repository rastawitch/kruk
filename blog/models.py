from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	# z biblioteki models weź klasę Model (nazwy klas z dużej litery)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    #charfield to ciąg znaków
    text = models.TextField()
    #pole tekstowe - models., bo pobrane z biblioteki models
    created_date = models.DateTimeField(
            default=timezone.now)
    #timezone to biblioteka, now to funkcja
    published_date = models.DateTimeField(
            blank=True, null=True) #blank, żeby pole publish date było opcjonalne, null, żeby łatwo było znaleźć puste pola, czyli w blanki będzie wprowadzana wartość specyficzna null
    # powyżej atrybuty (Auhor, title, itd.)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        #bierze konkretny obiekt i ustawia w nim date publikacji, self.save - zachowa tą zmienną, self to domyślny parametr "ten obiekt, na rzecz którego to wywołujesz" self wskazuje na obiekt dla którego ma się wywołać

    def __str__(self):
        return self.title
        #str : co chemy wyświetlić, coś jak print ale dla obiektu