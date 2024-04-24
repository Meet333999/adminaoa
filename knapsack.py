def knapsack(n, w, p, W):
    x = [0] * n
    weight = 0
    profit = 0
    for i in range(n):
        if weight + w[i] <= W:
            x[i] = 1
            weight += w[i]
            profit += p[i]
        else:
            x[i] = (W - weight) / w[i]
            weight = W
            profit += x[i] * p[i]
            break
    return profit, x

if __name__ == '__main__':
    no = int(input('Enter the number of Elements:- '))
    w = []
    val = []
    for i in range(no):
        w.append(int(input('Enter the weights:- ')))
    for j in range(no):
        val.append(int(input('Enter the values:- ')))
    W = int(input('Enter the Knapsack Capacity:- '))
    Ratio = []
    for k in range(no):
        Ratio.append(val[k] / w[k])
    print(Ratio)
    sorted_lists = sorted(zip(Ratio, w, val), reverse=True)
    Ratio, w, val = zip(*sorted_lists)
    print(w)
    print(val)
    print(Ratio)
    profit, selected_items = knapsack(no, w, val, W)
    print(profit)
    print(selected_items)



output
Enter the number of Elements:- 3
Enter the weights:- 10
Enter the weights:- 20
Enter the weights:- 30
Enter the values:- 60
Enter the values:- 100
Enter the values:- 120
Enter the Knapsack Capacity:- 50 
[6.0, 5.0, 4.0]
(10, 20, 30)
(60, 100, 120)
(6.0, 5.0, 4.0)
240.0
[1, 1, 0.6666666666666666]
