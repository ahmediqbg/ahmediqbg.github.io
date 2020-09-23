#!/usr/bin/env bash

# Run to update all Bandcamp data yml files.

pipenv run python pull-bandcamp-purchased-albums-to-data.py
pipenv run python pull-bandcamp-wishlisted-albums-to-data.py