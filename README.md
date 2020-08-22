# Fractional π
Calculate fractional approximations of pi from continued fractions.

## Usage
Clone this repo, run the script. You know the deal:

```
$ git clone https://github.com/slightknack/pi
$ cd pi
$ python3  pi.py
```

It'll print out the indexes of some accurate approximations, 
then prompt you to enter one.
Try something like `2` to get `22 / 7`, or `4` for the Milü approximation.

## Learn More
Check out this [blog post by Atrix256, "Irrational Numbers"](https://blog.demofox.org/2020/07/26/irrational-numbers/).
The method used here is the same one as the method presented there.
This script is really nothing more than a toy that I used 
to explore the [Simple continued fraction expansion of Pi](https://oeis.org/A001203).

For information on how this sequence is computed, read the paper titled
["Computation of Continued Fractions Without Input Values"](https://www.ams.org/journals/mcom/1995-64-211/S0025-5718-1995-1297479-9/S0025-5718-1995-1297479-9.pdf)
by P. Shiu.
