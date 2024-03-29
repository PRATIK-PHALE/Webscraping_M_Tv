# -*- coding: utf-8 -*-
"""Web Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hdpe2_BA-yWN_b1-NoeSJMRhLNn0eHWj

# **Web Scraping & Data Handling Challenge**

# **Start The Project**

## **Task 1:- Web Scrapping**
"""

#Installing all necessary labraries
!pip install bs4
!pip install requests

#import all necessary labraries
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

"""## **Scrapping Movies Data**"""

# Specifying the URL from which movies related data will be fetched
url='https://www.justwatch.com/in/movies?release_year_from=2000'

# Sending an HTTP GET request to the URL
response=requests.get(url)
# Parsing the HTML content using BeautifulSoup with the 'html.parser'
soup=BeautifulSoup(response.text,'html.parser')
# Printing the prettified HTML content
# print(soup.prettify())

"""## **Fetching Movie URL's**"""

# Write Your Code here
from urllib.parse import urljoin

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_links = soup.find_all(class_='title-list-grid__item')  # Replace 'title-list-grid__item' with the appropriate class name

    for link in movie_links:
        movie_title = link.text.strip()

        # Check if the link is stored in a different attribute or element
        if link.has_attr('href'):
            movie_href = link['href']
            full_movie_link = urljoin(url, movie_href)
        elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
            movie_href = link['src']
            full_movie_link = urljoin(url, movie_href)
        else: # Example: If the link is nested within the anchor tag
            movie_href = link.find('a')['href']
            full_movie_link = urljoin(url, movie_href)

        print(f"Movie Link:{full_movie_link}\n")

    print("Failed to fetch the webpage")

"""## **Scrapping Movie Title**"""

# Write Your Code here
movie_title = []
for link in movie_links:

        # Check if the link is stored in a different attribute or element
        if link.has_attr('href'):
            movie_href = link['href']
            full_movie_link = urljoin(url, movie_href)
        elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
            movie_href = link['src']
            full_movie_link = urljoin(url, movie_href)
        else:  # Example: If the link is nested within the anchor tag
            movie_href = link.find('a')['href']
            full_movie_link = urljoin(url, movie_href)

        # Send a GET request to the URL
        response = requests.get(full_movie_link)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the h1 tag with class 'title-block'
        title_block = soup.find('div', class_='title-block')

        #If the title-block is found, extract the title
        if title_block:
          title_h1 = title_block.find('h1')
          if title_h1:
            title = title_h1.text.strip()  # Get the text and remove leading/trailing whitespaces
            # print(f"Title:{title}\n")
        else:
          print("Title block not found.")
        movie_title.append(title)
        # print(f"Movie Title: {movie_title}\nMovie Link: {full_movie_link}\n")
print(movie_title)

"""## **Scrapping release Year**"""

Release_year=[]
# Write Your Code here
for link in movie_links:
        movie_title = link.text.strip()

        # Check if the link is stored in a different attribute or element
        if link.has_attr('href'):
            movie_href = link['href']
            full_movie_link = urljoin(url, movie_href)
        elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
            movie_href = link['src']
            full_movie_link = urljoin(url, movie_href)
        else:  # Example: If the link is nested within the anchor tag
            movie_href = link.find('a')['href']
            full_movie_link = urljoin(url, movie_href)
        # Send a GET request to the URL
        response = requests.get(full_movie_link)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the h1 tag with class 'title-block'
        title_block = soup.find('div', class_='title-block')
        #If the title-block is found, extract the title
        if title_block:
          release_Year = title_block.find('span',class_='text-muted')
          title_h1 = title_block.find('h1')
          if release_Year:
            year = release_Year.text.strip()
            title = title_h1.text.strip() # Get the text and remove leading/trailing whitespaces
            years=re.sub(r'[()]', '', year)
            # print(f"Title:{title}\nRelease Year:{year}\n")
          else:
            print("h1 tag not found inside the title-block div.")
        Release_year.append(years)
else:
    print("Title block not found.")


        # print(f"Movie Title: {movie_title}\nMovie Link: {full_movie_link}\n")
print("Failed to fetch the webpage")
Release_year

"""## **Scrapping Genres**"""

