# What's xcache
It's an opcode cacher.

OpCode Caches are a performance enhancing extension for PHP. They do this by
injecting themselves into the execution life-cycle of PHP and caching the
results of the compilation phase for later reuse. Its use is always recomended
even though it has an extra storage cost and some overhead at the restarting
of Apache and such operations that will cause a recaching.
[source](https://support.cloud.engineyard.com/hc/en-us/articles/205411888-PHP-Performance-I-Everything-You-Need-to-Know-About-OpCode-Caches).


# Interesting sources
* [xCache: Mejorando la potencia de PHP (I)](https://www.genbetadev.com/php/xcache-mejorando-la-potencia-de-php-i) (Spanish)
* [Install XCache to Accelerate and Optimize PHP Performance](http://www.tecmint.com/install-xcache-to-accelerate-and-optimize-php-performance/)