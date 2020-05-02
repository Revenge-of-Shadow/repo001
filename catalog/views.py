from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import Game, Author, GameInstance, Genre
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

# from .forms import RenewBookForm

from .forms import RenewGameForm

def index(request):
    num_games = Game.objects.all().count()
    num_instance = GameInstance.objects.all().count()
    num_instances_available = GameInstance.objects.filter(status='a').count()
    num_author = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    return render(
        request,
        'index.html',
        context = {'num_games':num_games,
               'num_instances':num_instance,
               'num_instances_available':num_instances_available, 
               'num_authors':num_author, 
               'num_visits':num_visits},)
def page1(request):
    return render(request, "page1.html")
def page2(request):
    return render(request, "page2.html")
def stolen_page1(request):
    return render(request, "stolen_page1.html")
def stolen_page2(request):
    return render(request, "stolen_page2.html")
# Create your views here.
class GameListView(generic.ListView):
    model = Game
    paginate_by = 10
    #context_object_name = "my game list"
    #queryset = Game.objects.filter(title__icontains='')[:5]
    #template_name = "games/my_arbitrary_template_name_list.html"
class GameDetailView(generic.DetailView):
    model = Game



class AuthorListView(generic.ListView):
    model = Author
    #context_object_name = "my author list"
    paginate_by = 10
    #template_name = "authors/my_arbitrary_template_name_list.html"
class AuthorDetailView(generic.DetailView):
    model = Author
class LoanedGamesByUserListView(LoginRequiredMixin, generic.ListView):
    model = GameInstance
    template_name = 'catalog/gameinstance_list_borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return GameInstance.objects.filter(borrower = self.request.user).filter(status__exact = 'o').order_by('due_back')
class View(generic.TemplateView):
    template_name = 'catalog/art.html'
class LoanedGamesAllListView(PermissionRequiredMixin, generic.ListView):
    model = GameInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/gameinstance_list_borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return GameInstance.objects.filter(status__exact='o').order_by('due_back')



@permission_required("catalog.can_mark_returned")
def renew_game_librarian(request, pk):
    game_instance = get_object_or_404(GameInstance, pk = pk)
    if request.method == "POST":
        form = RenewGameForm(request.POST)
        if form.is_valid():
            game_instance.due_back = form.cleaned_data["renewal_date"]
            book_instance.save()

            return HttpResponseRedirect(reverse("all-borrowed"))

        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks = 3)
            form = RenewGameForm(initial = {"renewal":proposed_renewal_date,})

        context = {
        'form': form,
        'game_instance': game_instance,
        }
        return render(request, "catalog/game_renew_librarian.html", {"form":form, "gameinst":game_inst})
class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}
    permission_required = 'catalog.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'catalog.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'


# Classes created for the forms challenge
class GameCreate(PermissionRequiredMixin, CreateView):
    model = Game
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class GameUpdate(PermissionRequiredMixin, UpdateView):
    model = Game
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class GameDelete(PermissionRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('games')
    permission_required = 'catalog.can_mark_returned'
