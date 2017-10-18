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

# 5. New number and Math features

## Number.toString(radix)

```js
255..toString(16) // 'ff'
4..toString(2) // '100'
8..toString(8) // '10'
```

The double dots are necessary so that the dot for property access isn't confused with a decimal dot.

> Note: Even though this is not a ES6 feature, I found it interesting

## Number.parseInt()

Supports hexadecimal number literals (but not for binary or octal literals)

## Number.isFinite & Number.isNaN

Do not coerce their parameters to be numbers whereas the global functions do

## Number.EPSILON

Constant used for float comparitions with error margin (the problem of sum up 0.1 + 0.2)

The number represents a reasonable margin of error for comparing float point numbers.

The new way of comparing float numbers is:

```js
function epsEqu(x, y) {
    return Math.abs(x - y) < Number.EPSILON;
}
console.log(epsEqu(0.1+0.2, 0.3)); // true
```

## Safe integers

Due to how mathmatical integers are represented once we riched -2^53 or 2^53, JavaScript can only represent even numbers.

```
> Math.pow(2, 53)
9007199254740992

> 9007199254740992
9007199254740992
> 9007199254740993
9007199254740992
> 9007199254740994
9007199254740994
> 9007199254740995
9007199254740996
> 9007199254740996
9007199254740996
> 9007199254740997
9007199254740996
```

JavaScript now provides ways of knowing if we reached the limit:

* Number.isSafeInteger(number)
* Number.MIN_SAFE_INTEGER
* Number.MAX_SAFE_INTEGER

## JavaScript 53 bit range

Javascript has only precision for 53 bits integers which is a problem when 64 bit integer are needed. The only way to work this around is to use a library such as decimal.js

# New string features

## String templates

Allows to:
* Use variables in strings
```js
const first = 'Jane';
const last = 'Doe';
console.log(`Hello ${first} ${last}!`);
    // Hello Jane Doe!
```

* Multilines strings
```js
const multiLine = `
This is
a string
with multiple
lines`;
```

* Raw string (neither special chars or escapes are interpreted)
```js
const str = String.raw`Not a newline: \n`;
console.log(str === 'Not a newline: \\n'); // true
```

## Checking for inclusion

```js
'hello'.startsWith('hell')
// true

'hello'.endsWith('ello')
// true

'hello'.includes('ell')
// true
```

## Repeat strings

```js
'doo '.repeat(3) // 'doo doo doo '
```

# 7. [Symbols](http://exploringjs.com/es6/ch_symbols.html)

New js primitive.

Build with the Symbol factory `Symbol()`. You can pass a string as a tag `Symbol("hello")`.

Symbols are unique so: `Symbol() !== Symbol()`

One of their great uses is for avoiding method clashes since each symbol is unique

```
const _counter = Symbol('counter');
const _action = Symbol('action');
class Countdown {
    constructor(counter, action) {
        this[_counter] = counter;
        this[_action] = action;
    }
    dec() {
        let counter = this[_counter];
        if (counter < 1) return;
        counter--;
        this[_counter] = counter;
        if (counter === 0) {
            this[_action]();
        }
    }
}
```

You can coerce a Symbol to a string representation: `String(Symbol('hello')) //'hello'`

There are several well-known symbols such as `Symbol.iterator`. Adding this symbol as key property for a method, makes the 
object iterable through for-of (it's the method that is going to be called).

# 8. Template Literals
There are template literals a tagged template

```js
const author = 'Edgar'
console.log(`${author} made this string`) // Edgar made this string
```

Tagged templates are function which are always invoked with a template string:

```
function tagFunction(templateStrings, ...substs)
```

The way of calling it: 

```
const author = 'Edgar'
tagFuntion`This is a tagged literal made by ${author}
```

The tag function will recieve as parameter (["This is a tagged literal made by", ""], 'Edgar'). Then the function can have any implementation and return whatever

> There's always 1 more template string than substitutions

# 9. [Variables and scoping](http://exploringjs.com/es6/ch_variables.html)
ES6 changhes with `let` and `const` its function scope to block scope for variables.

`let` works as var but with the block scope

`const` has other restrictions. Has to be inizialized right with its definition. Its value can't change afterwards.

The hoisting in `let` and `const` is temporal dead zone. This means that you can access to it ever since it has ben declared. If it has not been assigned any value, it'll return undefined. If we try to access to one variable declared with `let` or `const`, we'd get a `ReferenceError`. [Further reading](https://stackoverflow.com/a/33198850)

`const` forbids being assigned another value, but doesn't makes the value unmutable. For example if we assign an object we can add to it properties. For avoiding this we have to make the object unmutable with `Object.freeze(object)`

# 10. Destructuring

No notes for this chapter. It's all explained through clear examples so just check out the book =).

# 11. Parameter handling

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
* clash -> chocar/colisionar
* shallow -> poco profundo
