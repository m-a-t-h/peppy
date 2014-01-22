# -*- coding: utf-8 -*-

class Permutation:
    def __init__(self,):
       return

    """
    方針
    たとえば入力 lists = [[1,2,4,8], [1,3], [1,5,25]] の場合
    以下、[1,2,4,8] を 1st_list,
          [1,3] を 2nd_list,
          [1,5,25] を 3rd_list と呼ぶ。

    出力 res として欲しいのは
    [1,1,1], [1,1,5], [1,1,25], [1,3,1], [1,3,5], [1,3,25],
    [2,1,1], [2,1,5], [2,1,25],...
    [4,1,1], [4,1,5], [4,1,25],...
    [8,1,1], [8,1,5], [8,1,25],...             ...[8,3,25]
    という 4*2*3 = 24個 (= res_length) のリストのリスト

    このうち
    先頭が1 (= 1st_list[0]) のものは最初の 6つ (= rotation_length)
    ( 6 = 24 / 4 = res_length / len(1st_list)
    先頭が2,4,8 のものについても同じで、res の先頭には、6つずつ 1,2,4,8 を追加していけばよい

    先頭が決まったあと、2番目の要素については
    1,1,1, 3,3,3, 1,1,1, 3,3,3 ...
    のように、3つずつ、2nd_list[0] と 2nd_list[1] を追加していけばよい
    ( rotation_length = res_length / len(1st_list) / len(2nd_list) = 3)

    3番目の要素についても同様
    1,5,25, 1,5,25, 1,5,25 ...
    のように、1つずつ 3rd_list[0], 3rd_list[1], 3rd_list[2] を append していけばよい
    """
    def get_all_permutations(self, lists):
        """
        >>> P = Permutation()
        >>> P.get_all_permutations( [ [1,2,4,8], [1, 3], [1,5,25] ] )
        [['1', '1', '1'], ['1', '1', '5'], ['1', '1', '25'], ['1', '3', '1'], ['1', '3', '5'], ['1', '3', '25'], ['2', '1', '1'], ['2', '1', '5'], ['2', '1', '25'], ['2', '3', '1'], ['2', '3', '5'], ['2', '3', '25'], ['4', '1', '1'], ['4', '1', '5'], ['4', '1', '25'], ['4', '3', '1'], ['4', '3', '5'], ['4', '3', '25'], ['8', '1', '1'], ['8', '1', '5'], ['8', '1', '25'], ['8', '3', '1'], ['8', '3', '5'], ['8', '3', '25']]

        >>> P.get_all_permutations( [ [1,2,3], ["a", "b",], ["A"] ] )
        [['1', 'a', 'A'], ['1', 'b', 'A'], ['2', 'a', 'A'], ['2', 'b', 'A'], ['3', 'a', 'A'], ['3', 'b', 'A']]
        """
        res_length = reduce(lambda x,y: x*y, [len(list) for list in lists])
        # initialize res
        res = []
        for i in range(res_length):
            res.append([])
        # rotation length for each list
        rotation_length = res_length
        for list in lists:
            rotation_length /= len(list)
            for i in range(res_length):
                ith_element_to_add = (i / rotation_length) % len(list)
                res[i].append( str( list[ith_element_to_add] ) )
        return res

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed:
        import sys
        sys.exit(1)
