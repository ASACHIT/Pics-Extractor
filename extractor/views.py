from django.contrib import messages
from django.shortcuts import redirect, render

from .scraper import ScrapeImages  # scraping script


def scrape(request):
    # if form is submitted with post request then
    if request.method == "POST":
        url = request.POST.get("hero-field")  # fecthing url from input tag
        # validating inputted url
        if url.startswith("https") or url.startswith("http"):
            get_images = ScrapeImages(url)
            image_and_filename = get_images.get_all_images()
            return render(
                request,
                "home.html",
                context={"ImagesAndFilenames": image_and_filename},
            )
        # if invalid url then send error message
        else:
            messages.add_message(
                request, messages.INFO, "Wrong Website URL, Input with Protocols"
            )
            return redirect("extractimg")  # redirect to home page
    return render(request, "home.html")  # rendering home page
