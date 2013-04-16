#!/bin/sh
# Copyright (c) 2000 Upi Tamminen <desaster@dragonlight.fi>
# See the COPYRIGHT file for more information

HIENOA_LIST=". $HOME/hienoa ./hienoa $HOME/.epic/hienoa $HOME/.irc/hienoa"
EPIC_LIST="epic $HOME/bin/epic /usr/local/bin/epic $HOME/epic irc "

function hienoa {
    for i in $HIENOA_LIST
    do
	if [ -f "$i/hienoa.irc" ]
	then
	    exec $* -B -l $i/hienoa.irc
	fi
    done
    echo "hienoa not found"
}

for i in $EPIC_LIST
do
    if ($i -v | grep "EPIC4") >/dev/null 2>&1
    then
	hienoa $i $*
	exit
    fi
done

echo "hienoa needs ircII-EPIC4 to run, visit http://www.epicsol.org"

# vim: set ai tw=75 sw=4:
