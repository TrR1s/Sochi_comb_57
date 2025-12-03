''' do list comb 7 (rank,amount) type'''
import numpy as np
from itertools import combinations

def _comb_7_list_11111_11() -> list:
    res_list = []
    for curr_card_1 in range(12, 5, -1):
        for curr_card_2 in range(curr_card_1 - 1, 4, -1):
            for curr_card_3 in range(curr_card_2 - 1, 3, -1):
                for curr_card_4 in range(curr_card_3 - 1, 2, -1):
                    for curr_card_5 in range(curr_card_4 - 1, 1, -1):
                        for curr_card_6 in range(curr_card_5 - 1, 0, -1):
                            for curr_card_7 in range(curr_card_6 - 1, -1, -1):
                                res_list.append(
                                    [curr_card_7, curr_card_6, curr_card_5, curr_card_4, curr_card_3, curr_card_2,
                                     curr_card_1])
    return res_list


def _comb_7_list_11111_2() -> list:
    res_list = []
    for curr_one_pair in range(12, -1, -1):
        for curr_card_3 in range(12, 3, -1):
            for curr_card_4 in range(curr_card_3 - 1, 2, -1):
                for curr_card_5 in range(curr_card_4 - 1, 1, -1):
                    for curr_card_6 in range(curr_card_5 - 1, 0, -1):
                        for curr_card_7 in range(curr_card_6 - 1, -1, -1):
                            if (curr_card_3 == curr_one_pair or curr_card_4 == curr_one_pair or
                                    curr_card_5 == curr_one_pair or curr_card_6 == curr_one_pair
                                    or curr_card_7 == curr_one_pair):
                                continue
                            res_list.append(
                                [curr_card_7, curr_card_6, curr_card_5, curr_card_4, curr_card_3, curr_one_pair,
                                 curr_one_pair])
    return res_list


def _comb_7_list_111_2_2() -> list:
    res_list = []
    for curr_high_pair in range(12, 0, -1):
        for curr_low_pair in range(curr_high_pair - 1, -1, -1):
            for curr_card_5 in range(12, 1, -1):
                for curr_card_6 in range(curr_card_5 - 1, 0, -1):
                    for curr_card_7 in range(curr_card_6 - 1, -1, -1):
                        if (curr_card_5 == curr_high_pair or curr_card_6 == curr_high_pair
                            or curr_card_7 == curr_high_pair) or (curr_card_5 == curr_low_pair or
                                                                  curr_card_6 == curr_low_pair
                                                                  or curr_card_7 == curr_low_pair):
                            continue
                        res_list.append(
                            [curr_card_7, curr_card_6, curr_card_5, curr_low_pair, curr_low_pair,
                             curr_high_pair, curr_high_pair])
    return res_list


def _comb_7_list_1_2_2_2() -> list:
    res_list = []
    for curr_high_pair in range(12, 1, -1):
        for curr_med_pair in range(curr_high_pair - 1, 0, -1):
            for curr_low_pair in range(curr_med_pair - 1, -1, -1):
                for curr_card_7 in range(12, -1, -1):
                    if (curr_card_7 == curr_high_pair or curr_card_7 == curr_med_pair
                            or curr_card_7 == curr_low_pair):
                        continue
                    res_list.append(
                        [curr_card_7, curr_low_pair, curr_low_pair, curr_med_pair, curr_med_pair,
                         curr_high_pair, curr_high_pair])
    return res_list


def _comb_7_list_1111_3() -> list:
    res_list = []
    for curr_three_of_kind in range(12, -1, -1):
        for curr_card_4 in range(12, 2, -1):
            for curr_card_5 in range(curr_card_4 - 1, 1, -1):
                for curr_card_6 in range(curr_card_5 - 1, 0, -1):
                    for curr_card_7 in range(curr_card_6 - 1, -1, -1):
                        if (curr_card_4 == curr_three_of_kind or
                                curr_card_5 == curr_three_of_kind or curr_card_6 == curr_three_of_kind
                                or curr_card_7 == curr_three_of_kind):
                            continue
                        res_list.append(
                            [curr_card_7, curr_card_6, curr_card_5, curr_card_4, curr_three_of_kind, curr_three_of_kind,
                             curr_three_of_kind])
    return res_list


def _comb_7_list_11_2_3() -> list:
    res_list = []
    for curr_three_of_kind in range(12, -1, -1):
        for curr_one_pair in range(12, -1, -1):
            if curr_three_of_kind == curr_one_pair:
                continue
            for curr_card_6 in range(12, 0, -1):
                for curr_card_7 in range(curr_card_6 - 1, -1, -1):
                    if (curr_card_6 == curr_three_of_kind
                        or curr_card_7 == curr_three_of_kind) or (curr_card_6 == curr_one_pair
                                                                  or curr_card_7 == curr_one_pair):
                        continue
                    res_list.append(
                        [curr_card_7, curr_card_6, curr_one_pair, curr_one_pair, curr_three_of_kind,
                         curr_three_of_kind, curr_three_of_kind])
    return res_list


