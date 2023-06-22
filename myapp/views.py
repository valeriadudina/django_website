from django.shortcuts import render
from django.http import HttpResponse
from .models import Preferences, Tinder_review_2, all_client_trips, Tour, Tinder
from .forms import PrefFrom, TinderForm, ContactUs, Tinder_Review_Form, all_clients
from .openai import where_to_go


def main_page(request):
    return render(request, 'main.html')


def game(request):
    return render(request, 'game.html')


def tours(request):
    tour_list = Tour.objects.all()
    print(tour_list)
    return render(request, 'tours.html', {'tour_list': tour_list})


def index(request):
    form = PrefFrom()
    if request.method =="POST":
        print(request.POST)
        form = PrefFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data['review'])
            answer, picture = where_to_go(form.cleaned_data['review'])
            context = {'answer': answer, 'title': 'Умный подбор', 'url': picture}
            #form.save()
            return render(request, 'preference_form_answer.html', context)


    context = {'form':form}
    return render(request, 'preferences_form.html', context)


def contactus_form(request):
    form = ContactUs
    if request.method == "POST":
        print('responses are here!')
        print(request.POST)
        form = ContactUs(request.POST)

        print(form)

        context = {'answer': "Ваш запрос принят! Мы свяжемся с вами в ближайшее время", "title":"Спасибо"}
        return render(request, 'contact_us_answer.html', context)

    context = {'form': form}
    return render(request, 'contactus_form.html', context)


def tindef_from(request):
    def contains(current, person):
        for elem in current:
            print(elem)
            if elem in person:
                print('yes')
                print(elem)
                return True

        return False
    form = TinderForm()
    if request.method =="POST":
        print('responses are here!')
        print(request.POST)

        model = Tinder(name=request.POST['name'], phone = request.POST['phone'],
                                             type = request.POST['type'],prefered_activities = request.POST['prefered_activities'],
                                             person_details = request.POST['person_details'], about_me = request.POST['about_me'],
                                             about_second = request.POST['about_second']
                                             )
        model.save()
        current = Tinder.objects.last()

        cur_type = getattr(current, "type")
        cur_pref_act = getattr(current, "prefered_activities")
        cur_pers_det = getattr(current, "person_details")
        people_all = Tinder.objects.all()
        selected_person = ''
        for p in people_all:
            print(p.name)
            print(p.id)
            print('Cur', current.id)
            if p.id != current.id:
                p_type = getattr(p, "type")
                p_pref_act = getattr(p, "prefered_activities")
                p_pers_det = getattr(p, "person_details")
                contains_act = contains(cur_pref_act, p_pref_act)
                contains_det = contains(cur_pers_det, p_pers_det)
                print("p_type")
                print(p_type)
                print("cur_type")
                print(cur_type)
                print(contains_act)
                print(contains_det)
                if p_type == cur_type and contains_act and contains_det:
                    selected_person = p
            if selected_person!="":
                context = {'name': getattr(p, "name"),
                           'phone': getattr(p, "phone"),
                           'about_me': getattr(p, "about_me")}
                return render(request, 'tinder_form_answer.html', context)
        context = {'name': "Мы не нашла никого, кто бы вам подошел. Как только появится подходящий кандидат, сразу же вам сообщим",
                   'phone': "",
                   'about_me': ""}
        return render(request, 'tinder_form_answer.html', context)

    context = {'form':form}

    return render(request, 'tinder_form.html', context)


def review_by_id(request, review_id):
    review = Preferences.objects.get(pk=review_id)
    return render(request, 'review_details.html', {'review':review})


def map(request):
    return render(request, 'smart_map.html')


def count_tour(request):
    return render(request, 'count_tour.html')


def insurance(request):
    return render(request, 'insurance.html')


def photo_gallery(request):
    return render(request, 'photo_gallery.html')


def video_gallery(request):
    return render(request, 'video_gallery.html')


def routes_excursions(request):
    return render(request, 'routes_excursions.html')


def list_of_things(request):
    return render(request, 'list_of_things.html')


def about_us(request):
    return render(request, 'about_us.html')

def ways(request):
    return render(request, 'ways.html')