# Write Your Code here
Genres=[]
for link in movie_links:
    movie_title = link.text.strip()

    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        movie_href = link['href']
        full_movie_link = urljoin(url, movie_href)
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        movie_href = link['src']
        full_movie_link = urljoin(url, movie_href)
    else:  # Example: If the link is nested within the anchor tag
        movie_href = link.find('a')['href']
        full_movie_link = urljoin(url, movie_href)
    # Send a GET request to the URL
    response = requests.get(full_movie_link)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    genres_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Iterate through the found divs
    for genre_div in genres_divs:
        # Check if the text inside the div is 'Genres'
        if genre_div.text.strip() == 'Genres':
            # Find the sibling div containing the genre information
            sibling_div = genre_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If genre_value is found, print the text
                genre_text = sibling_div.get_text(strip=True)
                Genres.append(genre_text)
                # print(f"Genres: {genre_text}")
            else:
                # If genre_value is not found, print a message
                Genres.append(np.nan)
                print("Genres information not found ")
            break  # Exit the loop once the genre information is found
    else:
        # If 'Genres' section is not found, print a message
        print("Genres information not found for this movie.")
print(Genres)

"""## **Scrapping IMBD Rating**"""

Rating = []

for link in movie_links:
    movie_title = link.text.strip()

    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        movie_href = link['href']
        full_movie_link = urljoin(url, movie_href)
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        movie_href = link['src']
        full_movie_link = urljoin(url, movie_href)
    else:  # Example: If the link is nested within the anchor tag
        movie_href = link.find('a')['href']
        full_movie_link = urljoin(url, movie_href)

    # Send a GET request to the URL
    response = requests.get(full_movie_link)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    rating_divs = soup.find_all('h3', class_='detail-infos__subheading')

    # Iterate through the found divs
    for rating_div in rating_divs:
        # Check if the text inside the div is 'Rating'
        if rating_div.text.strip() == 'Rating':
            # Find the sibling div containing the rating information
            sibling_div = rating_div.find_next_sibling('div')

            # Fetch text of the div with a specific class
            if sibling_div:
                # If rating_value is found, append the text to the Rating list
                rating_text = sibling_div.get_text(strip=True)
                Rating.append(rating_text[0:3])
                # print(f"Rating: {rating_text}")
            else:
                # If rating_value is not found, print a message
                print("Rating information not found ")
            break  # Exit the loop once the rating information is found

    else:
        # If 'Rating' section is not found, print a message
        print("Rating information not found for this movie.")

# Print the Rating list
print(Rating)

"""## **Scrapping Runtime/Duration**"""

# Write Your Code here
Runtime=[]
for link in movie_links:
    movie_title = link.text.strip()

    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        movie_href = link['href']
        full_movie_link = urljoin(url, movie_href)
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        movie_href = link['src']
        full_movie_link = urljoin(url, movie_href)
    else:  # Example: If the link is nested within the anchor tag
        movie_href = link.find('a')['href']
        full_movie_link = urljoin(url, movie_href)
    # Send a GET request to the URL
    response = requests.get(full_movie_link)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    runtime_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Iterate through the found divs
    for Runtime_div in runtime_divs:
        # Check if the text inside the div is 'Runtime'
        if Runtime_div.text.strip() == 'Runtime':
            # Find the sibling div containing the  Runtime information
            sibling_div = Runtime_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Runtime_value is found, print the text
                Runtime_text = sibling_div.get_text(strip=True)
                Runtime.append(Runtime_text)
                # slice_str=Runtime_text[0:3]
                # print(f"Runtime: {Runtime_text}")
            else:
                # If Runtime_value is not found, print a message
                Runtime.append(np.nan)
                print("Runtime information not found ")
            break  # Exit the loop once the  Runtime information is found
    else:
        # If 'Runtime' section is not found, print a message
        print("Runtime information not found for this movie.")
Runtime

"""## **Scrapping Age Rating**"""

