from dw_morgan.models import CovidObservations
from django.http import JsonResponse
from datetime import datetime

def get_top_confirmed(request):
	if request.GET is not None:
		max_results = int(request.GET.get('max_results')) or None
		observation_date = request.GET.get('observation_date') or None
		response = {
			'obsvervation_date': observation_date,
			'countries': [
			]
		}
		if max_results:
			observations = CovidObservations.objects.filter(
				observation_date=datetime.strptime(observation_date, '%Y-%m-%d').date()
			).order_by('deaths', 'country_region')[:max_results]
			response['countries'] = [
					{
						"country": observation.country_region,
						"confirmed": observation.confirmed,
						"deaths": observation.deaths,
						"recovered": observation.recovered
					}
					for observation in observations
			]
		return JsonResponse(data=response, status=200)
	else:
		return JsonResponse(data={'Error': 'Please supply query parameters.'}, status=200)
		