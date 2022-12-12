#!/bin/bash

if [ -d ".venv" ]; then
  echo "Active virtualenv"
  source .venv/bin/activate
else
   echo ".venv does not exist, let's create it"
   python3 -m venv .venv
   source .venv/bin/activate
fi
echo "Install dependencies"
pip install -r requirements-dev.txt
