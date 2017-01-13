In your library write this in a composer.json file:
```js
{
    "name": "vendor/your_library_name",
    "version": "dev-master",

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



[More Info](https://knpuniversity.com/screencast/question-answer-day/create-composer-package)
