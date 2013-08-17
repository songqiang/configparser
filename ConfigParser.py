#! /usr/bin/env python

#
# Gmail Attachment Archiver
# Song Qiang <keeyang@ustc.edu>, 2013
#

class ConfigParser:
    """
    An alternative configure file parsor for python
    """
    def read(self, fn):
        """
        read configuration file
        """
        self.items = {}
        for line in open(fn):
            line = line.strip()
            comment_start = line.find("#")
            if comment_start != -1:
                line = line[:comment_start]

            fields = []
            if line.find("=") != -1:
                fields = line.split("=", 1)
            elif line.find(":") != -1:
                fields = line.split(":", 1)
            elif line.find("\t") != -1:
                fields = line.split("\t", 1)
            elif line.find(" ") != -1:
                fields = line.split(" ", 1)

                
            if len(fields) == 2:
                fields = [i.strip() for i in fields]
                if fields[0] and fields[1]:
                    self.items.update([(fields[0], fields[1])])
    
    def __init__(self, fn):
        self.read(fn)