# Write Your Code here
Age_rating=[]
for link in movie_links:
    movie_title = link.text.strip()

    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        movie_href = link['href']
        full_movie_link = urljoin(url, movie_href)
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        movie_href = link['src']
        full_movie_link = urljoin(url, movie_href)
    else:  # Example: If the link is nested within the anchor tag
        movie_href = link.find('a')['href']
        full_movie_link = urljoin(url, movie_href)
    # Send a GET request to the URL
    response = requests.get(full_movie_link)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    Age_rating_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Iterate through the found divs
    for Age_rating_div in Age_rating_divs:
        # Check if the text inside the div is 'Age_rating'
        if Age_rating_div.text.strip() == 'Age rating':
            # Find the sibling div containing the Age_rating information
            sibling_div = Age_rating_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Age_rating_value is found, print the text
                Age_rating_text = sibling_div.get_text(strip=True)
                Age_rating.append(Age_rating_text)
                # print(f"Age_rating: {Age_rating_text}")
            else:
                # If Age_rating_value is not found, print a message
                Age_rating.append(None)
                # print(f"Age_rating: {Age_rating_text}")
            break  # Exit the loop once the Age_rating information is found

    else:
      Age_rating.append(None)

print(len(Age_rating))

"""## **Fetching Production Countries Details**"""

Production_countries = []

for link in movie_links:
    movie_title = link.text.strip()

    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        movie_href = link['href']
        full_movie_link = urljoin(url, movie_href)
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        movie_href = link['src']
        full_movie_link = urljoin(url, movie_href)
    else:  # Example: If the link is nested within the anchor tag
        movie_href = link.find('a')['href']
        full_movie_link = urljoin(url, movie_href)

    # Send a GET request to the URL
    response = requests.get(full_movie_link)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    Production_country_divs = soup.find_all('h3', class_='detail-infos__subheading')

    # Flag to check if Production country information is found
    found_production_country = False

    # Iterate through the found divs
    for Production_country_div in Production_country_divs:
        # Check if the text inside the div is 'Production country'
        if Production_country_div.text.strip() == 'Production country':
            # Find the sibling div containing the Production country information
            sibling_div = Production_country_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Production country value is found, append it to the list
                Production_country_text = sibling_div.get_text(strip=True)
                Production_countries.append(Production_country_text)
                found_production_country = True
            else:
                # If Production country value is not found, append NaN
                Production_countries.append(np.nan)
                print(f"Production country not found for {movie_title}")
            break  # Exit the loop once the Production_countries information is found

    # If Production country information is not found, append NaN
    if not found_production_country:
        Production_countries.append(np.nan)
        print(f"Production country not found for {movie_title}")

Production_countries

"""## **Fetching Streaming Service Details**"""

Director=[]
for link in movie_links:
    movie_title = link.text.strip()

    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        movie_href = link['href']
        full_movie_link = urljoin(url, movie_href)
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        movie_href = link['src']
        full_movie_link = urljoin(url, movie_href)
    else:  # Example: If the link is nested within the anchor tag
        movie_href = link.find('a')['href']
        full_movie_link = urljoin(url, movie_href)
    # Send a GET request to the URL
    response = requests.get(full_movie_link)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    Director_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Iterate through the found divs
    for Director_div in Director_divs:
        # Check if the text inside the div is 'Director'
        if Director_div.text.strip() == 'Director':
            # Find the sibling div containing the Director information
            sibling_div = Director_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Director_value is found, print the text
                Director_text = sibling_div.get_text(strip=True)
                Director.append(Director_text)
                # print(f"Director: {Director_text}")
            else:
                # If Director_value is not found, print a message
                Director_text=np.nan
                Director.append(Director_text)
                # print(f"Director: {Director_text}")
            break  # Exit the loop once the Director information is found
    else:
        # If 'Director' section is not found, print a message
        Director_text=np.nan
        Director.append(Director_text)
        # print(f"Director: {Director_text}")
Director

"""## **Now Creating Movies DataFrame**"""

data = {
    'movie_title': movie_title,
    'Release_year': Release_year,
    'Genres': Genres,
    'Rating': Rating,
    'Runtime': Runtime,
    'Age_rating': Age_rating,
    'Production_countries': Production_countries,
    'Streaming_platform': Director
}

# Create DataFrame
Movies_df = pd.DataFrame(data)
# Display DataFrame
Movies_df.info()

"""## **Scraping TV  Show Data**"""

# Specifying the URL from which tv show related data will be fetched
tv_url='https://www.justwatch.com/in/tv-shows?release_year_from=2000'
# Sending an HTTP GET request to the URL
page=requests.get(tv_url)
# Parsing the HTML content using BeautifulSoup with the 'html.parser'
soup=BeautifulSoup(page.text,'html.parser')
# Printing the prettified HTML content
print(soup.prettify())

