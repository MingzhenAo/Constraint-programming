# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:46:09 2020

@author: Mingzhen Ao
"""

import playingmode1_data_analysis_function as daf

print("For the 'start' difficulty:\n")
daf.get_solvedcases_coverage_and_averagetime("start")
print(" ")
print("For the 'junior' difficulty:\n")
daf.get_solvedcases_coverage_and_averagetime("junior")
print(" ")
print("For the 'expert' difficulty:\n")
daf.get_solvedcases_coverage_and_averagetime("expert")
print(" ")
print("For the 'master' difficulty:\n")
daf.get_solvedcases_coverage_and_averagetime("master")
print(" ")
print("For the 'wizard' difficulty:\n")
daf.get_solvedcases_coverage_and_averagetime("wizard")
print(" ")
print("the overall data:\n")
daf.get_overall_solvedcases_coverage_and_averagetime()
