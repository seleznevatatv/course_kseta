import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
def load_data(file_path):
    return np.loadtxt(file_path)

def plot_data(data, output_file):
    x = data[:, 0]
    y = data[:, 1]
    fit = np.poly1d(np.polyfit(x, y, 1))(np.arange(20))
    
    plt.plot(np.arange(20), fit, color="r")
    plt.scatter(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(output_file)

def main():
    data = load_data("data.csv")
    plot_data(data, "plot.png")

if __name__ == "__main__":
    main()
=======
data = np.loadtxt("data.csv")
plt.plot(
    np.arange(20),
    np.poly1d(np.polyfit(data[:, 0], data[:, 1], 1))(np.arange(20)),
    color="r",
)
plt.scatter(data[:, 0], data[:, 1])
plt.xlabel("x")
plt.ylabel("Y")
plt.savefig("plot.png")
>>>>>>> refs/remotes/origin/main
