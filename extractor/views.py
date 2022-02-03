from django.contrib import messages
from django.shortcuts import redirect, render

from .scraper import ScrapeImages


def scrape(request):
    if request.method == "POST":
        url = request.POST.get("hero-field")
        if url.startswith("https") or url.startswith("http"):
            get_images = ScrapeImages(url)
            image_and_filename = get_images.get_all_images()
            return render(
                request,
                "home.html",
                context={"ImagesAndFilenames": image_and_filename},
            )
        else:
            messages.add_message(request, messages.INFO, "Wrong Website URL")
            return redirect("extractimg")
    return render(request, "home.html")
