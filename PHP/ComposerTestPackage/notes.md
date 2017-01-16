In your library write this in a composer.json file:
```js
{
    "name": "vendor/your_library_name",
    "version": "dev-master",
    "autoload": {
    	"psr-4" : {
		"Vendor\\YourLibraryName\\" : "src"
	}
    }

    "require": {
        "some/requirement_vendor": "^1.22"
    },
    "authors": [
        {
            "name": "Your Name",
            "email": "you_email@fakemail.com"
        }
    ]
}
```

> Some notes:
* add the autoload property for loading your own classes. This is
a requirement for easily load your own clases at the *test* folder.
* The namespace indicated at the autoload has to end with *\\*. (This is
a composer requirement)
* Any change at *composer.json* which affects the autoloader won't be
applied since `composer -dump-autoload` is executed in terminal.

In your project (in which you want your library) write as follows
in a composer.json file:

```js

{
	"repositories": [{
		"type": "vcs",
		"url": "repository url"
	}],
	"require": {
		"vendor/your_library_name": "dev-master"
	},
	"minimum-stability": "dev",
	"prefer-stable": true
}
```

> As long as you are developing it's usually seen the package as version `dev-master`. Once you
start to make versions, you can point out the version tag directly. This is specified in the 
composer docs and blogs listed below. Not tested by me though.


* [Create Composer Package](https://knpuniversity.com/screencast/question-answer-day/create-composer-package)
* [Autoload. Composer Docs](https://getcomposer.org/doc/04-schema.md#autoload)
* [Creating your first Composer Packagist Package](http://blog.jgrossi.com/2013/creating-your-first-composer-packagist-package/)
