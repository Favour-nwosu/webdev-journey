const input = document.getElementById("city-name")
const button = document.getElementById("button")
const result =document.getElementById("weather-result")

button.addEventListener("click" , function (){
    const city = input.value.trim()
    if (city ==="") return
    
    fetch("https://geocoding-api.open-meteo.com/v1/search?name=" + city + "&count=1")
    .then(function(response) {
        return response.json()
    })
    .then(function(data){
        const lat = data.results[0].latitude
        const lon = data.results[0].longitude

        return fetch("https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&current_weather=true")

    })
    .then(function(response){
        return response.json()
    })
    .then(function(weather){
        const temp = weather.current_weather.temperature
        const wind = weather.current_weather.windspeed
        result.textContent = "Temperature: " + temp + "°C | wind: "+ wind +" km/h"
    })
})
