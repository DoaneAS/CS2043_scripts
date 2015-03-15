#!/bin/bash

grep -E -o "(\d{3}.*|[.\(\s]?[\d]{3,4}\)\s\-?)" phone-data.txt