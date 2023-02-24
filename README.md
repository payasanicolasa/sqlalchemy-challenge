***SQLAlchemy Analysis***
<br>
**Project Description**<br>
<br>
*Part 1: Analyzing and Exploring Climate Data*<br>
In climate_analysis.ipynb, you will find a basic climate analysis and data exploration of a climate database. Specifically, this project uses Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. <br>
<br>
The analysis will show results displayed in various formats:<br>
> chart of the previous 12 months of precipitation data<br>
> summary statistics for the precipitation data<br>
> list of total number of stations in the dataset<br>
> list of the stations and observation counts in descending order<br>
> list of most active stations<br>
> histogram of the last year of temperature data (lowest, highest, and average temperatures) for the most active station<br>
<br>
*Part 2: Designing A Climate App*<br>
In app.py, you will find a Flask API based on the queries developed in the above Analysis. Flask is used to create the following routes:<br>
<br>
> Homepage: /api/v1.0/<br>
> Precipitation Data: /api/v1.0/precipitation<br>
> Stations: /api/v1.0/stations<br>
> Temperature Observations: /api/v1.0/tobs<br>
> Summary Data for a Given Start Date: /api/v1.0/<start><br>
> Summary Data for Given Start & End Dates: /api/v1.0/<start>/<end><br>
<br>
*Analysis*<br>
> September 2016, April 2017, and February 2017 saw the highest amounts of precipitation over 12 months, reaching a maximum of 6.7 inches in a single day.<br>
> Of the nine stations, USC00519281 was the most active; the temperatures recorded at the station often hovered around a range of 73-77 degrees Farenheight.<br>
<br>
*To Use*<br>
Open climate_analysis.ipynb file using Jupyter Notebook and the app.py file in your favorite browser.<br>
<br>
*Credits*<br>
https://stackoverflow.com/questions/53460391/passing-a-date-as-a-url-parameter-to-a-flask-route<br>
https://stackoverflow.com/questions/7143235/how-to-use-avg-and-sum-in-sqlalchemy-query<br>
https://stackoverflow.com/questions/43893457/understanding-inplace-true-in-pandas<br>
https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending<br>
https://devsheet.com/code-snippet/sqlalchemy-query-to-get-distinct-records-from-table/<br>
https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text<br>
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html<br>
Grepper Chrome Extension<br>
AskBCS Support<br>
Tutor: Bethany Lindberg