"""## **Fetching Tv shows Url details**"""

# Write Your Code here
if page.status_code==200:
  soup = BeautifulSoup(page.text,'html.parser')
  Tv_shows_links = soup.find_all(class_='title-list-grid__item--link')

for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    print(f"Movie Link: {fullurl}\n")
print('Not found tV SHOW ')

"""## **Fetching Tv Show Title details**"""

# Write Your Code here
Tv_shows_title=[]
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # GET THE RESPonse
    page=requests.get(fullurl)
    # parse the html content
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the h1 tag in the title-block
    title_block=soup.find('div',class_='title-block')
    # extract h1
    if title_block:
      title_h1=title_block.find('h1')
      if title_h1:
        Tv_shows=title_h1.text.strip()
        Tv_shows_title.append(Tv_shows)
      else:
        Tv_shows_title.append(np.nan)
print('Not found tV SHOW ')
Tv_shows_title

"""## **Fetching Release Year**"""

Tv_show_years=[]
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # GET THE RESPonse
    page=requests.get(fullurl)
    # parse the html content
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the h1 tag in the title-block
    title_block=soup.find('div',class_='title-block')
    # extract span inside title-block
    if title_block:
      year=title_block.find('span')
      if year:
        years=year.text.strip()
        tv_show_year=re.sub(r'[()]', '', years)
        # print(f'Title:{title}')
        Tv_show_years.append(tv_show_year)
      else:
        Tv_show_years.append(np.nan)
print('Not found tV SHOW ')
Tv_show_years

"""## **Fetching TV Show Genre Details**"""

TV_Show_Genre=[]
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # GET THE RESPonse
    page=requests.get(fullurl)
    # parse the html content
    soup = BeautifulSoup(page.content, 'html.parser')
    # find the h1 tag in the title-block
    Genres_divs=soup.find_all('h3',class_='detail-infos__subheading')
    # extract span inside title-block
    for Genres_div in Genres_divs:
      if Genres_div.text.strip() =="Genres":
        sibling_div=Genres_div.find_next_sibling('div')
        if sibling_div:
          TV_Shows_Genre=sibling_div.text.strip()
          TV_Show_Genre.append(TV_Shows_Genre)
        else:
          # print('sibling div not found')
          TV_Show_Genre.append(np.nan)
        break
print('Not found TV_Show_Genre ')
TV_Show_Genre

"""## **Fetching IMDB Rating Details**"""

Tv_show_Rating = []
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # Send a GET request to the URL
    response = requests.get(fullurl)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    rating_divs = soup.find_all('h3', class_='detail-infos__subheading')

    # Iterate through the found divs
    for rating_div in rating_divs:
        # Check if the text inside the div is 'Rating'
        if rating_div.text.strip() == 'Rating':
            # Find the sibling div containing the rating information
            sibling_div = rating_div.find_next_sibling('div')

            # Fetch text of the div with a specific class
            if sibling_div:
                # If rating_value is found, append the text to the Rating list
                rating_text = sibling_div.get_text(strip=True)
                Tv_show_Rating.append(rating_text[0:3])
                # print(f"Rating: {rating_text}")
            else:
                # If rating_value is not found, print a message
                print("Rating information not found ")
                Tv_show_Rating.append(np.nan)
            break  # Exit the loop once the rating information is found
    else:
        # If 'Rating' section is not found, print a message
        print("Rating information not found for this movie.")

# Print the Rating list
Tv_show_Rating

"""## **Fetching Age Rating Details**"""

Tv_Age_Rating  = []
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # Send a GET request to the URL
    response = requests.get(fullurl)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    Age_rating_divs = soup.find_all('h3', class_='detail-infos__subheading')

    # Iterate through the found divs
    for Age_rating_div in Age_rating_divs:
        # Check if the text inside the div is 'Age rating'
        if Age_rating_div.text.strip() == 'Age rating':
            # Find the sibling div containing the rating information
            sibling_div = Age_rating_div.find_next_sibling('div')

            # Fetch text of the div with a specific class
            if sibling_div:
                # If Age_rating_value is found, append the text to the Age_rating list
                Age_rating_text = sibling_div.get_text(strip=True)
                Tv_Age_Rating.append(Age_rating_text)
                # print(f"Rating: {rating_text}")
            else:
                Tv_Age_Rating.append(None)
            break  # Exit the loop once the rating information is found
    else:
        Tv_Age_Rating.append(None)
        # If 'Rating' section is not found, print a message


