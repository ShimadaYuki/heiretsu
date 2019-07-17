import math
import random
import time
import matplotlib.pyplot as plt

#ここへマージソートの関数をコピペ
def merge(array):                                   # line1
    mid = len(array)                                # line2
    if mid > 1:                                     # line3
        left = merge(array[:(mid//2)])               # line4
        right = merge(array[(mid//2):])              # line5
        array = []                                  # line6
        while len(left) != 0 and len(right) != 0:   # line7
            if left[0] < right[0]:                  # line8
                array.append(left.pop(0))           # line9
            else:                                   # line10
                array.append(right.pop(0))          # line11
        if len(left) != 0:                          # line12
            array.extend(left)                      # line13
        elif len(right) != 0:                       # line14
            array.extend(right)                     # line1
    return array                                    # line16
                
sumOfTime = 0
sumPltList = []
nlognList = []
list1 = []
# 配列の長さ0から3000までを作るループ
for i in range(1000):
    # 各々の長さiの配列に対し100回マージソートするループ
    for j in range(10):
        # 各インデックスに0~100000の中からランダムな数字を入れる
        for k in range(i):
            list1.append(random.randint(0,100000))
        # マージソート前の時間
        t0 = time.clock()
        merge(list1)
        # マージソート後の時間
        t1 = time.clock()
        #　次のマージソートの為に配列を空にしておく
        list1 = []
        # マージソートを行った時間の差異の総和
        sumOfTime += t1 - t0
        # 100回行ったマージソートの平均値
        sumOfTime /= 100
        # 平均時間をi個をリストへ格納、2000000は帳尻を合わせたので根拠はない
        sumPltList.append(sumOfTime*2000000)
        # log(0)の対処してilog(i)を比較対象としてi個をリストへ格納
        if i != 0:
            nlognList.append(i*math.log(i)//math.log(2))
        else:
            nlognList.append(0.0)
    # 時間の総和を100回毎にリセット
    sumOfTime = 0
# マージソートとnlog(n)の曲線を描く
plt.plot(sumPltList, "r-", label = "Merge_Sort")
plt.plot(nlognList, "g-", label = "O(nlogn)")
# レーベルを左上に表示
plt.legend(loc=2)
# x軸、y軸にレーベルをつける
plt.xlabel('number of elements in a list')
plt.ylabel('time be taken')
#グラフの表示
plt.show()
        
