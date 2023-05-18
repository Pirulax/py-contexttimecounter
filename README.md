A little context time counter.
Use it as:

```py
from contexttimecounter import ContextTimeCounter

with ContextTimeCounter() as ctc:
    # ...
print(f"Time spent in the context: {ctc.time_total:.4f}")
```
