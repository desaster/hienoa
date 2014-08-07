#!/usr/bin/env python
# Copyright (c) 2001-2014 Upi Tamminen <desaster at gmail>
# See the COPYRIGHT file for more information

# hienoa (0.53) theme validator

import sys, string

available_formats = [
    'ACTION',
    'BANNER',
    'CHANNEL_SIGNOFF',
    'CONFIG_TITLE',
    'CTCP_CHANNEL',
    'CTCP_REPLY',
    'CTCP_USER',
    'DCC_CHAT',
    'DCC_COMPLETED',
    'DCC_CONNECT',
    'DCC_LOST',
    'DCC_OFFER',
    'DCC_OFFER_CHAT',
    'DCC_REQUEST',
    'HILIGHT_NOTIFY',
    'INPUT_PROMPT',
    'INVITE',
    'JOIN',
    'KICK',
    'KICK_USER',
    'KILL',
    'LEAVE',
    'MODE',
    'MSG',
    'NAMES_BOTTOM',
    'NAMES_NONOP',
    'NAMES_OP',
    'NAMES_ROW',
    'NAMES_TOP',
    'NAMES_VOICE',
    'NICK',
    'NOTICE',
    'NOTIFY_SIGNOFF',
    'NOTIFY_SIGNON',
    'PUBLIC',
    'PUBLIC_HL',
    'PUBLIC_MSG',
    'PUBLIC_MSG_HL',
    'PUBLIC_NOTICE',
    'PUBLIC_OTHER',
    'PUBLIC_OTHER_HL',
    'SEND_ACTION',
    'SEND_CTCP',
    'SEND_DCC_CHAT',
    'SEND_MSG',
    'SEND_NOTICE',
    'SEND_PUBLIC',
    'SERVER_NOTICE',
    'STATUS_AWAY',
    'STATUS_CHANMODE',
    'STATUS_CHANNEL',
    'STATUS_CHANOP',
    'STATUS_CLOCK',
    'STATUS_CPU_SAVER',
    'STATUS_DCC',
    'STATUS_HOLD',
    'STATUS_HOLD_LINES',
    'STATUS_IDLE',
    'STATUS_IRCOP',
    'STATUS_LAG',
    'STATUS_LINE',
    'STATUS_LINE1',
    'STATUS_LINE2',
    'STATUS_MAIL',
    'STATUS_NICK',
    'STATUS_NOTIFY',
    'STATUS_OVERWRITE',
    'STATUS_PASTE',
    'STATUS_QUERY',
    'STATUS_SCROLLBACK',
    'STATUS_SERVER',
    'STATUS_UMODE',
    'STATUS_UPTIME',
    'STATUS_VOICE',
    'TIMESTAMP',
    'TOPIC',
    'TOPIC_CHANGE',
    'TOPIC_EMPTY',
    'TOPIC_SETBY',
    'TOPIC_UNSET',
    'WALLOP',
    'WHO',
    'WHO_END',
    'WHOIS_AWAY',
    'WHOIS_CHANNELS',
    'WHOIS_END',
    'WHOIS_HEADER',
    'WHOIS_IDLE',
    'WHOIS_IRCNAME',
    'WHOIS_NICK',
    'WHOIS_OPER',
    'WHOIS_SERVER',
    'WHOIS_USERLIST',
    'WHOWAS_END',
    'WHOWAS_HEADER',
    'WHOWAS_IRCNAME',
    'WHOWAS_NICK',
    ]

def validate(filename):
    theme = open(filename, "r")
    lines = theme.readlines()
    used_formats = []
    for line in lines:
	words = string.split(line)
	if not len(words): continue
	if words[0] != "format": continue
	if words[1][0] == '-':
	    if len(words) > 2:
		print filename + ":", words[1][1:],
		print "is disabled with \"-\", but has a format string"
	    used_formats.append(words[1][1:])
	else:
	    used_formats.append(words[1])
    for format in used_formats:
	if not available_formats.count(format):	
	    print filename + ":", format, "is not valid"
    for format in available_formats:
	if not used_formats.count(format):	
	    print filename + ":", format, "is missing"
    theme.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
	print "Usage: checktheme.py <theme>"
	sys.exit(0)
    validate(sys.argv[1])

# vim: set ai tw=75 sw=4:
