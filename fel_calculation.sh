# FEL (free energy landscape) against RMSD and Radius of Gyration (Rg)
################################################################################################################

# Step 1: Calculate RMSD and Rg from trajectory
################################################################################################################
echo 1 1 | gmx gyrate -f input_traj.xtc -s input_str.pdb -o rg_protein.xvg
echo 1 1 | gmx rms -f input_traj.xtc -s input_str.pdb -o rmsd_protein.xvg

# Step 2: Merge the data into one file
################################################################################################################
perl sham.pl -i1 rg_protein.xvg -i2 rmsd_protein.xvg -data1 1 -data2 1 -o rg_rmsd_protein_gsham_input.xvg

# # or Combine RMSD and Rg data
# paste rg_protein.xvg rmsd_protein.xvg > rg_rmsd_protein_gsham_input.xvg

# Step 3: Calculate Free Energy Landscape using gmx sham
################################################################################################################
gmx sham -f rg_rmsd_protein_gsham_input.xvg -ls rg_rmsd_protein_fel.xpm -ls gibbs.xpm -g sham.log

# Step 4: Generate the txt file from xpm file using python script
################################################################################################################
python xpm2txt_python3.py -f rg_rmsd_protein_fel.xpm -o rg_rmsd_protein_fel.txt

# gmx xpm2ps to generate eps frile from xpm
##############################################
# gmx xpm2ps -f rg_rmsd_protein_fel.xpm -o rg_rmsd_protein_fel.eps -rainbow blue

# Step 5: Generate a 2D contour plot from txt file
# Syntax: python 2d_fel_from_fes_txt.py input.txt output.png
################################################################################################################
python 2d_fel_from_fes_txt.py rg_rmsd_protein_fel.txt FEL_rg_rmsd_protein_fel.png

# Step 6: Generate a 3D surface plot
# Syntax: python 3d_fel_surface_plot.py input.txt output.png --title "Title for plot"
################################################################################################################
python 3d_fel_surface_plot.py rg_rmsd_protein_fel.txt rg_rmsd_protein_fel_output.png --title "Free Energy Landscape (Rg vs RMSD)"

# Step 7: Find the closest matching timestamp in a 3-column file (output of sham.pl) based on two input values
# Syntax: python get_timestamp.py -f <sham output> -1 <value 1> -2 <value 2>
# Example: Free energy is 0.81200 with Rg 0.14149 and RMSD 0.10211
# Get the time to see the structure with this value (closest)
python get_timestep_python3.py -f rg_rmsd_protein_gsham_input.xvg -1 0.14149 -2 0.10211            

#output T = 54.1 (0.141523, 0.112718)

