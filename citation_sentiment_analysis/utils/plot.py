import matplotlib.pyplot as plt


def configure_default_plot_style():
    plt.rcParams.update({
        'font.size': 20,
        'figure.figsize': (20, 10)
    })


def add_bar_plot_numbers(ax, fontsize=None):
    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = 3

        # Use Y value as label
        label = "%s" % y_value

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va='bottom',                # Vertically align label at bottom
            fontsize=fontsize
        )


def bar_plot_with_numbers(df_or_series, kind='bar', fontsize=None, **kwargs):
    ax = df_or_series.plot(kind='bar', **kwargs)
    add_bar_plot_numbers(ax, fontsize=fontsize)
    