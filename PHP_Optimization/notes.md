Before further reading see the following quote:

> The patient reader who is still wondering why so much emphasis is given to
discussing non-PHP issues is reminded that PHP is a fast language, and many of
the likely bottlenecks causing slow speeds lie outside PHP
[source](http://phplens.com/lens/php-book/optimizing-debugging-php.php#squid).

Seems that the better way for boost php performance is by implementing some
sort of cache.

# For loop optimization

```php
// Instead of something like this
for ($j=0; $j<sizeof($arr); $j++)
    echo $arr[$j]."<br>";

// use this
for ($j=0, $max = sizeof($arr), $s = ''; $j<$max; $j++)
  $s .= $arr[$j]."<br>";

echo $s;
```

This avoids re-evaluate `sizeof($arr)` each time. Also avoids to call the
function `echo` (which can be a bit )

# Monitoring PHP

For monitoring your php app there [are several Aplication Performance Managers](https://haydenjames.io/50-top-server-monitoring-application-performance-monitoring-apm-solutions/)
called APM.

# Interesting resources:

* [A HOWTO on Optimizing PHP](http://phplens.com/lens/php-book/optimizing-debugging-php.php)
* [What are the best methods for optimizing PHP/MySQL code for speed without caching?](https://www.quora.com/What-are-the-best-methods-for-optimizing-PHP-MySQL-code-for-speed-without-caching)
actually the best responses are about do caching.
* [Pear: Extension for caching](https://pear.php.net/index.php)