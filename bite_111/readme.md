# Bite 111. Use the ipinfo API to lookup IP country

## Description

In this Bite you will use the `requests` library to make a GET request to the ipinfo service.

Use `IPINFO_URL` and parse the (2 char) country code from the obtained json response.

Note how we mocked out the `requests.get` call in the tests, you can see another example of this in our [Parsing Twitter Geo Data and Mocking API Calls by Example](https://pybit.es/twitter-api-geodata-mocking.html) article.

Querying APIs is a common need so this should become second nature :) - enjoy!
