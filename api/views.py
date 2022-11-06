from django.http import HttpResponse

from django.shortcuts import render


def test_home(request):
    text = """<h1>Testing</h1>"""
    return HttpResponse(text, content_type='text/html')
