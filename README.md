# linear-pack

A linear materials packing tool. Don't over buy materials, and never cut too short.

I wrote this to take the tedium out of calculating how much stock to
buy when the materials were sold by the lineal foot.

This implements a naive packing algorithm to minimize waste. Bin
packing is NP-complete, so I make no promises that you're absolutely
optimal. But it'll do a quick and pretty damn good job, so that you
don't need to worry when going to the lumber yard or metal shop.

# Usage

```
python scripts/simplepack.py example.txt
```

This is currently hard-coded for 20' lengths with 1" of padding between
cuts.

# Credits

The original source was pulled from (this stackoverflow
answer)[http://stackoverflow.com/questions/7392143/python-implementations-of-packing-algorithm]. It
has been modifed to fit my project needs.

# License

MIT
