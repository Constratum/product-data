# product-data
CSV lists of building product data, as found online or supplied by product manufacturers or distributors.

Install full database using pip:
```
  !pip install git+https://github.com/Constratum/product-data/product_data.git
```

Import specific data into python or notebook as pandas df using import function, eg to import Ceiling Tiles.csv as a dataframe:
```
  from product_data import constratum_product_data_in
  tiles = constratum_product_data_in.get_df_from_file_name("Ceiling Tiles.csv")
```