def _comb_7_list_2_2_3() -> list:
    res_list = []
    for curr_three_of_kind in range(12, -1, -1):
        for curr_high_pair in range(12, 0, -1):
            for curr_low_pair in range(curr_high_pair - 1, -1, -1):
                if curr_three_of_kind == curr_high_pair or curr_three_of_kind == curr_low_pair:
                    continue
                res_list.append(
                    [curr_low_pair, curr_low_pair, curr_high_pair, curr_high_pair, curr_three_of_kind,
                     curr_three_of_kind, curr_three_of_kind])
    return res_list


def _comb_7_list_1_3_3() -> list:
    res_list = []
    for curr_high_three_of_kind in range(12, 0, -1):
        for curr_low_three_of_kind in range(curr_high_three_of_kind - 1, -1, -1):
            for curr_card_7 in range(12, -1, -1):
                if curr_card_7 == curr_high_three_of_kind or curr_card_7 == curr_low_three_of_kind:
                    continue
                res_list.append(
                    [curr_card_7, curr_low_three_of_kind, curr_low_three_of_kind, curr_low_three_of_kind,
                     curr_high_three_of_kind,
                     curr_high_three_of_kind, curr_high_three_of_kind])
    return res_list


def _comb_7_list_111_4() -> list:
    res_list = []
    for curr_four_of_kind in range(12, -1, -1):
        for curr_card_5 in range(12, 1, -1):
            for curr_card_6 in range(curr_card_5 - 1, 0, -1):
                for curr_card_7 in range(curr_card_6 - 1, -1, -1):
                    if (curr_card_5 == curr_four_of_kind or curr_card_6 == curr_four_of_kind
                            or curr_card_7 == curr_four_of_kind):
                        continue
                    res_list.append(
                        [curr_card_7, curr_card_6, curr_card_5, curr_four_of_kind, curr_four_of_kind, curr_four_of_kind,
                         curr_four_of_kind])
    return res_list


def _comb_7_list_1_2_4() -> list:
    res_list = []
    for curr_four_of_kind in range(12, -1, -1):
        for curr_one_pair in range(12, -1, -1):
            if curr_four_of_kind == curr_one_pair:
                continue
            for curr_card_7 in range(12, -1, -1):
                if curr_card_7 == curr_four_of_kind or curr_card_7 == curr_one_pair:
                    continue
                res_list.append(
                    [curr_card_7, curr_one_pair, curr_one_pair, curr_four_of_kind, curr_four_of_kind,
                     curr_four_of_kind, curr_four_of_kind])
    return res_list


def _comb_7_list_3_4() -> list:
    res_list = []
    for curr_four_of_kind in range(12, -1, -1):
        for curr_three_of_kind in range(12, -1, -1):
            if curr_four_of_kind == curr_three_of_kind:
                continue
            res_list.append(
                [curr_three_of_kind, curr_three_of_kind, curr_three_of_kind, curr_four_of_kind, curr_four_of_kind,
                 curr_four_of_kind, curr_four_of_kind])
    return res_list


def do_comb_7_tuple_list() -> list:
    def do_tuple_comb(comb: list) -> tuple:
        # comb_np = np.array(comb)
        # unigue_ranks, counts_ranks = np.unique(comb_np, return_counts=True)
        
        return sorted(list(map(lambda x: int(x+2),comb)))
        # return (tuple(map(lambda x: int(x+2),unigue_ranks)), tuple(tuple(map(lambda x: int(x),counts_ranks))))
        # return (unigue_ranks, counts_ranks)

    total_comb_list = _comb_7_list_11111_11()
    total_comb_list.extend(_comb_7_list_11111_2())
    total_comb_list.extend(_comb_7_list_111_2_2())
    total_comb_list.extend(_comb_7_list_1_2_2_2())
    total_comb_list.extend(_comb_7_list_1111_3())
    total_comb_list.extend(_comb_7_list_11_2_3())
    total_comb_list.extend(_comb_7_list_2_2_3())
    total_comb_list.extend(_comb_7_list_1_3_3())
    total_comb_list.extend(_comb_7_list_111_4())
    total_comb_list.extend(_comb_7_list_1_2_4())
    total_comb_list.extend(_comb_7_list_3_4())
    mapped_total_comb_list = list(map(do_tuple_comb, total_comb_list))
    return mapped_total_comb_list



def do_comb7_with_fl_list() -> list:
    comb7_with_fl_list =[]
    comb_7_list = do_comb_7_tuple_list()
    for curr_comb_7 in comb_7_list:
        unique_ranks, _ = np.unique(np.array(curr_comb_7), return_counts=True)
        comb7_with_fl_list.append((curr_comb_7,[]))
        if len(unique_ranks) >=5:
            unique_ranks = list(map(int,list(unique_ranks)))
            
            for flushed_am in range(5,8):
                for comb in combinations(unique_ranks,flushed_am):
                    comb7_with_fl_list.append([curr_comb_7,list(sorted(comb))])
    return comb7_with_fl_list
                
if __name__ == "__main__":



    comb_7_tuple_list = do_comb7_with_fl_list()
    comb_7_tuple_list[3][1] = [12,13]
    print(comb_7_tuple_list[:20])
    print(len(comb_7_tuple_list))
    