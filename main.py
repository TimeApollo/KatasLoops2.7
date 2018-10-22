#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 2.7 Katas Loops.

First exercise in Python printing katas 1 that we learned in Javascript.

author: TimeApollo
"""

sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712, 71, 456, 21, 398, 339, 882, 848, 179, 535, 940, 472]

def main():
    print '1. ----------------------------------'

    for i in range(1,21): print i,

    print '\n2. ----------------------------------'

    for i in range(2, 21, 2): print i,

    print '\n3. ----------------------------------'

    for i in range(1, 21, 2): print i,

    print '\n4. ----------------------------------'

    for i in range(5, 101, 5): print i,

    print '\n5. ----------------------------------'

    for i in range(1,11): print i*i,

    print '\n6. ----------------------------------'

    for i in range(20,0, -1): print i,

    print '\n7. ----------------------------------'

    for i in range(20,0, -2): print i,

    print '\n8. ----------------------------------'

    for i in range(19,0, -2): print i,

    print '\n9. ----------------------------------'

    for i in range(100,0, -5): print i,

    print '\n10. ----------------------------------'

    for i in range(10,0, -1): print i*i,

    print '\n11. ----------------------------------'

    for item in sampleArray: print item,

    print '\n12. ----------------------------------'

    for item in sampleArray: 
        if item%2==0 : print item,

    print '\n13. ----------------------------------'

    for item in sampleArray: 
        if item%2==1 : print item,

    print '\n14. ----------------------------------'

    for item in sampleArray: print item*item,

    print '\n15. ----------------------------------'

    print sum(range(1,21))

    print '16. ----------------------------------'

    print sum(sampleArray)

    print '17. ----------------------------------'

    print min(sampleArray)

    print '18. ----------------------------------'

    print max(sampleArray)

if __name__ == '__main__':
    main()