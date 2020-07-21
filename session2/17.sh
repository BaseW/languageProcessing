#!/bin/sh

cut -f 1 popular-names.txt | sort | uniq > result_test.txt

# Pythonのプログラムで実行、diffで比較するためにソート
python 17.py | sort > result.txt

# 結果の確認
diff --report-identical-files result.txt result_test.txt
