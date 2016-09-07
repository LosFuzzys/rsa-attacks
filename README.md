# RSA Attacks

Some attacka on the RSA public-key encryption scheme.

## Wiener's attack

This attack uses the continued fraction method to **expose the private key d when d is small**.

* Key recovery (recover `d` from `e` and `n`)

* Required: 
  * encryption exponend `e` (public key, probably very larger)
  * modulus `n`

* Folder: *wiener*


## Other implementations:

* https://github.com/Ganapati/RsaCtfTool
* https://github.com/rk700/attackrsa
