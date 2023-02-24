***SQLAlchemy Analysis***

**Project Description**

*Part 1: Analyzing and Exploring Climate Data*
In climate_analysis.ipynb, you will find a basic climate analysis and data exploration of a climate database. Specifically, this project uses Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. 

The analysis will show results displayed in various formats:
> chart of the previous 12 months of precipitation data
> summary statistics for the precipitation data
> list of total number of stations in the dataset
> list of the stations and observation counts in descending order
> list of most active stations
> histogram of the last year of temperature data (lowest, highest, and average temperatures) for the most active station

*Part 2: Designing A Climate App*
In app.py, you will find a Flask API based on the queries developed in the above Analysis. Flask is used to create the following routes:

> Homepage: /api/v1.0/
> Precipitation Data: /api/v1.0/precipitation
> Stations: /api/v1.0/stations
> Temperature Observations: /api/v1.0/tobs
> Summary Data for a Given Start Date: /api/v1.0/<start>
> Summary Data for Given Start & End Dates: /api/v1.0/<start>/<end>

*Analysis*
> September 2016, April 2017, and February 2017 saw the highest amounts of precipitation over 12 months, reaching a maximum of 6.7 inches in a single day.
> Of the nine stations, USC00519281 was the most active; the temperatures recorded at the station often hovered around a range of 73-77 degrees Farenheight.

*To Use*
Open climate_analysis.ipynb file using Jupyter Notebook and the app.py file in your favorite browser.

*Credits*
https://stackoverflow.com/questions/53460391/passing-a-date-as-a-url-parameter-to-a-flask-route
https://stackoverflow.com/questions/7143235/how-to-use-avg-and-sum-in-sqlalchemy-query
https://stackoverflow.com/questions/43893457/understanding-inplace-true-in-pandas
https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending
https://devsheet.com/code-snippet/sqlalchemy-query-to-get-distinct-records-from-table/
https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html
Grepper Chrome Extension
AskBCS Support
Tutor: Bethany Lindberg