# Flick

Flick is a streaming service which depicts the basic and simplest nature of we can build a set of streaming services using and language by implementing microservioce approach.
This app is a mini-project for the core subject of 4th trimester MCA.

The structure of the project is as follows:

main

- app.py

- Lists

  - getList.py (list of videos/series/movies)

- Movies

  - getAMovie.py (search for a movie)
  - getMovies.py (get list of movies)

- Shows

  - getAShow.py (search for a show)
  - getShows.py (get list of shows)

- msenv (virtual environment for the streamlit pkg)

## For virtual environment

For creating a virtual environment so that we can streamlit in the system.

The following are the steps:

```
    cd project-folder
```

```
    python -m venv msenv
```

```
    # Windows command prompt
    msenv\Scripts\activate.bat

    # Windows PowerShell
    msenv\Scripts\Activate.ps1

    # macOS and Linux
    source msenv/bin/activate
```

```
    pip install streamlit
```
