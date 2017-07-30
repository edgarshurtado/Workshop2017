[Exploring ES6](http://exploringjs.com/es6/)

# 1. About ECMAScript

The language is evolved by the TC39 (Technical Committee 39). Who define the new specifications for
each release.

JavaScript official name is ECMAScript since 'Java' is trademarked by Oracle. It's named ECMAScript after 
the Ecma international organization which is a standard organization that manages the language standard.

Javascript has the commitment of "One Javascript" which mean no version of the language will not be compatible backwards.

ECMAScript releases:
* ECMASCript1 (1997)
* ECMASCript2 (1998)
* ECMASCript3 (1999). Introduced a lot af new features
* ECMAScript4 (never released)
* ECMASCript5. A superset of ES3 (originally was ES3.1) but less ambitious than what ES4 was. It's the version most browsers support today.
* ECMAScript6/ECMAScript2015 (2015). This book. Is a superset of ES5 (this secures forward compatibility. All ES5 code is ES6 code). Its official name is ECMAScript2015, however everyone knows it as ES6
* ECMAScript2016. From this point on, the language will recieve small yearly updates and will be named after its year release

[Kangax’ ES6 compatibility table](http://kangax.github.io/compat-table/es6/)

# 2. Chapter skiped

# 3. One JavaScript: Avoiding versioning en ECMAScript6

JavaScript follows the 'One JavaScript' principle wich means that no breaking 
changes will be added and it will be always backwards-compatible.

The reasons behind it:
* Allows browser engines to update allowing old code to still run. 
* Better transition for programmers to start using new features.

What One JavaScript can't do:
* Delete functionalities
* Change functionalities
* Remove some quirks of the language

What One JavaScript can do:
* Introduce new features
* Improve functionalities

Strict mode was introduced for cleaning up the language, however it meant having
2 versions of JavaScript (Strict-mode code will break in sloopy-mode and viceversa).
Thus, for returning to the 'One JavaScript' philosophy, the development of 
ES6 has been forced to add the new functionalities to both strict mode and 
sloppy mode.

# 4. Core ES6 features

This chapter lists all the new core features of the language comparing they with
how would we get this done in ES5. As a sumarize: ES6 syntactic sugar is great =D.

# New vocabulary
* trademark -> marca registrada
* inception -> comienzo
* stake holders -> interesados
* sloppy -> descuidado/chapucero
* w.r.t. -> with respect to/ with regard to/ with reference to
* pitfall -> obstáculo/dificultad/inconveniente
* bloated -> hinchado/inflado
* brittle -> frágil/transitorio
* clutter -> follón/lío
* hassle -> dificultad/confusión
* quirk -> peculiaridad/singularidad
* clumsy -> torpe/desastrado/patoso
* coerce -> obligar/forzar

