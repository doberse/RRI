README

This readme is a guideline for the network analysis in Zhu et al.: Network characteristics of human RNA-RNA interactions and application in finding key RNAs of breast cancer

Dependencies on Python v3.6.5 packages: 

- pandas v0.23.0
- numpy v1.14.3
- networkx v2.1

Functions of scripts:

1. direct_and_indirect_pair.py: Form the directly / indirectly (with an interval of one node) connected pairs in the RRI network.
2. SPL_disease_RRI.py: Calculate the shortest path lengths between every disease gene pairs in the RRI network.
3. SPL_disease_PPI.py: Calculate the shortest path lengths between every disease gene pairs in the PPI network.
4. SPL_disease_CoEx.py: Calculate the shortest path lengths between every disease gene pairs in the co-expression network.
5. relative_connectivity_of_subgraphs.py: Compute the relative connectivity of degree-ordered subgraphs in the BC-related RRI network.

The folder "input_data" contains input data for the scripts. Please decompress these data files to the folder "input_data" before running the scripts.

Note: The scripts are able to fetch the involved input automatically. In order to run the scripts smoothly, please make sure that all the scripts and the data folder are downloaded into the same path. 

State: All the data is for academic exchange only.
