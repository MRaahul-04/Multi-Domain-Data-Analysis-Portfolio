import matplotlib.pyplot as plt
import seaborn as sns


def save_plot(fig, path):
    fig.tight_layout()
    fig.savefig(path, dpi=300)
    plt.close(fig)
