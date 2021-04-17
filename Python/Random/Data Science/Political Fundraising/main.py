import numpy as np 
import pandas as pd 
import matplotlib.pyplot as mpl 

def findAboveBelowAvgStates(df: pd.DataFrame) -> pd.DataFrame:

    

def main():
    df = pd.read_csv("lobbyist_bundle.csv")
    cols = df.columns

    print(df.to_numpy().shape)
    df_clean = df.drop(['Link_Image'], axis=1).dropna()
    print(df_clean.to_numpy().shape)
    
    avg_q_amt = np.nanmean(df_clean['Quarterly_Contribution'])
    avg_year_amt = avg_q_amt*4
    print(avg_q_amt)
    print(avg_year_amt)

    above_avg_states = df

if __name__ == '__main__':
    main()