import matplotlib.pyplot as plt


def plot_graph_j(x1, y1, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a', label_b='label_b'):
    """
      Plots a simple line graph with the provided data and labels.

    Parameters:
    x1 (list or array-like): X-axis values.
    y1 (list or array-like): Y-axis values for the first plot.
    title (str, optional): Title of the graph. Default is 'title'.
    xlabel (str, optional): Label for the X-axis. Default is 'xlabel'.
    ylabel (str, optional): Label for the Y-axis. Default is 'ylabel'.
    label_a (str, optional): Legend label for the first plot. Default is 'label_a'.
    label_b (str, optional): Legend label for the second plot. Default is 'label_b'.

    Returns:
    None

    This function creates a line plot of the given x and y values. The function also adds a title,
    axis labels, a legend, and a grid to the plot.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label=label_a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


