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


