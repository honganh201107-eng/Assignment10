#1
import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(data['value'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_chuck_norris_joke()



#2
import requests

def get_weather():
    api_key = "7ebec69a5659ed93b555a1ca04976968"
    municipality = input("Enter the name of a municipality: ")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data['weather'][0]['description']
            temp_kelvin = data['main']['temp']
            
            temp_celsius = temp_kelvin - 273.15
            
            print(f"Weather condition: {description.capitalize()}")
            print(f"Temperature: {temp_celsius:.1f} °C")
        else:
            print("Municipality not found or API key error.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_weather()



#3
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })

if __name__ == '__main__':
    app.run(port=5000)



#4
import json
from flask import Flask, jsonify

app = Flask(__name__)

def load_airports():
    try:
        with open('airports.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport(icao):
    airports = load_airports()
    airport = next((a for a in airports if a["icao"].upper() == icao.upper()), None)

    if airport:
        return jsonify({
            "icao": airport["icao"],
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(port=5001)



[
    {"icao": "LFLL", "name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    {"icao": "EGLL", "name": "Heathrow Airport", "city": "London", "country": "GB"},
    {"icao": "KJFK", "name": "John F. Kennedy International Airport", "city": "New York", "country": "US"}
]



{
  "categories": [],
  "created_at": "2020-01-05 13:42:29.296379",
  "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
  "id": "GAQ6zEpsR3myzahGPpZKbQ",
  "updated_at": "2020-01-05 13:42:29.296379",
  "url": "https://api.chucknorris.io/jokes/GAQ6zEpsR3myzahGPpZKbQ",
  "value": "freakin Chuck Norris, is there nothing this guy can't do?"
}