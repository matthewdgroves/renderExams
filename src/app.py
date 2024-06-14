import pandas as pd
import plotly.express as px
from dash import dcc, Dash, html

summary_dict = {
    'Student': 
        {0: 'Abbott, Luke', 1: 'Ammons, Waylon', 2: 'Ashton, John', 4: 'Balette, Forrest', 5: 'Biggs, Marley', 6: 'Billcheck, Helen', 8: 'Bullock-Coles, Danzelle', 9: 'Carter, Josephine', 
         10: 'Couling, Gavin', 11: 'Dalton, Taylor', 12: 'de Vink, Cosmo', 13: 'Edelberg-Moore, Ella', 14: 'Edwards, Harrison', 15: 'Elias, William', 16: 'Esposito, Sebastian', 17: 'Fagan, Imogen', 18: 'Fleming, Sally', 19: 'Garbacky, Gabriel', 
         20: 'Gearhart, Owen', 21: 'Geismar, Lance', 22: 'George, Mary', 23: 'Granville, Charles', 24: 'Hanley, Margaret', 25: 'Hartog, Anne', 26: 'Horton, Caroline', 27: 'Horton, Isabel', 28: 'Horton, Isabel', 29: 'Humphreys, Quinn', 
         30: 'Ismailova, Diana', 31: 'Johnson, Campbell', 32: 'Johnston, Giada', 34: 'Kelly, Jackson', 35: 'Kestner, Jones', 36: 'Lawson, Frances', 37: 'Miller, Charlotte', 39: 'Moyer, Corbett', 
         40: 'Murphy, Quinn', 41: 'Ng, Edwin', 42: 'Norment, William', 43: 'Oakey, Darby', 44: 'Parlee, Jacob', 45: 'Pisani, Elizabeth', 46: 'Pisani, Mia', 47: 'Reed, James', 48: 'Ross, Kayleigh', 49: 'Sanchez, Raelon', 
         50: 'Sheehy, Alina', 51: 'Van Santvoord, Jackson', 52: 'Williams, Harmony', 53: 'Womack, Elizabeth', 54: 'Yang, Kaichun', 55: 'Zhang, Wenshi', 56: 'Biggs, Ezra', 57: 'Bingler, Emma', 58: 'Brown, Zaria', 59: 'Clark, Thomas', 
         60: 'Cole, Holmes', 61: 'de Vink, Cassia', 62: 'Elias, Ellen', 63: 'Eliason, Quinn', 64: 'Farnsworth, Blake', 65: 'Fisher, John', 66: 'Gatt, Joaquin', 67: 'Hawkins, Quinn', 68: 'Hyonkeu, Ange', 69: 'Kamalsky, Taylor', 
         70: 'Ledger, Emily', 71: 'Matula, Joshua', 72: 'Meney, Carli', 73: 'Moore, Oliver', 74: 'Morris, Harrison', 75: 'Pittard, Evelyn', 76: 'Rannigan, Matteo', 77: 'Raymond, Davis', 78: 'Roberts, Holden', 79: 'Ross, Parker', 
         80: 'Shifflett, Madelin', 81: 'Steeper, Ryan', 82: 'Villines, Dax', 83: 'Walden, Sylas', 84: 'Welsh, Liam', 85: 'Williams, Junius'}, 
    'Review Packet Total': {0: 11.5, 1: 14.0, 2: 14.25, 4: 7.800000000000001, 5: 10.6, 6: 15.0, 8: 10.1, 9: 11.5, 10: 15.0, 11: 14.0, 12: 15.0, 13: 10.1, 14: 15.0, 15: 15.0, 16: 15.0, 17: 14.5, 18: 13.5, 19: 10.0, 20: 11.0, 21: 14.5, 22: 12.5, 23: 14.0, 24: 15.0, 25: 12.0, 26: 8.2, 27: 11.5, 28: 7.5, 29: 14.5, 30: 7.800000000000001, 31: 15.0, 32: 11.5, 34: 10.0, 35: 14.0, 36: 15.0, 37: 14.5, 39: 12.0, 40: 15.0, 41: 14.5, 42: 12.5, 43: 14.0, 44: 11.0, 45: 13.5, 46: 13.5, 47: 7.5, 48: 11.0, 49: 8.1, 50: 6.5, 51: 15.0, 52: 14.5, 53: 15.0, 54: 7.5, 55: 11.0, 56: 13.5, 57: 9.0, 58: 7.5, 59: 12.75, 60: 9.5, 61: 14.5, 62: 9.25, 63: 13.0, 64: 10.25, 65: 11.0, 66: 10.5, 67: 8.5, 68: 9.0, 69: 13.5, 70: 15.0, 71: 9.0, 72: 9.5, 73: 11.0, 74: 13.5, 75: 11.0, 76: 8.6, 77: 10.0, 78: 11.5, 79: 7.5, 80: 8.85, 81: 14.5, 82: 8.35, 83: 14.0, 84: 7.5, 85: 11.5}, 
    'Final Exam': {0: 2.4, 1: 1.955, 2: 3.55, 4: 2.58, 5: 2.4, 6: 3.225, 8: 1.2, 9: 2.875, 10: 3.15, 11: 2.725, 12: 2.79, 13: 2.35, 14: 3.409, 15: 2.475, 16: 3.42, 17: 3.4, 18: 2.865, 19: 2.8, 20: 1.7, 21: 2.65, 22: 1.72, 23: 3.275, 24: 2.64, 25: 1.725, 26: 2.325, 27: 2.825, 28: 2.825, 29: 3.25, 30: 1.75, 31: 2.9, 32: 2.35, 34: 3.35, 35: 2.75, 36: 2.87, 37: 2.25, 39: 1.625, 40: 3.055, 41: 2.7, 42: 1.75, 43: 2.235, 44: 2.175, 45: 2.25, 46: 2.675, 47: 2.4, 48: 2.15, 49: 2.39, 50: 2.05, 51: 3.5, 52: 2.3, 53: 3.475, 54: 2.55, 55: 2.525, 56: 2.268, 57: 1.58, 58: 0.739, 59: 1.732, 60: 2.161, 61: 3.346, 62: 2.286, 63: 3.05, 64: 1.668, 65: 1.429, 66: 0.93, 67: 1.161, 68: 0.969, 69: 2.714, 70: 3.556, 71: 1.857, 72: 1.75, 73: 2.589, 74: 2.839, 75: 3.018, 76: 2.214, 77: 1.768, 78: 2.73, 79: 2.071, 80: 0.804, 81: 2.839, 82: 0.668, 83: 1.11, 84: 1.268, 85: 3.304}
    }
summary = pd.DataFrame.from_dict(summary_dict)

fig = px.scatter(summary, x="Review Packet Total", y="Final Exam", hover_name="Student", trendline="ols", title="Performance vs Preparation on the Exam")

app = Dash()
server = app.server
app.layout = html.Div([
    # html.H1(children='Comparing Performance vs. Preparation on the Exam', style={
    #     'textAlign':'center',
    #     }),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True, port=8059)