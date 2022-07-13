from bs4 import *
import re
import requests
from selenium import webdriver


# DOWNLOAD ALL IMAGES FROM THAT URL
# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"Total {len(images)} Image Found!")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

            # 1.data-srcset
            # 2.data-src
            # 3.data-fallback-src
            # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]

            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content
                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"{folder_name}/images{i + 1}.jpg", "wb+") as f:
                        f.write(r)

                    # counting number of image downloaded
                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


# MAIN FUNCTION START
def main():
    main_url = r'https://cubecobra.com/cube/list/museumofmagic?view=spoiler'
    output_path = r'C:\Users\Developer\Downloads\Cubes\museum_of_magic_cube'
    chrome_driver_path = r'C:\Users\Developer\Downloads\chromedriver.exe'

    driver = webdriver.Chrome(chrome_driver_path)

    driver.get(main_url)
    # a = input("Waiting...")

    driver.execute_script("window.scrollTo(0, 0);")

    page_html = driver.page_source
    page_soup = BeautifulSoup(page_html, 'html.parser')
    containers = page_soup.findAll('div', {'class': "col-4 col-sm-3 col-md-2 col-lg-2 col-xl-1-5 col"})
    images = page_soup.findAll('img', {'src': re.compile("^https:")})

    print(len(images))

    # xPath = //*[@id="react-root"]/div/div/div[1]/div[3]/div[2]

    # content of URL
    # r = requests.get(main_url)


    # # Parse HTML Code
    # soup = BeautifulSoup(r.text, 'html.parser')
    #
    # # find all images in URL
    # images = soup.findAll('div', {'class': "position-relative"})
    # print(len(images))
    #
    #
    # # Call folder create function
    download_images(images, output_path)


# CALL MAIN FUNCTION
main()
