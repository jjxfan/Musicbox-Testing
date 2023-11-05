import seaborn 
from matplotlib import pyplot
import pandas

FILE_PATH = 'concentration.csv'

# Graph a heatmap, which is really a scatterplot in disguise. 
def graph_function():
    print("Please give the concentration to be plotted on the x-axis.")
    x_axis_col = str(input())
    print("Please give the concentration to be plotted on the y-axis.")
    y_axis_col = str(input())
    print("Please give the name of the concentration we are graphing.")
    relative_conc_label = str(input())

    concentration_data = pandas.read_csv(FILE_PATH)
    filtered_by_timestamp = concentration_data.filter(regex='^\\d+$')
    max_concentrations = list(range(len(filtered_by_timestamp.index)))
    for ind, row in filtered_by_timestamp.iterrows():
        max_concentrations[ind] = row.max()
    
    graphedData = pandas.DataFrame()
    graphedData[x_axis_col] = concentration_data[x_axis_col]
    graphedData[y_axis_col] = concentration_data[y_axis_col]
    graphedData[relative_conc_label] = max_concentrations
    seaborn.scatterplot(x=x_axis_col, y=y_axis_col, hue=relative_conc_label)
    pyplot.xlabel(x_axis_col)
    pyplot.ylabel(y_axis_col)
    pyplot.title(f"Maximum {relative_conc_label}, when given initial concentrations of {x_axis_col} and {y_axis_col}")
    pyplot.savefig("Simulation.png")
    print("Successfully Graphed and Saved!")




