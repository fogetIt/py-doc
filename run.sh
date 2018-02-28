#!/bin/bash
# @Date:   2018-02-28 10:25:02
# @Last Modified time: 2018-02-28 10:25:04

python -c "import sphinx; exit()" || pip install Sphinx==1.0.1

sphinx-build -b html ./ ./dist/
