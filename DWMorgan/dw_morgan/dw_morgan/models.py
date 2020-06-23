from django.db import models

class CovidObservations(models.Model):
	sno = models.IntegerField(primary_key=True, )
	observation_date = models.DateField()
	province_state = models.CharField(max_length=255)
	country_region = models.CharField(max_length=255)
	last_update = models.DateTimeField()
	confirmed = models.IntegerField()
	deaths = models.IntegerField()
	recovered = models.IntegerField()

	class Meta:
		db_table = 'covid_observations'