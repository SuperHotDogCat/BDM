import matplotlib.pyplot as plt
import numpy as np

def read_data():
    data = []
    with open("alcohol_data_0.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line.replace(" ", "").replace("A0:", "").replace("\n", "")))
    return data

def save_hist_img(data):
    plt.hist(data)
    plt.savefig("dist.png")

def otsu_method(data):
    min_data = np.min(data)
    max_data = np.max(data)
    data = np.array(data)
    max_sigmab = 0
    best_threshold = 0
    for threshold in range(min_data, max_data):
        left_data = data[data < threshold]
        right_data = data[data >= threshold]
        omega_left = len(left_data)
        omega_right = len(right_data)
        sigmab = omega_left * omega_right * (left_data.mean() - right_data.mean()) ** 2 / (omega_left + omega_right) ** 2
        if sigmab > max_sigmab:
            max_sigmab = sigmab
            best_threshold = threshold
    return best_threshold

if __name__ == "__main__":
    data = read_data()
    save_hist_img(data)
    print(otsu_method(data))