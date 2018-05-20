!!! danger "Important note regarding the use of Weather Underground data"
    The open-source software that ThingPulse provides for its devices relies on weather data pulled from Weather Underground. The standard setup process involves creating a Wunderground API key (documented below). The usage was free for up to 500 requests per day or 10 requests per minute.
    
    In the [evening of May 15th](https://apicommunity.wunderground.com/weatherapi/topics/weather-underground-api-changes) The Weather Company, a subsidiary of IBM, announced that [it will no longer provide free weather API keys](https://www.wunderground.com/weather/api). There was no prior announcement and the change became effective immediately. It is unclear for how long existing keys will still be valid. As not even the tens of thousand of weather station owners who deliver their data to Wunderground for free will get a key to read their data back the uproar in the community is big.
    
    For you this means that unless you already obtained a key from Wunderground you can not use the ready-made software for your ThingPulse device. We are very sorry, and furious, about this development but our hands are tied. The promise to our customers is that we will be working hard and not rest until we can offer an adequate alternative integration. We started working on a new service integration on May 19th.
    
!!! danger
	So, again, as per the note above the instructions below became effectively void on May 15th. They remain here for the time being until the dust over this issue has fully settled.

As your device will be displaying data from [Weather Underground](https://en.wikipedia.org/wiki/Weather_Underground_(weather_service) ) 
you need an "API key" from them. It uniquely ties requests from your device(s) to your account and ensures that the 
number of requests remains withing your allotted quota.

- Go to [https://docs.thingpulse.com/go/create-wunderground-key](/go/create-wunderground-key)
- Select the "Stratus Plan".
- Take note of the "Developer" rate limits and hit the "Purchase Key" (even if you do not actually purchase) button. 
![Wunderground API plan overview](/img/how-tos/wunderground-API-key_plan-overview.png)
- Fill in email and password to sign-up for a new account
![Wunderground sign up](/img/how-tos/wunderground-API-key_sign-up.png)
- Fill in required information about how you intend to use the API key
![Wunderground sign up](/img/how-tos/wunderground-API-key_info.png)

Once the API key is created you can come back to this page any time to regenerate or edit it.

If the instructions above are not detailed enough or if you would like more visual guidance there is a good video how-to at [https://youtu.be/yQHrnmeWTRk](https://youtu.be/yQHrnmeWTRk).
