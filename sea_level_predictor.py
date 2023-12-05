import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope * df['Year'] + intercept, 'r', label='Linear Fit Full Data')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope_recent * df['Year'] + intercept_recent, 'k', label='Linear Fit 2000-Recent')

    # Add vertical dashed green line at the intersection point
    intersection_year = (intercept_recent - intercept) / (slope - slope_recent)
    plt.axvline(x=intersection_year, linestyle='--', color='g', label='Intersection')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Display legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == '__main__':
    draw_plot()