# Print the Rating list
Tv_Age_Rating

"""## **Fetching Production Country details**"""

Tv_P_countries = []

for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # Send a GET request to the URL
    response = requests.get(fullurl)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    Production_country_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Flag to check if Production country information is found
    found_production_country = False
    # Iterate through the found divs
    for Production_country_div in Production_country_divs:
        # Check if the text inside the div is 'Production country'
        if Production_country_div.text.strip() == 'Production country':
            # Find the sibling div containing the Production country information
            sibling_div = Production_country_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Production country value is found, append it to the list
                Production_country_text = sibling_div.get_text(strip=True)
                Tv_P_countries.append(Production_country_text)
                found_production_country = True
            else:
                # If Production country value is not found, append NaN
                Tv_P_countries.append(np.nan)
                print(f"Production country not found for {movie_title}")
            break  # Exit the loop once the Production_countries information is found

    # If Production country information is not found, append NaN
    if not found_production_country:
        Tv_P_countries.append(np.nan)
        print(f"Production country not found for {movie_title}")

Tv_P_countries

"""## **Fetching Streaming Service details**"""

tv_show_Director=[]
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # Send a GET request to the URL
    response = requests.get(fullurl)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    Director_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Iterate through the found divs
    for Director_div in Director_divs:
        # Check if the text inside the div is 'Director'
        if Director_div.text.strip() == 'Director':
            # Find the sibling div containing the Director information
            sibling_div = Director_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Director_value is found, print the text
                Director_text = sibling_div.get_text(strip=True)
                tv_show_Director.append(Director_text)
                # print(f"Director: {Director_text}")
            else:
                tv_show_Director.append(None)
                # print(f"Director: {Director_text}")
            break  # Exit the loop once the Director information is found
    else:
        # If 'Director' section is not found, print a message
        tv_show_Director.append(None)
        # print(f"Director: {Director_text}")
tv_show_Director

"""## **Fetching Duration Details**"""

Tv_show_RT=[]
for link in Tv_shows_links:
    # Check if the link is stored in a different attribute or element
    if link.has_attr('href'):
        Tv_hrefs = link['href']
    elif link.has_attr('src'):  # Example: If the link is stored in the 'src' attribute
        Tv_hrefs = link['src']
    else:  # Example: If the link is nested within the anchor tag
        Tv_hrefs = link.find('a')['href']
    fullurl = urljoin(tv_url, Tv_hrefs)
    # Send a GET request to the URL
    response = requests.get(fullurl)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all occurrences of the div with class 'detail-infos__subheading' with h3 tag
    runtime_divs = soup.find_all('h3', class_='detail-infos__subheading')
    # Iterate through the found divs
    for Runtime_div in runtime_divs:
        # Check if the text inside the div is 'Runtime'
        if Runtime_div.text.strip() == 'Runtime':
            # Find the sibling div containing the  Runtime information
            sibling_div = Runtime_div.find_next_sibling('div')
            # Fetch text of the div with a specific class
            if sibling_div:
                # If Runtime_value is found, print the text
                Runtime_text = sibling_div.get_text(strip=True)
                Tv_show_RT.append(Runtime_text)
                # print(f"Runtime: {Runtime_text}")
            else:
                # If Runtime_value is not found, print a message
                print("Runtime information not found ")
                Tv_show_RT.append(np.nan)
            break  # Exit the loop once the  Runtime information is found
    else:
        # If 'Runtime' section is not found, print a message
        print("Runtime information not found for this movie.")
Tv_show_RT

"""## **Creating TV Show DataFrame**"""

data2 ={
    'Tv_s_title':Tv_shows_title,
    'Tv_s_years':Tv_show_years,
    'TV_s_Genre':TV_Show_Genre,
    'Tv_s_Rating':Tv_show_Rating,
    'Tv_Age_Rating':Tv_Age_Rating,
    'Tv_P_countries':Tv_P_countries,
    'Tv_Streaming_platform':tv_show_Director,
    'Tv_s_RTime':Tv_show_RT
}
Tv_df=pd.DataFrame(data2)
Tv_df