def tinder_review(request):
    form = Tinder_Review_Form()
    if request.method == "POST":
        print('responses are here!')
        print(request.POST['is_pair'])
        form_submitted = TinderForm(request.POST)
        print(request.POST)
        is_pair = request.POST['is_pair']
        what = request.POST['what']
        rating = request.POST['rating']
        review = request.POST['review']
        Tinder_Review = Tinder_review_2(is_pair = is_pair,what = what, rating= rating,review=review  )
        Tinder_Review.save()
        # print(form.cleaned_data['geeks_field'])
        context = {'answer': "submitted!"}
        return render(request, 'tinder_review_answer.html', context)

    context = {'form': form}
    return render(request, 'tinder_review_form.html', context)


def popular_destinations(request):
    tour_list = Tour.objects.values_list('place', flat=True).distinct()
    tour_list = list(tour_list)
    print(tour_list)
    labels_cities = tour_list
    data_cities = [0, 0, 0]
    labels_tours = Tour.objects.values_list('title', flat=True)
    labels_tours = list(labels_tours)
    print(tour_list)

    data_tours = [0, 0, 0, 0, 0, 0]
    data_price=[]
    data_days=[]
    queryset = Tour.objects.order_by('-days')
    for rev in queryset:
        data_price.append(rev.price)
        data_days.append(rev.days)
        if rev.place =="Сочи":
            data_cities[0]+=1
        elif rev.place =="Санкт-Петербург":
            data_cities[1] += 1
        elif rev.place =="Иркутск":
            data_cities[2] += 1

        if rev.title == 'Жемчужина черноморья':
            data_tours[0]+=1
        elif rev.title == 'По Пушкинским местам':
            data_tours[1]+=1
        elif rev.title == 'Искусство на Неве':
            data_tours[2]+=1
        elif rev.title == 'Великолепие Байкала':
            data_tours[3]+=1
        elif rev.title == 'Красная поляна':
            data_tours[4]+=1
        elif rev.title == 'Байкал':
            data_tours[5]+=1
    print(labels_cities)
    print(data_cities)
    print(labels_tours)
    print(data_tours)
    print(data_price)
    print(data_days)
    return render(request, 'dashboard_tours.html', {'labels_cities': labels_cities, 'data_cities': data_cities,
                                                    "labels_tours": labels_tours, "data_tours": data_tours,
                                                    "data_price": data_price, "labels_days": data_days,
                                                    })


def dashboard(request):
    print('dashboard func')
    labels_rating = ["1", "2","3", "4", "5"]
    data_rating = [0,0,0,0,0]

    print('dashboard')
    queryset = Tinder_review_2.objects.order_by('-rating')
    for rev in queryset:
        print(rev)
        print(rev.rating)
        rating = int(rev.rating)
        data_rating[rating-1] += 1

    print(labels_rating)
    print(data_rating)
    labels_pairs = ['Да', 'Нет']
    data_pairs = [0,0]
    for rev in queryset:
        if rev.is_pair == "1":
            data_pairs[0]+=1
        else:
            data_pairs[1] += 1
    labels_what = ['Только общались', 'Поехали в путешествие вместе', 'Завязались отношения', 'Поженились']
    data_what = [0,0,0,0]
    for rev in queryset:
        if rev.what =='talk':
            data_what[0] += 1
        elif rev.what =='trip':
            data_what[1]+=1
        elif rev.what =='continue':
            data_what[2] += 1
        elif rev.what =='married':
            data_what[3] += 1
    print(labels_rating)
    print(data_rating)
    print(labels_pairs)
    print(data_pairs)
    print(labels_what)
    print(data_what)
    return render(request, 'dashboard_tinder_review.html', {'labels_rating':labels_rating, 'data_rating':data_rating,
                                             "labels_pairs" : labels_pairs, "data_pairs" : data_pairs,
                                       "labels_what": labels_what, "data_what": data_what,
                                            })


def tour_list(request):
    """A view of all bands."""
    tour_list = Tour.objects.all()
    print(tour_list)
    return render(request, 'test.html', {'tour_list': tour_list})


def TourDetailView(request, slug):
    """Полное описание тура"""
    tour = Tour.objects.get(url=slug)
    print(tour.get_comfort_display())
    return render(request, "tour_detail.html", {"tour": tour})



