import matplotlib.pyplot as plt

def main():
    n = int(input("Enter the first number 'n': "))
    rada = [n]
    y_axis = []

    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        rada.append(n)

    for I in range(len(rada)):
        y_axis.append(I+1)

    ax=plt.gca()

    ax.set_facecolor("lightgray")

    plt.grid()

    plt.plot(rada, marker='o', markerfacecolor='black', color = "gray")

    for J in range(len(rada)):
        if rada[J] > 5:
            plt.annotate(int(rada[J]), (J, rada[J]-3))
        else:
           plt.annotate(int(rada[J]), (J, rada[J]+3))



    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Collatz-Problem Graph!')

    # function to show the plot
    plt.show()

if __name__ == '__main__':
    main()