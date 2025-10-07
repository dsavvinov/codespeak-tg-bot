from django.shortcuts import render


def hello_world(request):
    """Display the HelloWorld greeting page."""
    return render(request, 'django_app/hello_world.html')
