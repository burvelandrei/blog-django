from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView, ListView, DetailView
from .models import Publication
from .forms import PublicationForm
from comment.models import Comment
from comment.forms import CommentForm


class PublicationListView(ListView):
    model = Publication
    template_name = 'publication/index.html'
    context_object_name = 'publications'


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication/publication_detail.html'
    context_object_name = 'publication'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publication = self.get_object()
        context['comments'] = Comment.objects.filter(publication=publication)
        context['form'] = CommentForm()
        context['author'] = publication.author
        context['is_author'] = publication.author == self.request.user
        return context


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


class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = "publication/index.html"
    success_url = '/'


def add_comment(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.publication = publication
            comment.author = request.user
            comment.save()
            return redirect("publication_detail", pk=id)
