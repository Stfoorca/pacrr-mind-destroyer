#!/usr/bin/env bash
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

START=$(date +%s.%N)


python -m prepare
python -m corpus_gen
python -m train_w2v
python -m embedding_matrix

END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo finished within $DIFF