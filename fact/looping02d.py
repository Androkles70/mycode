#!/usr/bin/env python3
""" NDE | For - less memory consumption """

with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        svr = svr.rstrips('\n')

        if svr.endswith('org'):
            with open("org-domain.txt", "a")
                srvfile.write(svr + "\n")

        elif svr.endswith('com'):
            with open("com-domain.txt", "a")
                srvfile.write(svr + "\n")
