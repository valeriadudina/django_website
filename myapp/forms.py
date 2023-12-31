from django.forms import ModelForm
from .models import Preferences, Tinder,  Tinder_review_2, all_client_trips
from django import forms

activities = (
('sea_activities', 'Загорать и купаться'),
('walking', 'Гулять по городу'),
('for_oldies', 'Посетить санаторий/спа'),
('mountains', 'Подняться в горы'),
('for_masha', 'Сходить в поход'),
('museums', 'Посещать музеи и достопримечательности'),
('sex', 'Развлекаться')
)
person = (('smart', 'Умный'),
('funny', 'Веселый'),
('versatile', 'Разносторонний'),
('talkative', 'Общительный'),
('brave', 'Смелый')
)


class PrefFrom(ModelForm):
    class Meta:
        model = Preferences
        fields = '__all__'


class TinderForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=200)
    phone = forms.CharField(max_length=11, label="Номер телефона")

    type = forms.ChoiceField(label="Какой тип отдыха вы предпочитаете",
                              choices=(('active', 'Активный'), ('culture', 'Культурно-познавательный'),
                                        ('health', 'Оздоровительный'),
                                        ('beach', 'Пляжный'),))

    prefered_activities = forms.MultipleChoiceField(label="Выберите, что вы предпочитаете делать во время отдыха",
                                                    choices=activities, widget=forms.CheckboxSelectMultiple())
    person_details = forms.MultipleChoiceField(label="Какие черты характера для вас важны",
                                               choices=person, widget=forms.CheckboxSelectMultiple())

    about_me = forms.CharField(max_length=300, label="Напишите пару слов о себе",  widget=forms.Textarea(attrs={'rows': 6, 'cols': 35}))
    about_second = forms.CharField(max_length=300, label="Опишите своего идеального попутчика", widget=forms.Textarea(attrs={'rows': 6, 'cols': 35}))


class Tinder_Review_Form(forms.Form):
    is_pair = forms.ChoiceField(label="Вы нашли пару?", widget=forms.RadioSelect(attrs={'size': 10, 'title': 'Вы нашли пару?'}), choices=(('1', 'Да'), ('2', 'Нет'),))
    what= forms.ChoiceField(label="Что делали вместе?",choices=(('talk', 'Только общались'),
                                                     ('trip', 'Поехали в путешествие вместе'),
                                                       ('continue', 'Завязались отношения'),
                                                       ('married', 'Поженились'),
                                                       ))
    rating= forms.ChoiceField(label="Рейтинг", choices = (('1', '1'),
                                                            ('2', '2'),
                                                            ('3', '3'),
                                                            ('4', '4'),
                                                            ('5', '5'),
                                                            ))
    review= forms.CharField(label="Рейтинг 2", max_length=1000, widget=forms.Textarea(attrs={ 'rows':5}))
    class Meta:
        model = Tinder_review_2

        fields = '__all__'


class ContactUs(forms.Form):
    name = forms.CharField(label="Имя", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    phone = forms.CharField(label="Номер телефона", max_length=11, widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    email = forms.CharField(label="Почта", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    question = forms.CharField(label="Ваш вопрос:", max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Ваш вопрос', 'rows':5}))

class all_clients(forms.Form):
    city = forms.CharField(max_length=20)
    tour = forms.CharField(max_length=20)
    price = forms.IntegerField()
    days = forms.IntegerField()
    class Meta:
        model = all_client_trips

        fields = '__all__'