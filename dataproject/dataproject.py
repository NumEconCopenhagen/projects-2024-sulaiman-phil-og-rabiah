import matplotlib.pyplot as plt


def plot_graph_j(x1, y1, y2=None, title='title', xlabel='xlabel', ylabel='ylabel', label_a='label_a', label_b='label_b'):
    """
    Plots a graph with one or two sets of y-values against a common set of x-values.

    Parameters:
    x1 (list or array-like): X-axis values.
    y1 (list or array-like): Y-axis values for the first plot.
    y2 (list or array-like, optional): Y-axis values for the second plot. Default is None.
    title (str, optional): Title of the graph. Default is 'title'.
    xlabel (str, optional): Label for the X-axis. Default is 'xlabel'.
    ylabel (str, optional): Label for the Y-axis. Default is 'ylabel'.
    label_a (str, optional): Legend label for the first plot. Default is 'label_a'.
    label_b (str, optional): Legend label for the second plot. Default is 'label_b'.

    Returns:
    None

    This function creates a line plot of the given x and y values. If a second set of y values is provided,
    it plots both sets on the same graph with different styles and labels. The function also adds a title,
    axis labels, a legend, and a grid to the plot.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label=label_a)
    if y2 is not None:
        plt.plot(x1, y2, marker='x', linestyle='--', color='green', label=label_b)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
