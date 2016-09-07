# RSA Attacks

Some attacks on the RSA public-key cryptosystem.

Most of this attacks only work on [Textbook RSA](http://crypto.stackexchange.com/a/1449/12582).

## Wiener's attack

This attack uses the continued fraction method to **expose the private key d when d is small**.

* Key recovery (recover `d` from `e` and `n`) if `d` is small (a large `e` is a good hint this is the case)

* Required: 
  * encryption exponend `e` (public key, probably very larger)
  * modulus `n`

* Folder: *wiener*


## Other implementations:

* https://github.com/Ganapati/RsaCtfTool
* https://github.com/rk700/attackrsa
