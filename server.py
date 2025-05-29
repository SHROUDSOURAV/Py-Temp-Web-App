from flask import Flask, render_template, request
from weather import getWeather 
from waitress import serve

# makes app an instance of Flask object
# flask is used to develop web applications 
app = Flask(__name__)

# @app.route('/url')    specifies a url path(route) of the website which triggers some function made by flask when the url is visited
# @app.route mentioned urls need to have implemented functions
# those functions must return something

@app.route('/') #   / means the homepage of the website
@app.route('/index')    #   /index means the index page of the website

def index():    # index url function triggered when /index page of the webiste is visited
    return render_template('index.html')    # loads and renders the index.html page

@app.route('/weather')
def weather():
    # get the value of the city from the index.html input field
    city = request.args.get('city')
    weather_data = getWeather(city)

    # render the details to the HTML page
    # loads an HTML file from the templates folder and renders it
    return render_template(
        # all the data  
        "weather.html", # template 
        title = weather_data["name"],    # getting the city name for the title of the web page for displaying
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"

    )




if __name__ == '__main__':
    #app.run runs the web server on localhost at port 8000
    #app.run hosts the server on localhost on port 8000
    # app.run(host="0.0.0.0", port=8000)
    serve(app, host="0.0.0.0", port=8000)