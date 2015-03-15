#!/bin/bash

awk '
NR==FNR {
    a[NR]=$0; next
    }
    {
        if (length(a[FNR]) > 0)
            {print a[FNR]"\n"$0}
        else
            {print $0}
    }
    ' song1.txt song2.txt > songremix.txt

    cat songremix.txt
