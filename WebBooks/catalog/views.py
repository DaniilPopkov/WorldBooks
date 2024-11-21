from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import * 
from .forms import AuthorsForm 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from .models import Book 
from .forms import UserForm
from django.shortcuts import redirect

# Create your views here.
 


def index(request):
#  # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
 # Доступные книги (статус = 'На складе')
 # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
 # Авторы книг,
    num_authors = Author.objects.count()
# Количество посещений этого view, подсчитанное 
# в переменной session 
    num_visits = request.session.get('num_visits', 0) 
    request.session['num_visits'] = num_visits + 1 
 # Отрисовка HTML-шаблона index.html с данными
 # внутри переменной context
    return render(request, 'index.html', context={
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_visits': num_visits})
class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
class BookDetailView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView): 
   model = Author 
   paginate_by = 4   
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView): 
   """ 
   Универсальный класс представления списка книг, 
   находящихся в заказе у текущего пользователя. 
   """ 
   model = BookInstance 
   template_name = 'catalog/bookinstance_list_borrowed_user.html' 
   paginate_by = 10 
def get_queryset(self):
      return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
# получение данных из БД и загрузка шаблона authors_add.html 
def authors_add(request): 
   author = Author.objects.all() 
   authorsform = AuthorsForm() 
   return render(request, "catalog/authors_add.html", 
      {"form": authorsform, "author": author})
def create(request): 
   if request.method == "POST": 
      author = Author() 
      author.first_name = request.POST.get("first_name") 
      author.last_name = request.POST.get("last_name") 
      author.date_of_birth = request.POST.get("date_of_birth") 
      author.date_of_death = request.POST.get("date_of_death") 
      author.save() 
      return HttpResponseRedirect("/authors_add/")
# удаление авторов из БД 
def delete(request, id): 
   try: 
      author = Author.objects.get(id=id) 
      author.delete() 
      return HttpResponseRedirect("/authors_add/") 
   except Author.DoesNotExist: 
      return HttpResponseNotFound("<h2>Автор не найден</h2>") 
# изменение данных в БД 
def edit1(request, id): 
   author = Author.objects.get(id=id) 
   if request.method == "POST": 
      author.first_name = request.POST.get("first_name") 
      author.last_name = request.POST.get("last_name") 
      author.date_of_birth = request.POST.get("date_of_birth") 
      author.date_of_death = request.POST.get("date_of_death") 
      author.save() 
      return HttpResponseRedirect("/authors_add/") 
   else: 
      return render(request, "edit1.html", {"author": author})

class BookCreate(CreateView): 
   model = Book 
   fields = '__all__' 
   success_url = reverse_lazy('books') 
class BookUpdate(UpdateView): 
   model = Book 
   fields = '__all__' 
   success_url = reverse_lazy('books') 
class BookDelete(DeleteView): 
   model = Book 
   success_url = reverse_lazy('books')
# Boot_start
def boot_start_page(request):
   return render(request, "start1.html")
def boot_start_page1(request):
   return render(request, "color_bg.html")
def boot_start_page2(request):
   return render(request, "color_text.html")
def boot_start_page3(request):
   return render(request, "color_text_bg.html")
def space_start_page(request):
   return render(request, "space_1.html")
def space_start_page1(request):
   return render(request, "space_2.html")
def space_start_page2(request):
   return render(request, "space_3.html")
def aligment_start_page(request):
   return render(request, "aligment_1.html")
def aligment_start_page1(request):
   return render(request, "aligment_2.html")
def border_start_page(request):
   return render(request, "border_1.html")
def border_start_page1(request):
   return render(request, "border_2.html")
def border_color_page(request):
   return render(request, "border_color.html")
def border_radius_page(request):
   return render(request, "border_radius.html")
def border_radius_page1(request):
   return render(request, "border_radius_1.html")
def start_start_page(request):
   return render(request, "start.html")
def start_start_page1(request):
   return render(request, "start_1.html")
def table_start_page(request):
   return render(request, "table.html")
def table_start_page1(request):
   return render(request, "table_1.html")

# end
# def index(request): 
#    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->', 'IV квартал->'] 
#    my_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'] 
#    context = {'my_month': my_month, 'my_kv': my_kv} 
#    return render(request, "firstapp/index.html", context)
def index(request): 
   my_text = 'Изучаем формы Django' 
   context = {'my_text': my_text} 
   return render(request, "firstapp/index.html", context) 
def about(request): 
   return render(request, "firstapp/about.html") 
def contact(request): 
   return render(request, "firstapp/contact.html") 
def my_form(request): 
   if request.method == "POST": 
      userform = UserForm(request.POST) 
      if userform.is_valid(): 
         name = request.POST.get("name")  # получить значение поля Имя 
         age = request.POST.get("age")  # получить значение поля Возраст 
         output = "<h2>Пользователь</h2><h3>Имя - {0}," " Возраст – {1} </h3 >".format(name, age) 
      return HttpResponse(output) 
   userform = UserForm() 
   return render(request, "firstapp/my_form.html", {"form": userform})

