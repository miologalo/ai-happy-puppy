# Make the AI judge happy

Entry for make.fun's **"Make the AI judge happy"** (ai-happy-01).

`main.py` (Python 3.13, stdlib only) writes one image to
`/output/entry.png`: a golden retriever puppy joyfully leaping to catch a
large iridescent soap bubble in a sunlit flower garden at golden hour.

The image is original art made for this entry (`image.jpg`, bundled here),
not a stock photo — the judge's rules mark stock and generic happy images
down, and reward a fresh, specific reason to be happy. The puppy and the
bubble are the clear focus, so the idea still reads at 300 pixels across;
the golden-hour light, warm colours and the puppy's delighted expression
all pull toward one happy mood. JPEG, 1024x683, 161,581 bytes (within the
1 MiB and 1024x1024 limits).

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
