from django.shortcuts import render
import datetime


def home(request):
    value = {'num': 10, 'paragraph': "T'his is a paragraph",
             'name': 'ashik', 'title': 'Django with web devlopment',
             'Birthday': datetime.datetime.now(), 'empty': '', 'file': 256897, 'yourList': ['Ashik', 'Ahnaf', 'Nishat'], 'line': 'one', 'list': [
                 {'name': 'Josh', 'age': 19},
                 {'name': 'Dave', 'age': 22},
                 {'name': 'Joe', 'age': 31},
                 {'name': 'Ashik', 'age': 35},
             ], 'name2': 'ASHIK', 'makelist': 'ashik ahnaf nishat josh dave', 'randomnum': ['a', 'b', 'c'],
             'blog': 'lorem ipsum dolor sit amet consectetur adipisicing elit'}
    return render(request, 'app.html', value)
