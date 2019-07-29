# README

This readme is a guideline for the formation of graphs in Zhu et al: *Network characteristics of human RNA-RNA interactions and application in finding key RNAs of breast cancer*

Dependencies on Python packages: 

- pyecharts


- pandas


- matplotlib_venn
- matplotlib
- itertools
- seaborn
- math
- scipy

Functions of scripts:

1. **count.py**: Count the numbers of each type of RNA and RRI in the RRI network.
2. **degree_distribution.py**: Produce the distribution map of node degrees of each type of RNA in the RRI network.
3. **venn_for_nodes.py**: Produce the Venn diagram for the nodes of the RRI network, the PPI network, and the co-expression network.
4. **venn_for_edges.py**: Produce the Venn diagram for the edges of the RRI network, the PPI network, and the co-expression network.
5. **compare_distribution_of_node_degree.py**: Produce the distribution map of node degrees of the RRI network, the PPI network, and the co-expression network.
6. **node_degree_and_shortest_path_length.py**: Produce the distribution map of degrees and shortest path lengths of the BC-related nodes in the RRI network.
7. **key_nodes.py**: Produce the Venn diagram of the hub nodes, the BC-related genes and the DEGs.

The folder "input_data" contains input data for the scripts.

The file "other_data.xls" contains other data and graphs in the paper.

Note: The scripts are able to fetch the involved input automatically, in order to run the scripts smoothly, please make sure that all the scripts and data folders are downloaded into the same path.
