#!/bin/bash

function sudoku_assert() {
  pip --disable-pip-version-check list | grep "sudoku-cli" >/dev/null
  if [ $? -ne 0 ]; then
    echo "[ERROR][sk_file] pip package sudoku-cli not found."
    exit 1
  fi
}
function sudoku_fold() {
  if [ -z "${1}" ]; then
    echo "[ERROR][sk_file] Missing at least one argument [puzzle]"
    exit 1
  fi
  local puzzle="${1}"
  local tmp="./.tmp.txt"
  echo "${puzzle}" > "${tmp}"
  echo "Solved"
  sudoku "${tmp}" | fold -w9 | sed 's/./&|/6' | sed 's/./&|/3' | awk 'NR==7{print "---+---+---"}1' | awk 'NR==4{print "---+---+---"}1' | awk 'NR==1{print "==========="}1' && rm "${tmp}"
}