"""## **Task 2 :- Data Filtering & Analysis**"""

from datetime import datetime
from datetime import timedelta

# Tv_shows
Tv_df['Tv_s_years'] = pd.to_datetime(Tv_df['Tv_s_years'], format='%Y')
Tv_df['Tv_s_Rating'] = pd.to_numeric(Tv_df['Tv_s_Rating'], errors='coerce')

# Movies
Movies_df['Rating'] = pd.to_numeric(Movies_df['Rating'], errors='coerce')
# Convert 'release_date' to datetime.date objects
Movies_df['Release_year'] = pd.to_datetime(Movies_df['Release_year'], format='%Y')


current_year = datetime.now().year
two_years_ago = pd.to_datetime(current_year - 2)

# - Only include movies and TV shows released in the last 2 years (from the current date).
#  - Only include movies and TV shows with an IMDb rating of 7 or higher.
Movies_fillter_df=Movies_df[(Movies_df['Release_year'] >= two_years_ago) & (Movies_df['Rating'] >= 7)]
Tv_fillter_df=Tv_df[(Tv_df['Tv_s_years'] >= two_years_ago) & (Tv_df['Tv_s_Rating'] >= 7)]

"""## **Calculating Mean IMDB Ratings for both Movies and Tv Shows**"""

# Write Your Code here
Mean_Tv_df_Ratings=Tv_df['Tv_s_Rating'].mean()
print(Mean_Tv_df_Ratings)
Mean_Movies_df_Ratings=Movies_df['Rating'].mean()
print(Mean_Movies_df_Ratings)

"""## **Analyzing Top Genres**"""

# Write Your Code here
movies_genre_counts =Movies_df['Genres'].value_counts()
movies_genre_counts.head(5)
Tv_genre_counts =Tv_df['TV_s_Genre'].value_counts()
Tv_genre_counts.head(5)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Count occurrences of each genre
genre_counts1 = Movies_df['Genres'].value_counts().head(5)
genre_counts2 = Tv_df['TV_s_Genre'].value_counts().head(5)

# Convert the genre counts to a dictionary
genre_counts_dict1 = genre_counts1.to_dict()
genre_counts_dict2 = genre_counts2.to_dict()

# Generate the word cloud
wordcloud1 = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(genre_counts_dict1)
wordcloud2 = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(genre_counts_dict2)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis('off')
plt.show()
print('\n')
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis('off')
plt.show()

"""## **Finding Predominant Streaming Service**"""

# Write Your Code here
movies_Streaming_counts =Movies_df['Streaming_platform'].value_counts()
movies_Streaming_counts.head(5)
Tv_Streaming_counts =Tv_df['Tv_Streaming_platform'].value_counts()
Tv_Streaming_counts.head(5)

#Let's Visvalize it using word cloud
# Count occurrences of each genre
Streaming_counts1 = Movies_df['Streaming_platform'].value_counts().head(5)
Streaming_counts2 = Tv_df['Tv_Streaming_platform'].value_counts().head(5)

# Convert the Streaming counts to a dictionary
Streaming_counts_dict1 = Streaming_counts1.to_dict()
Streaming_counts_dict2 = Streaming_counts2.to_dict()

# Generate the word cloud
wordcloud1 = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(Streaming_counts_dict1)
wordcloud2 = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(Streaming_counts_dict2)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis('off')
plt.show()
print('\n')
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis('off')
plt.show()

"""## **Task 3 :- Data Export**"""

#saving final dataframe as Final Data in csv format
Movies_df.to_csv("D:\\DATA_EXCEL\\movies_data.csv", index=False)
Tv_df.to_csv("D:\\DATA_EXCEL\\Tv_show_data.csv", index=False)

#saving filter data as Filter Data in csv format
Movies_fillter_df.to_csv("D:\\DATA_EXCEL\\Movies_fillter.csv", index=False)
Tv_fillter_df.to_csv("D:\\DATA_EXCEL\\Tv_fillter_.csv", index=False)

"""# **Dataset Drive Link (View Access with Anyone) -**

https://drive.google.com/drive/folders/1R3Thqy77C7Qw4QKtcWyjf2U2_aRIm1tN?usp=drive_link
"""