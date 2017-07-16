# MovieLens Data Extractor

This program allows you to clean the data of Movielens 10M100k dataset and create a small sqlite database and then data can be extracted through the other program on the basis of Tags and Category.

## movielens.py

This Script will clean the dataset and create a simplified 'movielens.sqlite' database. This program is using the 10m dataset from movielens. There are three files in dataset movies.dat, ratings.dat and tags.dat.

### movies data file structure

UserID::MovieID::Rating::Timestamp ---- For .dat files

movieId,title,genres --- For new .csv files

### Ratings data file structure

UserID::MovieID::Rating::Timestamp ---- For .dat files

userId,movieId,rating,timestamp ----- For new .csv files

Ratings are made on a 5-star scale, with half-star increments.

### Tags data file structure

UserID::MovieID::Tag::Timestamp ----- For .dat files

userId,movieId,tag,timestamp ---- For new .csv files

## moviextractor.py

This script will extract data from 'movielens.sqlite' according to the category and tags that will be entered by the user. This will give the movie name and their average ratings given by movielens users.
  
## Requirements

Movielens 10M dataset: https://grouplens.org/datasets/movielens/

You should install the SQLite browser to view and modify the databases from:
http://sqlitebrowser.org/

Put the dataset in same folder with the program then run movielens.py and to extract movies run moviextractor.py.
 
