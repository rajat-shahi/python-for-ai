import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,4,6,8,10,12]

plt.title("Linear Equation")
plt.xlabel("Value of X")
plt.ylabel("Value of Y")
plt.grid()
plt.plot(x,y)
plt.show()


a = [i for i in range (-10,11,1)]
b = [i*i for i in a]
print(b)
plt.title("Quadratic Equation")
plt.xlabel("Value of X")
plt.ylabel("Value of Y")
plt.plot(a,b,marker="o",markersize=7,markerfacecolor="red",markeredgecolor="black",markeredgewidth=2)
plt.show()
