import matplotlib.pyplot as plt

def plot_graph_j(x1, y1, y2=None, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a', label_b='label_b'):
    """ docstrings """
    plt.figure(figsize=(8, 4))
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label=label_a)
    if y2 is not None:
        plt.plot(x1, y2, marker='x', linestyle='--', color='green', label=label_b)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show();



def plot_graph(x, y, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a'):
    """ docstrings """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label=label_a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_graph_2(x1,x2, y1,y2, title='title', xlabel='xlabel', ylabel='Percentage', label_a='label_a', label_b='label_b'):
    """ docstrings """
    plt.figure(figsize=(8, 4))
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label=label_a)
    plt.plot(x2, y2, marker='x', linestyle='--', color='green', label=label_b)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_graph_3(x, y, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a'):
    """ docstrings """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label=label_a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_graph_4(x, y, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a'):
    """ docstrings """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label=label_a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_graph_5(x, y, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a'):
    """ docstrings """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label=label_a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()