#!/bin/bash

ERRORS=false
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BIN=/usr/bin

declare -A tests
declare -A builds
declare -A running

tests["C"]="$BIN/gcc -fsyntax-only $DIR/c/hello.c > $DIR/logs/gcc.log 2>&1"
builds["C"]="$BIN/gcc $DIR/c/hello.c -o $DIR/c/hello >> $DIR/logs/gcc.log 2>&1"
running["C"]="$DIR/c/hello"

tests["C++"]="$BIN/g++ -fsyntax-only $DIR/cpp/hello.cpp > $DIR/logs/cpp.log 2>&1"
builds["C++"]="$BIN/g++ $DIR/cpp/hello.cpp -o $DIR/cpp/hello >> $DIR/logs/cpp.log 2>&1"
running["C++"]="$DIR/cpp/hello"

tests["Java"]="true"
builds["Java"]="$BIN/javac $DIR/java/hello.java > $DIR/logs/java.log 2>&1"
running["Java"]="$BIN/java -cp $DIR/java HelloWorld"

tests["Python"]="$BIN/python2 -m py_compile $DIR/python/hello.py > $DIR/logs/python.log 2>&1"
builds["Python"]="true"
running["Python"]="$BIN/python2 $DIR/python/hello.py"

tests["Ruby"]="$BIN/ruby -c $DIR/ruby/hello.rb > $DIR/logs/ruby.log 2>&1"
builds["Ruby"]="true"
running["Ruby"]="$BIN/ruby $DIR/ruby/hello.rb"

function c_cpp_build()
{
  for i in "${!tests[@]}"
  do
    eval ${tests[$i]}
    RET=$?

    if [ $RET -eq 0 ]
    then
      eval ${builds[$i]}
      RET=$?
      if [ $RET -eq 0 ]
      then
        printf "%8s Program: Build success. Running: " $i
        eval ${running[$i]}
      else
        printf "%s Program: No syntax errors were detected, but no compilation were done.\n" $i
        ERRORS=true
      fi
    else
      printf "%s Program: Syntax error in the house!\n" $i
      ERRORS=true
    fi
  done

  if $ERRORS
  then
    $BIN/python2 $DIR/sms.py +37369614191 "IDE. Errors happened. Check the logs."
  fi
}

c_cpp_build


