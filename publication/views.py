from django.shortcuts import render, get_object_or_404
from .models import Publication


def index(request):
    publications = Publication.objects.all()
    return render(request, "publication/index.html", {"publications": publications})


def publication_detail(request, id):
    publication = get_object_or_404(Publication, id=id)
    return render(
        request, "publication/publication_detail.html", {"publication": publication}
    )
