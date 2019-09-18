
Project Title: Data Science - JSON File: Loading and Data Analysis

===== To view Notebook file in Github =====

Due to a github bug, sometimes jupyter notebook files fail to load. If that happens, then to view the notebook file paste this link to your browser:
https://nbviewer.jupyter.org/github/ds130/sp/blob/master/projects/jsonFileDataAnalysis/json_dataAnalysis.ipynb

===== 


Included one Python Notebook file:

- json_dataAnalysis.ipynb



Included the corresponding python file:
- json_dataAnalysis.py



Plot files:
see execution below




===== To Open/Run Jupyter Notebook file =====


To open jupyter notebook file (.ipynb), open a terminal, go to the directory where the file is located, and run the following command:

$ jupyter notebook json_dataAnalysis.ipynb


Or, to open file in jupyter lab, run the following command:

$ jupyter lab json_dataAnalysis.ipynb



Use "Run" button in the notebook interface to run the above.



===== To Execute .py file =====


To run the Python file (.py), open a terminal, go to the directory where the file is located, and run the following command:

$ python3 json_dataAnalysis.py


At runtime, it will generate and save all the 4 plot files as .jpg in the same directory. These are:
- Figure_Plot1_topTenCountries.jpg
- Figure_Plot2_topTenMajorProjectThemes.jpg
- Figure_Plot3_bar_allMajorProjectThemes.jpg
- Figure_Plot4_pie_allMajorProjectThemes.jpg


===== Description =====


File json_dataAnalysis.ipynb contains:

- Loading JSON file dataset (contains 500 rows with 50 columns) into dataframe.

- Finding the 10 countries with most projects.

- Finding the top 10 major project themes (using column 'mjtheme_namecode').

- Visualization with Bar-plot and Pie-plot.

- Creating new dataframe with the missing names in df filled in for major project themes (column 'mjtheme_namecode').


=====




