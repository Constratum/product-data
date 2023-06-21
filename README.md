# product-data
CSV lists of building product data, as found online or supplied by product manufacturers or distributors.

Install full database using pip:
```
  !pip install git+https://github.com/Constratum/product-data.git
```

Import specific data into python or notebook as pandas df using import function, eg to import Ceiling Tiles.csv:
```
  from product_data import product_data_importer
  tiles = get_df_from_file_name("Ceiling Tiles.csv")
```
