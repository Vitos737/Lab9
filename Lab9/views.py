from django.http import HttpResponse

def home(request):
    return HttpResponse("Це головна сторінка проєкту Артюхова Віталія")

def resume(request):
    return HttpResponse("Це моє резюме: Артюхов Віталій ,3 Курс Спеціальності: Кібербезпека ")
   
