# Responsive images
## Udacity course

* [link]()

## Developer set up

> All this set up is made by using Google Chrome on both, computer and mobile

We have to enable developer mode on our andoroid device. (See your device
manual to achieve this).

Conect the phone to your computer by an usb.

Open chrome on your device.

On your computer, open chrome and type `chrome://inspect` in your navigation
bar.

## See the naural resolution for an image

1. By selectin an `<img>` and then typing `$0.naturalWidth` in the chrome
console

2. Just hover an `<img>` on the chrome inspector

## Bits and pixels

Total bits = prixels x bits per pixel

This means that we'll try to follos ->  
`less pixels * better compression = less bytes`

> lowest possible quality and the smallest size as possible.

## Relative sizing

* We need to avoid the images to resize up, cause it will turn into a pixeled
and blurred img in larger displays. Set `max-width: 100%` to let the image to 
size down but not size up.

* With `calc` we can make calculus mixin relative and absolute css values.
e.g: `width: calc(100% - 10px)/2` This will apply a 50% width minus the 10px

## Less Well Known Css Units

* vh -> viewport heigh 
* vw -> viewport width
* vmin -> is equal at the minimum of the other 2 units in the current display
* vmax -> same as *vmin* but for the maximum value.

## Raster And Vector images
* *Raster* -> Images compounded by a grid of pixels (Like the images from a 
camera)
* Vector -> Images defined by a set of lines, shapes, etc.

The advanteage of a vector img is that a browser can render it at any size 
without quality degradation.

## File formats

Preference in use: 
SVG > PNG > JPEG

## Compression, Optimization and Automation

* ImageMagick
* Grunt
    - [Getting started with grunt](https://gruntjs.com/getting-started)
    - [grunt-responsive-image](https://addyosmani.com/blog/generate-multi-resolution-images-for-srcset-with-grunt/)
* ImageOptim (Mac only)
    - [installation](http://cactuslab.com/imagemagick/)
* Trimage - Similar to ImageOptim (Windows, Mac, Linux)

The lesson 14 has several links to this resources (link to lesson)[https://classroom.udacity.com/courses/ud882/lessons/3520939843/concepts/35820386070923]

## Check web img optimization

Using [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)

There's also a pluggin for grunt -> [grunt-pagespeed](https://www.npmjs.com/package/grunt-pagespeed).

## Cover and contain

* *COVER* : The image is sized so that it is as large as possible while still
being completely cisible inside its container
* *CONTAIN* The image is sized so that it is as small as possible while still
completely filling its container.

## Unicode characters

You have to set your webpage to use UTF-8

```html
<meta charset=utf-8>
```

 * [List of unicode characters](https://unicode-table.com/en/)

 ## Icon fonts

 * [Zocial](http://zocial.smcllns.com/)
 * [Font Awesome](http://fortawesome.github.io/Font-Awesome/)
 * [We Love Icon Fonts!](http://weloveiconfonts.com/)
    - List of available icon fonts.
 * [Icon fontos on CSS-tricks](https://css-tricks.com/examples/IconFont/)
 * [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
    - Stands for *Accessible Rich Internet Applications*
    - Set of attributes for markup that screen-readers can understand.
    - Some attributes examples: **aria-hidden**, **role**

## SVG and data URIs

For reducing the number of requests to the server, we can add to our markup
*inline svg* and/or *data uri*(a.k.a: img encoded in base64)

Can be inlined in css.

Interesting link: [SVG optimiser](http://petercollingridge.appspot.com/svg-optimiser)

## srcset and sizes attributes

Allows the browser in the html which image has to download by specifing in advance
the information that a browser doesn't know. It is image sizes and display
relative of the viewport.

```html
<!-- 
According to the resolution of the screen. 1x and 2x refers to the pixel density
of the screen.

We keep adding the `src` default attribute as a fallback in case the browser
doesn't have support for srcset
-->
<img src="wallaby_1x.jpg" srcset="wallaby_1x.jpg 1x, wallaby_2x.jpg 2x" alt='Wallaby'>

<!-- 
Width width ( the `w` represents the image size not the viewport width, so
in the example small.jpg is 500px wide and large 1000 px )

The sizes attribute allows us to set media-queries to tell the browser how
the image will be displayed in the viewport (this has to match to the actual
media-queries for the image in our css to work propperly)
-->
<img src="small.jpg" 
    srcset="small.jpg 500w, large.jpg 1000w" 
    sizes="(min-width: 36em) 33.3vw,
           100vw"
    alt='Wallaby'>

```

We can check the resolution of our screen by typing in the devtool:
`window.devicePixelRatio`

Notice we cant mix `w` and `x` in the srcset

A great article where this is explained: [Srcset and sizes](http://ericportis.com/posts/2014/srcset-sizes/)

For improve browser support, there's a [polyfill](https://github.com/scottjehl/picturefill)

### Calculating the device pixel ratio

Suppose a smart phone has a screen with a physical pixel size of 180 pixels per inch (ppi). Calculating the device pixel ratio takes three steps:

    1. Compare the actual distance at which the device is held to the distance for the reference pixel.

     Per the spec, we know that at 28 inches, the ideal is 96 pixels per inch. However, since it's a smart phone, people hold the device closer to their faces than they hold a laptop. Let's estimate that distance to be 18 inches.

    2. Multiply the distance ratio against the standard density (96ppi) to get the ideal pixel density for the given distance.

    idealPixelDensity = (28/18) * 96 = 150 pixels per inch (approximately)

    3. Take the ratio of the physical pixel density to the ideal pixel density to get the device pixel ratio.

    devicePixelRatio = 180/150 = 1.2

[source](https://www.html5rocks.com/en/mobile/high-dpi/)

So in summary the device pixel ratio is the ratio between the pixel density
a device should have ideally according to the distance is held and the actual
pixel density of the device.