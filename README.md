# rsa-wiener-attack

A Python implementation of the [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack) on RSA public-key encryption scheme.

It uses some results about continued fractions approximations to infer the private key from public key in the cases the encryption exponent is too small or too large.


## Usage

Enter your `e`, `n` (and maybe `c`) in `atack.py` and run `python attack.py`.


## Credits

Based on [rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack) by @pablocelayes.