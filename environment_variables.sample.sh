#!/usr/bin/env bash

export ES_GEONAMES_HOST=http://localhost:9200/
export ES_GEONAMES_USER=
export ES_GEONAMES_PASSWORD=
export ES_GEONAMES_INDEX=geonames

# dont modify this if you download the files in the default location:
export ES_GEONAMES_CACHE_FEATURECODES=$(pwd)\/dict_featurecodes.csv
export ES_GEONAMES_CACHE_ISOCODES=$(pwd)\/dict_country_isocode.csv
export ES_GEONAMES_CACHE_COUNTRYID=$(pwd)\/dict_country_geonameid.csv
export ES_GEONAMES_CACHE_ADMIN1FEATURE=$(pwd)\/dict_admin1_feature.csv
export ES_GEONAMES_CACHE_ADMIN2FEATURE=$(pwd)\/dict_admin2_feature.csv
export ES_GEONAMES_CACHE_ADMIN1ID=$(pwd)\/dict_admin1_geonameid.csv
export ES_GEONAMES_CACHE_ADMIN2ID=$(pwd)\/dict_admin2_geonameid.csv

export ES_GEONAMES_FILE=$(pwd)\/tmp\/allCountries.txt
export ES_GEONAMES_BOUNDINGBOXES_FILE=$(pwd)\/tmp\/boundingbox.txt
export ES_GEONAMES_POLYGONS_FILE=$(pwd)\/tmp\/allshapes.txt
export ES_GEONAMES_COUNTRYINFO_FILE=$(pwd)\/tmp\/countryInfo.txt

