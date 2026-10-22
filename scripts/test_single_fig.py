# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_figure_legends(generator_func, fig_name):
    fig = plt.figure()
    # Run the generator, which creates figures
    # Let's inspect the code of generator functions
    pass

print("Script template ready.")
