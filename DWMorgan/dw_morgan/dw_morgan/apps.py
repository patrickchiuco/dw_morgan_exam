from django.apps import AppConfig
import csv, os
from datetime import datetime
import pytz
from django.db.utils import ProgrammingError

def date_time_parser(date_string):
    try:
        return_value = datetime.strptime(date_string, '%m/%d/%Y %H:%M')
    except:
        try:
            return_value = datetime.strptime(date_string, '%m/%d/%y %H:%M')
        except:
            try: 
                return_value = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
            except:
                try:
                    return_value = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    print('Invalid date format obtained.')
    return pytz.utc.localize(return_value)


class DWMorganConfig(AppConfig):
    name = 'dw_morgan.apps'
    verbose_name = "DW Morgan"

    def ready(self):
        from dw_morgan.models import CovidObservations
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../files/covid_19_data.csv")
        if not CovidObservations.objects.count():
            with open(path) as covid_observations:
                print('Loading dataset...')
                observations = csv.reader(covid_observations, delimiter=',')
                next(observations)
                instances = [
                    
                    CovidObservations(
                        sno=observation[0],
                        observation_date=datetime.strptime(observation[1], '%m/%d/%Y').date(),
                        province_state=observation[2],
                        country_region=observation[3],
                        last_update=date_time_parser(observation[4]),
                        confirmed=observation[5],
                        deaths=observation[6],
                        recovered=observation[7]
                    )
                    for observation in observations
                ]
                
                CovidObservations.objects.bulk_create(instances)

            

