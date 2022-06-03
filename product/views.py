from django.shortcuts import render, redirect
from .models import Category, Drink


def drink_view(request):
    if request.method == "POST":
        # name = request.POST.get("name", None)
        # return redirect("drink")
        return render(request, "product/drink.html", {"POST": "POST방식입니다!"})
    elif request.method == "GET":
        # category = Category.objects.get(category=category)
        # name = Drink.objects.get(name=name)
        # nutrition = Drink.objects.get(nutrition=nutrition)
        # allergy = Drink.objects.get(allergy=allergy)

        # return render(
        #     request,
        #     "product/drink.html",
        #     {
        #         "name": name,
        #         "category": category,
        #         "nutrition": nutrition,
        #         "allergy": allergy,
        #     },
        # )
        return render(request, "product/drink.html", {"GET": "GET방식입니다!"})
