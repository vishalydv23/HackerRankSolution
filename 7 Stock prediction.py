# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:37:39 2022

@author: Vishal
"""
import math
def printTransactions(money, k, d, name, owned, prices):
    def mean(data):
        return sum(data)/ len(data)
    
    def sd(nums):
        average = mean(nums)
        return math.sqrt(sum([(x - average) ** 2 for x in nums]) / len(nums))

    def info(price):
        cc, sigma, acc = 0, 0.0, 0
        for i in range(1, 5): 
            if price[i] > price[i - 1]: cc += 1
        sigma = sd(price)
        mu = mean(price)
        c1, c2, c3 = mean(price[0:3]), mean(price[1:4]), mean(price[2:5])
        
        return (price[-1] - price[-2]) / price[-2]
    
    infos = map(info, prices)
    res = []
    
    drop = []
    
    for i in range(k):
        cur_info = info(prices[i])
        if cur_info > 0 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
        elif cur_info < 0:
            heappush(drop, (cur_info, i, name[i]))
    
    while money > 0.0 and drop:
        rate, idx, n = heappop(drop)
        amount = int(money / prices[idx][-1])
        if amount  > 0:
            res.append((n, 'BUY', str(amount)))
            money -= amount * prices[idx][-1]
    
    print(len(res))
    for r in res:
        print(' '.join(r))

if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = input().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])
        
    printTransaction(m,k,d,names,owned,prices)