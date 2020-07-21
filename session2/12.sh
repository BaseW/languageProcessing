#!/bin/sh

# col1の抽出と比較
cut -f 1 popular-names.txt > col1_test.txt
diff --report-identical-files col1.txt col1_test.txt

# col2の抽出と比較
cut -f 2 popular-names.txt > col2_test.txt
diff --report-identical-files col2.txt col2_test.txt