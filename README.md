# PhoenixOCR
Standalone OCR for analyzing direct video captures of PIU Phoenix score screens

# Environment:
Python 3.10.7
EasyOCR 1.6.2 (installed using pip 22.2.2)

# Running:

(Examples)
```
# running:
python run.py samples/etude.png --mode fast

# returns:
{
    "P1": {
        "Score": 834414,
        "Perfect": 931,
        "Great": 307,
        "Good": 72,
        "Bad": 16,
        "Miss": 24,
        "MaxCombo": 183
    },
    "P2": {
        "Score": 827441,
        "Perfect": 960,
        "Great": 235,
        "Good": 79,
        "Bad": 50,
        "Miss": 26,
        "MaxCombo": 171
    }
}
```

```
# running:
python run.py -u https://cdn.discordapp.com/attachments/1159343966890766437/1165890065772335175/etude.png --mode scores

# returns:
{
    "P1": {
        "Score": 834414
    },
    "P2": {
        "Score": 827441
    }
}
```

```
# running:
python run.py samples/versailles.png --mode scores

# returns:
{
    "P1": {
        "Score": 951257
    },
    "P2": {
        "Score": null
    }
}
```
