# 🎬 Movies dataset template

A simple Streamlit app showing movie data from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movies-dataset-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### Extract RUT numbers

Use the `rut_extractor.py` script to scan a folder of text files and collect RUT numbers:

```bash
python rut_extractor.py --input-dir ./rut_files --output-file worldoffice.txt
```

Once the file has been generated, upload `worldoffice.txt` to World Office.
