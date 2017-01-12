PHP is a blocking language, so there aren't async calls. However if you 
don't care about the server response there are 3 possible approaches.
Which to chose it's up of your performance needs and system config.:

* [fsockopen](http://php.net/manual/en/function.fsockopen.php)

```php
<?php
private function request($body) {

    $protocol = "ssl";
    $host = "api.segment.com";
    $port = 443;
    $path = "/v1/" . $body;
    $timeout = $this->options['timeout'];

    try {
      # Open our socket to the API Server.
      $socket = fsockopen($protocol . "://" . $host, $port,
                          $errno, $errstr, $timeout);

      # Create the request body, and make the request.
      $req = $this->create_body($host, $path, $content);
      fwrite($socket, $req);
      # ...
    } catch (Exception $e) {
      # ...
    }
}

```
This has a bit of delay though (Over 300 ms), due to the TLS Handsake.

* non blocking sockets (`socket_set_nonblock`)

it's possible to use **socket_set_nonblock** for a no blocking socket at its
creation. However you still need ~100 ms for being able to write into it

* fork a `curl` process

using the php `exec` comand to make the *curl* operation in another thread in the
server.

This works but you need some permission level at your server for doing this. And
doing this too often my slow down the server if there are too many concurrent forks


# Multiple calls to an API

I was searching this because of an implementation I need to make for performance
monitoring. For this particular case I found very interesting these aproches because
afect so little on code performance.

* Write logs locally and then send them in a unique call to the service
* Make use of a helper object and send the results in its `__destruct()`

```
<?php
class Analytics_SomeConsumer {

  public function __construct() {
    $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    socket_set_nonblock($this->socket);
    socket_connect($this->socket, $this->host, $this->port);
    $this->queue = array();
  }

  public function __destruct() {
    $payload = json_encode($this->queue);
    # ... // wait for socket to be writeable
    socket_write($this->socket, $payload);
    socket_close($this->socket);
  }

  public function track($item) {
    array_push($this->queue, $item);
  }
```

All what I've written here is a summarized version of [Calvin French-Owen blog post](https://segment.com/blog/how-to-make-async-requests-in-php/)

