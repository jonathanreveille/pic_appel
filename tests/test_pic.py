#! /usr/bin/env python3
# coding : utf-8

from appel_pic import Simultaneous

def test_create_Simultaneous():
    """Initiate the tests"""

    s = Simultaneous()
    assert s.call_list == list()

def test_read_call_list():
    """test if method can read txt file and transform
    it into a 2D list of string"""

    s = Simultaneous()

    assert s.read_call_list('data/calls.txt') == [
                                            ['1385718405', '1385718491'],
                                            ['1385718407', '1385718409'],
                                            ['1385718408', '1385718452'],
                                            ['1385718408', '1385718464'],
                                            ['1385718413', '1385718452']
                                            ]

def test_transform_str_to_int_from_a_list():
    """Test if method can read the 2D str list,
    and transform it into 2D int list"""

    s = Simultaneous()
    data = s.read_call_list('data/calls.txt')
    s.transform_str_to_int_from_a_list(data)

    assert s.fresh_list == [
                        [1385718405, 1385718491],
                        [1385718407, 1385718409],
                        [1385718408, 1385718452],
                        [1385718408, 1385718464],
                        [1385718413, 1385718452]
                        ]

def test_read_two_dimensional_list_and_find_simulataneous_calls():
    """test if method can read through each value,
    and compare the first call line with the other
    call lines. Once done for one line, go to the
    next line and check with every call"""
    
    s = Simultaneous()
    data = s.read_call_list('data/calls.txt')
    clean_data = s.transform_str_to_int_from_a_list(data)
    count = s.count_simultaneous_calls(clean_data)

    assert count == 4

def test_read_two_dimensional_list_and_find_simulataneous_calls_2_new_list1():
    """test if method can read through each value,
    and compare the first call line with the other
    call lines. Once done for one line, go to the
    next line and check with every call"""

    clean_data = [
        [1485718825, 1485718911],
        [1485718827, 1485718830],
        [1485718828, 1485718872],
        [1485718828, 1485718884],
        [1485718833, 1485718872]
        ]
    
    s = Simultaneous()
    count = s.count_simultaneous_calls(clean_data)
    assert count == 4

def test_read_two_dimensional_list_and_find_simulataneous_calls_new_list2():
    """test if method can read through each value,
    and compare the first call line with the other
    call lines. Once done for one line, go to the
    next line and check with every call"""

    clean_data = [
        [425, 511],
        [426, 462],
        [428, 433], 
        [428, 484],
        [433, 472]
        ]

    s = Simultaneous()
    count = s.count_simultaneous_calls(clean_data)
    assert count == 4

#1 random data in ascending order from start
    # clean_data = [
    #     [1895684425, 1895684511],
    #     [1895684427, 1895684472],
    #     [1895684427, 1895684430],
    #     [1895684429, 1895684484],
    #     [1895684433, 1895684472]
    #     ]

#2 random data in ascending order from start
        # clean_data = [
        # [1895684425, 1895684511],
        # [1895684427, 1895684430],
        # [1895684427, 1895684472],
        # [1895684429, 1895684484],
        # [1895684433, 1895684472]
        # ]
    