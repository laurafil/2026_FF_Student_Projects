import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import sys
raw_dir = Path(__file__).resolve().parent.parent / "raw"
sys.path.insert(0, str(raw_dir))
#raw_dir = ... → "Here is the path to the folder where my module sits."
#sys.pa...     → "Look in this folder when importing modules."
import module 








# AVAILABLE FUNCTIONS:
# module.analysis(csv_path="", tolerance=):             initial analysis of your glucose fluctuations
# module.graph(df, output_path = "glucose_plot.png"):   draws graph from all the results
# module.vegetables(core):                              makes table to understand the effect of vegetables on glucose fluctuation
# module.day_request(df):                               allows you to ask for graph of a particular day


# you enter NAME of your DATA file 
data_dir = Path(__file__).resolve().parent.parent / "data"
csv_file = data_dir / "trial_3d.csv"  # <-- HERE
df = pd.read_csv(csv_file)

# you use the functions
core = module.analysis(csv_path=csv_file, tolerance=5)
module.graph(df, "full_graph.png")
module.vegetables(core)
module.day_request(df)