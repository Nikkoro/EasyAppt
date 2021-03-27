from django.db import models

# Create your models here.


SERVICES = (
	('Haircut with clippers 10$','Haircut with clippers 10$'),
	('Haircut with clippers & scissors 15$','Haircut with clippers & scissors 15$'),
	('Haircut and beard combo 25$','Haircut and beard combo 25$'),
	('Beard 5$','Beard 5$'),
	('Haircut & eyebrows 15$','Haircut & eyebrows 15$'),
	('Dying gray hair 25$','Dying gray hair 25$'),


	)

BARBERS = (
	('First Available','First Available'),
	('Keith Apelon','Keith Apelon'),
	('Frank Swan','Frank Swan'),
	('Dario Tequila','Dario Tequila'),
	)



class MyModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    service = models.CharField(max_length=200, choices=SERVICES)
    barber = models.CharField(max_length=200, choices=BARBERS)

    def __str__(self):
        return 'Appointment: {}/{} on {} at {} {} {}'.format(self.username, self.email, self.date, self.time, self.service, self.barber)

