# Dositeja extractor

Extractor made to make sense of preliminary data for "Dositeja"

## Prerequsites

- `node`
- `python3`
- `pipenv`

## Installation

> `npm install`
> `pipenv install`

## Extracting files

To extract raw text data:

> `node .\index.js > text.txt`

NOTE: newlines are kinda wonky so probs need to do some manual postprocessing

After you've extracted and postprocessed text data run:

> `python main.py`

You should get csv with the desired data in `stipendija.csv` file.

This was made in ~1 hour so it's most likely that it has some bugs.