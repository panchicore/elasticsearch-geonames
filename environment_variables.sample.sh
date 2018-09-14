#!/usr/bin/env bash

export ES_GEONAMES_HOST=http://localhost:9200/
export ES_GEONAMES_USER=
export ES_GEONAMES_PASSWORD=
export ES_GEONAMES_INDEX=geonames

# dont modify this if you download the files in the default location:
export ES_GEONAMES_FILE=$(pwd)\/tmp\/allCountries.txt
export ES_GEONAMES_BOUNDINGBOXES_FILE=$(pwd)\/tmp\/boundingbox.txt
export ES_GEONAMES_POLYGONS_FILE=$(pwd)\/tmp\/allshapes.txt
export ES_GEONAMES_COUNTRYINFO_FILE=$(pwd)\/tmp\/countryInfo.txt

