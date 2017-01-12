<?php
require __DIR__ . '/vendor/autoload.php';

use phpseclib\Crypt\RSA;
use phpseclib\Net\SFTP;

$sftp = new SFTP("domain"); // Just the domain, do not put the dir
                            // It can be a IP as well

$Key = new RSA();

$Key->loadKey(file_get_contents("/route/to/certificate"));

if(!$sftp->login("user", $Key)){
    echo "error!";
}

$sftp->chdir("/some/dir/path");

var_dump($sftp->nlist()); // List all the files in the dir;
