from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def reverse(request):
    text = (request.GET['usertext'])
    reveres_text = text[::-1]
    return render(request, 'reverse.html', {'end_text': reveres_text, 'original_text': text})