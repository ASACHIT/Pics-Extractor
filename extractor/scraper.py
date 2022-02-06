from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup as bs


class ScrapeImages:
    def __init__(self, url):
        self.url = url

    def validate_url(self, image_url):
        """
        Check if url is valid or not
        """
        parsed = urlparse(image_url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_all_images(self):
        """
        Returns image link, image file name, image file extension zipped makig queryset or an object
        """

        urls = []
        filenames_list = []
        file_extension = []

        soup = bs(requests.get(self.url).content, "html.parser")
        for img in soup.find_all("img"):
            img_url = img.attrs.get("src")

            # if image url doesnot containt src attribute continue or skip
            if not img_url:
                continue

            # make the URL absolute by joining domain with the URL that is just extracted
            img_url = urljoin(self.url, img_url)

            try:
                # removing other mess like queries in urls
                pos = img_url.index("?")
                img_url = img_url[:pos]
            except ValueError:
                pass

            if self.validate_url(img_url):
                # if direct image links are valid, then append to the defined list
                urls.append(img_url)

                # fullimagename such as sachit.png, python.png etc
                full_image_name = img_url.split("/")[-1]

                # file name only without extension like sachit, python etc
                filenames_list.append(full_image_name.split(".")[0][:10])

                # file extension only like png, jpeg, jpg, svg
                file_extension.append(full_image_name.split(".")[-1][:10])

        # zipping all list and returning a queryset or object
        all_list = zip(urls, filenames_list, file_extension)
        return all_list


if __name__ == "__main__":
    a = ScrapeImages("http://itsnp.org/")
    for link, filename, fileformat in a.get_all_images():
        print(link, filename, fileformat)
