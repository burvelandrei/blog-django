from django.shortcuts import render, get_object_or_404, redirect
from .models import Publication
from .forms import PublicationForm
from comment.models import Comment
from comment.forms import CommentForm


def index(request):
    publications = Publication.objects.all()
    return render(request, "publication/index.html", {"publications": publications})


def publication_detail(request, id):
    publication = get_object_or_404(Publication, id=id)
    comments = Comment.objects.filter(publication=id)
    comment_form = CommentForm()
    return render(
        request,
        "publication/publication_detail.html",
        {"publication": publication, "comments": comments, "form": comment_form},
    )

def add_publication(request):
    if request.method == "GET":
        publication_form = PublicationForm()
        return render(request, 'publication/add_publication.html', {'form': publication_form})
    elif request.method == 'POST':
        publication_form = PublicationForm(request.POST)
        if publication_form.is_valid():
            publication_form.save()
            return redirect('index')
        else:
            publication_form = PublicationForm()
        return render(request, 'publication/add_publication.html', {'form': publication_form})

def delete_publication(request, id):
    publication = Publication.objects.filter(id=id)
    publication.delete()
    return redirect("index")

def add_comment(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.publication = publication
            comment.save()
            return redirect('publication_detail', id=id)