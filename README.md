 <!-- last_siri = models.Siri.objects.order_by("-id").first() -->
    <!-- last_word = last_siri.title

    last = last_word[-1]
    head = title[0]

    new_siri.save()
    return HttpResponseRedirect(reverse("siri:index")) -->

# def create(request):

#     new_siri = models.Siri()
#     new_siri.title = request.POST.get("title")
#     new_siri.save()
#     return HttpResponseRedirect(reverse("siri:index"))

# head == last
        # new_siri = models.Siri()
        # new_siri.title = title
        # new_siri.finished = False