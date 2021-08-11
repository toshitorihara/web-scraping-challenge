# Web Scraping: Mission to Mars
![Image](Images/mission_to_mars.png)
The purpose of this project is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Part I - Web Scraping
Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
* Create a [**Jupyter Notebook**](Missions_to_Mars/mission_to_mars.ipynb) and use this to complete all scraping and analysis tasks. 

### 1. NASA Mars News
* Scrape the [**Mars News Site**](https://redplanetscience.com/) and collect the latest `News Title` and `Paragraph Text`. Assign the text to variables that you can reference later.

### 2. JPL Mars Space Images - Featured Image
* Visit the url for the [**Featured Space Image**](https://spaceimages-mars.com/#) site.
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
* Make sure to find the image url to the full size .jpg image.
* Make sure to save a complete url string for this image.

### 3. Mars Facts
* Visit the [**Mars Facts**](https://galaxyfacts-mars.com/) webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

### 4. Mars Hemispheres
* Visit the [**Astrogeology**](https://marshemispheres.com/) site to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
* Use a Python dictionary to store the data using the keys `img_url` and `title`.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Part II - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
* Convert the **Jupyter notebook** into a [**Python script**](Missions_to_Mars/scrape_mars.py) with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.
* Create a [**Python application**](Missions_to_Mars/app.py) with route called `/scrape` that will import `scrape_mars.py` script to `app.py` and call the scrape function using Pymongo and store the return value in Mongo as a Python dictionary.
* Create a root route `/` that will query the Mongo database and pass into a template [**HTML file**](Missions_to_Mars/templates/index.html) that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
