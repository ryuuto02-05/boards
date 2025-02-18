import re
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from siri import models

JAPANESE_PATTERN = re.compile(r"^[ぁ-んァ-ン一-龥ー]+$")


def index(request):
    all_siri = models.Siri.objects.all()  # データベースからデータを取得
    context = {"all_siri": all_siri}
    return render(request, "siri/index.html", context)


def point(request):
    context = {}
    return render(request, "siri/index2.html", context)


def create(request):
    title = request.POST.get("title")

    if not JAPANESE_PATTERN.match(title):
        return render(
            request,
            "siri/index.html",
            {
                "all_siri": models.Siri.objects.all(),
            },
        )

    last_siri = models.Siri.objects.order_by("-id").first()
    if last_siri is None:
        if title != "しりとり":
            return HttpResponseRedirect(reverse("siri:index"))
    else:
        last_word = last_siri.title
        last = last_word[-1]
        head = title[0]

        if head != last:
            return HttpResponseRedirect(reverse("siri:index"))

    new_siri = models.Siri(title=title, finished=False)
    new_siri.save()

    return HttpResponseRedirect(reverse("siri:index"))


def delete(request, siri_id):
    target_siri = models.Siri.objects.get(id=siri_id)
    target_siri.delete()

    return HttpResponseRedirect(reverse("siri:index"))
