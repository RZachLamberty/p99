#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

"""
Module: p99.py
Author: zlamberty
Created: 2015-06-02

Description:
    Implementation of the p99 problems in python

Usage:
    <usage>

"""

def p01(l):
    """ find the last element in a list """
    return l[-1]


def p02(l):
    """ find the penultimate element of a list """
    return l[-2]


def p03(l, k):
    """ find the kth element of a list """
    return l[k]


def p04(l):
    """ find the number of elements in a list """
    return len(l)


def p05(l):
    """ reverse a list """
    return list(reversed(l))


def p06(l):
    """ whether or not a list is a palindrome """
    return l == p05(l)


def p07(x):
    """ flatten a possibly nested list structure """
    r = []
    for l in x:
        if isinstance(l, list):
            r += p07(l)
        else:
            r.append(l)
    return r


def p08(l):
    """ eliminate consecutive duplicates of list elements """
    r = []
    xlast = None
    for x in l:
        if x == xlast:
            pass
        else:
            r.append(x)
        xlast = x
    return r


def p09(l):
    """ pack consecutive duplicates of list elements into sublists """
    r = []
    xlast = None
    rsub = []
    for x in l:
        if x == xlast:
            rsub.append(xlast)
        else:
            if rsub:
                r.append(rsub)
            rsub = [x]
        xlast = x
    r.append(rsub)
    return r


def p10(l):
    """ run-length encoding of a list (consecutive dupes are recorded as
        [N, E], where N is the number of elements E)

    """
    return [[len(x), x[0]] for x in p09(l)]


def p11(l):
    """ modified run-length encoding of a list (consecutive dupes are
        recorded as [N, E], where N is the number of elements E, *unless*
        N = 1, in which case it is only E)

    """
    return [
        [len(x), x[0]] if len(x) > 1 else x[0]
        for x in p09(l)
    ]


def p12(l):
    """ decode a run-length encoded list """
    r = []
    for el in l:
        if isinstance(el, list):
            r += [el[1] for i in range(el[0])]
        else:
            r.append(el)
    return r


def p13(l):
    """ run-length encoding of a list (direct). Create run-length encoding
        without constructing sublists first

    """
    if len(l) < 2:
        return [l]
    r = []
    xlast = l[0]
    rsub = [1, xlast]
    for i in range(1, len(l)):
        xnow = l[i]
        if xnow == xlast:
            rsub[0] += 1
        else:
            r.append(rsub if rsub[0] > 1 else rsub[1])
            rsub = [1, xnow]
        xlast = xnow
    r.append(rsub if rsub[0] > 1 else rsub[1])
    return r


def p14(l):
    """ duplicate the elements of a list """
    return [x for x in l for i in range(2)]


def p15(l, n):
    """ repeat ever elemtn of a list n times """
    return [x for x in l for i in range(n)]


def p16(l, n):
    """ drop every nth element from a list """
    return [x for (i, x) in enumerate(l) if (i + 1) % n]


def p17(l, n):
    """ split a list into two parts, the first of lenght n """
    return l[:n], l[n:]


def p18(l, i, j):
    """ extract a slice, including ith and jth, indexing starting at 1 """
    return l[i - 1: j]


def p19(l, n):
    """ rotate a list n places to the left """
    L = len(l)
    return [l[(i + n) % L] for i in range(L)]


def p20(l, k):
    """ remove the kth element from a list """
    return [x for (i, x) in enumerate(l) if i + 1 != k]
