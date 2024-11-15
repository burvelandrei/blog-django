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
    is_author = publication.author == request.user
    return render(
        request,
        "publication/publication_detail.html",
        {
            "publication": publication,
            "comments": comments,
            "form": comment_form,
            "is_author": is_author,
        },
    )


def add_publication(request):
    if request.method == "GET":
        publication_form = PublicationForm()
        return render(
            request, "publication/add_publication.html", {"form": publication_form}
        )
    elif request.method == "POST":
        publication_form = PublicationForm(request.POST)
        if publication_form.is_valid():
            publication = publication_form.save(commit=False)
            publication.author = request.user
            publication.save()
            return redirect("index")
        else:
            publication_form = PublicationForm()
        return render(
            request, "publication/add_publication.html", {"form": publication_form}
        )


def edit_publication(request, id):
    publication = get_object_or_404(Publication, id=id)

    if request.method == "GET":
        publication_form = PublicationForm(instance=publication)
        return render(
            request, "publication/edit_publication.html", {"form": publication_form}
        )
    elif request.method == "POST":
        publication_form = PublicationForm(request.POST, instance=publication)
        if publication_form.is_valid():
            publication = publication_form.save(commit=False)
            if not publication.author_id:
                # Обработка ошибки, если автор не указан
                return render(
                    request,
                    "publication/edit_publication.html",
                    {"form": publication_form, "error_message": "Автор обязателен"}
                )
            publication.save()
            return redirect("index")
        return render(
            request, "publication/edit_publication.html", {"form": publication_form}
        )


def delete_publication(request, id):
    publication = Publication.objects.filter(id=id)
    publication.delete()
    return redirect("index")


def add_comment(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.publication = publication
            comment.author = request.user
            comment.save()
            return redirect("publication_detail", id=id)
