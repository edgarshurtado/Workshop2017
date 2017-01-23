* How to send a POST request with body

This is an example of how to send a post request with a body request.
It's based on [this blog post](http://web.ontuts.com/tutoriales/aprendiendo-a-utilizar-la-libreria-curl-en-php/)

```php

$jsonString = file_get_contents("randomFile.json"); 

$curlChannel = curl_init();
curl_setopt($curlChannel, CURLOPT_URL , $url);
curl_setopt($curlChannel, CURLOPT_POST , true);
curl_setopt($curlChannel, CURLOPT_POSTFIELDS , $jsonString);

curl_exec($curlChannel);
curl_close($curlChannel);
```
