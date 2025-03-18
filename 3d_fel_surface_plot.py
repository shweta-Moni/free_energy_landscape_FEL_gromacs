from customstyle import customizer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from mpl_toolkits import mplot3d
import argparse

# Apply custom style
customizer()

def surface_plot(data_file, filename, title_name):
    # Load data from the input file
    data = np.loadtxt(data_file, delimiter='\t', dtype='float')

    # Extract columns for x, y, z
    x = data[:, 0]  # 1st column (e.g., Radius of Gyration)
    y = data[:, 1]  # 2nd column (e.g., RMSD)
    z = data[:, 2]  # 3rd column (e.g., Free Energy)

    # Create a 3D plot
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Create a surface plot
    surf = ax.plot_trisurf(x, y, z, cmap=plt.cm.viridis, linewidth=0.2)
    ax.set_title(title_name, fontsize=15, fontweight='bold')

    # Add a color bar
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # Set axis labels
    ax.set_xlabel('Radius of Gyration (nm)', fontsize=8, fontweight='bold')
    ax.set_ylabel('RMSD (nm)', fontsize=8, fontweight='bold')
    ax.set_zlabel('Free Energy (kJ/mol)', fontsize=8, fontweight='bold')

    # Customize ticks
    plt.xticks(fontweight='bold', fontsize=8, rotation=0)
    plt.yticks(fontweight='bold', fontsize=8, rotation=0)

    # Save the plot
    plt.savefig(filename, bbox_inches='tight')

    # Show the plot, pause for 5 seconds, and then close it
    plt.show(block=False)  # `block=False` allows the script to continue execution
    plt.pause(5.0)  # Pause for 5 seconds
    plt.close()  # Close the plot window

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a 3D surface plot of free energy landscape.")
    parser.add_argument("data_file", type=str, help="Path to the input data file")
    parser.add_argument("output_file", type=str, help="Path to the output image file")
    parser.add_argument("--title", type=str, default="Free energy landscape (FEL)", help="Title of the plot")

    # Parse arguments
    args = parser.parse_args()

    # Call the surface_plot function with the provided arguments
    surface_plot(args.data_file, args.output_file, args.title)

if __name__ == "__main__":
    main()