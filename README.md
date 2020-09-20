# CRUD-SQLlite-note-app
Simple CRUD for terminalbased note taking.



## Requirements to run the APP

The APP is designed for Linux terminals running Python 3.x

* Place the code in the desired directory.
* Create a SQLlite DB file in the same directory
* Use the create statement to make one table with 2 columns.

`CREATE TABLE "notes" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"heading"	TEXT,
	"note"	TEXT
);`

**Pip install :**
* prettytable
* clipboard

## Run the APP

`python3 crp-notes-v0.1.py`

## What happens from here....

Maybe code cleanup and break stuff in various ways.
