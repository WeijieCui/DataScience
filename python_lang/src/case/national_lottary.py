import matplotlib.pyplot as plt


def main():
    rounds = []
    with open('history.txt', 'r') as f:
        for line in f.readlines():
            rounds.append([int(s) for s in line[:-1].split('\t')])
    print(rounds)
    count_normals = [0] * 50
    count_lucks = [0] * 12
    for nums in rounds:
        for num in nums[:-2]:
            count_normals[num - 1] += 1
        for num in nums[-2:]:
            count_lucks[num - 1] += 1
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.bar([i for i in range(1, 51)], count_normals)
    ax2.bar([i for i in range(1, 13)], count_lucks)
    plt.show()
    # 5, 16, 21, 30, 35, 1, 9


if __name__ == '__main__':
    main()
