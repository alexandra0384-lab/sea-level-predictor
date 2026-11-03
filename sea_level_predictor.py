import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Datos originales')

    # Create first line of best fit
    ajuste_total = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    años_total = pd.Series(range(1880, 2051))
    ax.plot(
        años_total,
        ajuste_total.intercept + ajuste_total.slope * años_total,
        color='red',
        label='Tendencia desde 1880',
    )

    # Create second line of best fit
    df_recientes = df[df['Year'] >= 2000]
    ajuste_reciente = linregress(df_recientes['Year'], df_recientes['CSIRO Adjusted Sea Level'])
    años_recientes = pd.Series(range(2000, 2051))
    ax.plot(
        años_recientes,
        ajuste_reciente.intercept + ajuste_reciente.slope * años_recientes,
        color='green',
        label='Tendencia desde 2000',
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
