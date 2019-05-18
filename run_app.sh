#!/usr/bin/env bash

export FLASK_APP=./zeus
export FLASK_ENV=development

echo $FLASK_APP $FLASK_ENV
pip install -e
flask run

