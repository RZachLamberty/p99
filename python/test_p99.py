#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

"""
Module: test_p99.py
Author: zlamberty
Created: 2015-06-02

Description:
    Test that the functions implemented in p99.py return the correct answers

Usage:
    <usage>

"""

import p99 as P

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
RL = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
NEST = [1, [2, [3, 4], 5]]
DUPES = [1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]
ABC = ['a', 'b', 'c']
ABC8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ABC10 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']

if __name__ == '__main__':
    assert P.p01(L) == 9
    assert P.p02(L) == 8
    assert P.p03(L, 3) == 3
    assert P.p04(L) == 10
    assert P.p05(L) == RL
    assert P.p06(L) == False
    assert P.p07(NEST) == [1, 2, 3, 4, 5]
    assert P.p08(DUPES) == [1, 2, 3, 1, 4, 5]
    assert P.p09(DUPES) == [[1, 1, 1, 1], [2], [3, 3], [1, 1], [4], [5, 5, 5, 5]]
    assert P.p10(DUPES) == [[4, 1], [1, 2], [2, 3], [2, 1], [1, 4], [4, 5]]
    assert P.p11(DUPES) == [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
    assert P.p12(P.p11(DUPES)) == DUPES
    assert P.p13(DUPES) == [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
    assert P.p14(ABC) == ['a', 'a', 'b', 'b', 'c', 'c']
    assert P.p15(ABC, 3) == ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
    assert P.p16(L, 3) == [0, 1, 3, 4, 6, 7, 9]
    assert P.p17(L, 4) == ([0, 1, 2, 3], [4, 5, 6, 7, 8, 9])
    assert P.p18(ABC10, 3, 7) == ['c', 'd', 'e', 'f', 'g']
    assert (
        P.p19(ABC8, 3) == ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
        and
        P.p19(ABC8, -2) == ['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f']
    )
    assert P.p20(['a', 'b', 'c', 'd'], 2) == ['a', 'c', 'd']
    print("")
    print("I've got 99 problems, bein a bitch ain't one")
    print("")
