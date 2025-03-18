import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import argparse
import time  # Import the time module for pausing

def contour_plot(data_file, filename, title_name):
    data = np.loadtxt(data_file, delimiter='\t', dtype='float')

    # Extract columns for x, y, z
    x = data[:, 0]  # CV1
    y = data[:, 1]  # CV2
    z = data[:, 2]  # Free energy

    # Create a grid for CV1 and CV2
    xi = np.linspace(x.min(), x.max(), 300)
    yi = np.linspace(y.min(), y.max(), 300)
    xi, yi = np.meshgrid(xi, yi)

    # Interpolate z values
    zi = griddata((x, y), z, (xi, yi), method='linear')

    # 2D Contour Plot
    plt.clf()
    plt.figure(figsize=(8, 6))
    contour = plt.contourf(xi, yi, zi, levels=25, cmap='viridis')
    cbar = plt.colorbar(contour)
    cbar.set_label('Free Energy (kJ/mol)', fontsize=10, fontweight='bold')

    # Add title and axis labels
    plt.title(title_name, fontsize=15, fontweight='bold')
    plt.xlabel('Radius of Gyration (nm)', fontsize=12, fontweight='bold')
    plt.ylabel('RMSD (nm)', fontsize=12, fontweight='bold')

    # Customize ticks
    plt.xticks(fontweight='bold', fontsize=10)
    plt.yticks(fontweight='bold', fontsize=10)

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fontsize=10, ncol=2, frameon=False)

    # Save the plot
    plt.savefig(filename, bbox_inches='tight', dpi=300)

    # Show the plot and pause for 2 seconds
    plt.show(block=False)  # `block=False` allows the script to continue execution
    plt.pause(2)  # Pause for 2 seconds
    plt.close()  # Close the plot window

def main():
    parser = argparse.ArgumentParser(description="Generate a 2D free energy landscape plot.")
    parser.add_argument("data_file", type=str, help="Path to the input data file")
    parser.add_argument("output_file", type=str, help="Path to the output image file")
    parser.add_argument("--title", type=str, default="Free energy landscape (FEL)", help="Title of the plot")

    args = parser.parse_args()

    contour_plot(args.data_file, args.output_file, args.title)

if __name__ == "__main__":
    main()