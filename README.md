# linear-pack

A linear materials packing tool. Don't over buy materials, and never cut too short.

I wrote this to take the tedium out of calculating how much stock to
buy when the materials were sold by the lineal foot.

This implements a naive packing algorithm to minimize waste. Bin
packing is NP-complete, so I make no promises that you're absolutely
optimal. But it'll do a quick and pretty damn good job.

# Usage

```
    python scripts/simplepack.py example.txt
```


