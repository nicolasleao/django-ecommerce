from django.shortcuts import render
from allauth.account.forms import LoginForm

# Create your views here.
def StoreLanding(request):
	context = {
		'form': LoginForm(),
		'categories': ['Camisetas', 'Camisas', 'Calças', 'Jaquetas'],

		'top_sellers': [{'name': 'Camiseta branca', 'price': 45.0},
						{'name': 'Camiseta preta', 'price': 50.0},
						{'name': 'Camiseta azul', 'price': 45.0},
						{'name': 'Jeans desbotada', 'price': 70.0}],

		'best_reviews': [{'name': 'Camiseta branca', 'price': 45.0},
						{'name': 'Camiseta preta', 'price': 50.0},
						{'name': 'Jaqueta preta', 'price': 130.0},
						{'name': 'Jaqueta azul', 'price': 45.0}],
	}
	return render (request, 'store/store.html', context)

def StoreSearch(request, category_id=''):
	query = request.GET.get('q')
	context = {
		'form': LoginForm(),
		'categories': ['Camisetas', 'Camisas', 'Calças', 'Jaquetas'],
		'current_category': {'name': '', 'id':'13141231'},
		'query': query,
		'results': [{'name': 'Camiseta branca', 'price': 45.0},
						{'name': 'Camiseta preta', 'price': 50.0},
						{'name': 'Camiseta azul', 'price': 45.0},
						{'name': 'Camiseta preta', 'price': 50.0},
						{'name': 'Camiseta azul', 'price': 45.0},
						{'name': 'Jeans desbotada', 'price': 70.0}],
	}
	return render (request, 'store/search.html', context)