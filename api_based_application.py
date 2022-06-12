import tkinter as tk #for ui 
import requests #for json files
import time #to format some variables (sunset and surise)


#defining a funtion to get the data from the API  
def getWeather(canvas):
    city=textfield.get() 
    api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=715c19b33be756aef7a3abbdd70938f5"

    #now we wil call the json data using request 
    json_data= requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15) #to convert kelvin into celius 
    min_temp = int(json_data['main']['temp_min'] - 273.15) 
    max_temp = int(json_data['main']['temp_max'] - 273.15) 
    pressure = json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S" ,time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunset=time.strftime("%I:%M:%S" ,time.gmtime(json_data['sys']['sunset'] - 19800))

    #we'l define a string to carry all the data 
    final_info = condition+"\n"+ str(temp) +'degree C'
    final_data = '\n'+ 'Maxtemp :' +str(max_temp) +'\n'+'Mintemp :' +str(min_temp) +'Pressure :' + str(pressure) +'\n' + 'Humidity :' +str(humidity) +'\n'+ "wind speed :"  + str(wind)  +'\n' +'Sunrise :' + (sunrise) + '\n' +"Sunset :" + (sunset)

    #attach these strings in our label 
    label1.config(text=final_info)
    label2.config(text=final_data)





#let's define our UI for this we have to write 
canvas = tk.Tk()
#now let's set the geometry of our canvas , let's set it to 600 * 500
canvas.geometry("600x500")
#now we'll set a title for our canvas 
canvas.title("weather app")

#now we'll define some fonts here
f=('poppins',15 ,"bold") #15 is the font size 
t=('poppins',35,'bold')
# now we'll define a text field here to get the city name from the user
textfield = tk.Entry(canvas,justify='center', font = t) #we set the font size as of t
#let's pack this entry
textfield.pack(pady=20) #padding of y coordinate =20
#when user enters the app without moving the cursor if he can directrly enter the name of the city by-
textfield.focus()

#after enter the data should load so 
textfield.bind('<Return>',getWeather)


#now let's create two labels here to show the data so the first one is
label1 = tk.Label(canvas ,font=t) # we attached it to the canvas and set the font size also 
#now lets pack this label 
label1.pack()
#another label 
label2 = tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()

