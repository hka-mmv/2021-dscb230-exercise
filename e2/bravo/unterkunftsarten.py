import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as ple

df = pd.read_csv("AB_NYC_2019(cleaned).csv")

room_Types = df.room_type

print(room_Types)
