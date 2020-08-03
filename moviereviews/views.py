from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
import requests

# Create your views here.
def reviews(request):
  queryResult = {}
  movies = {}

  if 'query' in request.GET:
    movie = request.GET['query']
    api_key = 'Lo21uGmevc2IHnOZGtA3KqDdTwc925Zb'
    url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=' + api_key 
    url += '&query=%s' % movie
    
    response = requests.get(url)
    queryResult = response.json()
    # print(queryResult['num_results'])
    count = 1
    while queryResult['has_more']:
      url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=' + api_key 
      url += '&query=%s' % movie
      url += '&offset=%s' % str(count * 20)
      count += 1
      response = requests.get(url)
      nextQueryResult = response.json()
      # if (nextQueryResult['num_results']):
      #   print(nextQueryResult['num_results'])
      # else:
      #   print("num_results not existent")

      try:
        queryResult['results'].extend(nextQueryResult['results'])
        # print(type(queryResult['results']))
        # print("nextQueryResult now %s" % str(len(nextQueryResult['results'])))
        # print("queryResult now %s" % str(len(queryResult['results'])))

      except:
        print("can't extend queryResult further. try to exit quietly, pretend nothing happened")
        break




    # print(len(queryResult['results']))
    movies = queryResult['results']
    # print(type(queryResult['results'][0]))
    # print(queryResult['results'][0]['display_title'])

    # title = movie['results'][0]['display_title']
    # review = movie['results'][0]['summary_short']

  return render(request, 'moviereviews/reviews.html', {'movies': movies } )
    
    
  #, 'title': title, 'review': review})




  # # url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=' + api_key 
  # r = requests.get(url)
  # json_data = r.json()
  # print(type(json_data))
  # print(json_data['status'] + str(len(json_data)))
  # print(type(json_data['results']))
  # for review in json_data['results']:
  #   print(review['display_title'] + " >> " + review['summary_short'])
  # # for byline in json_data:
  # #   print(byline['status'])
    
  # # return render(request, "moviereviews/reviews.html")
  # return JsonResponse(json_data)