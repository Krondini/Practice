import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def addDonationAmt(state_amt_dict: dict, state: str, amt: float) -> None:
	
	state_amt_dict[state] += amt
	return None

def main():
    df = pd.read_csv("lobbyist_bundle.csv")
    cols = df.columns
    print("Columns: {}".format(cols))

    print(df.to_numpy().shape)
    df_clean = df.drop(['Link_Image'], axis=1).dropna()
    print(df_clean.to_numpy().shape)
    
    avg_q_amt = np.nanmean(df_clean['Quarterly_Contribution'])
    avg_year_amt = avg_q_amt*4
    # print("Average Quarterly Amount: ${:.2f}".format(avg_q_amt))
    # print("Average Yearly Amount: ${:.2f}".format(avg_year_amt))



    state_amt_dict = {state: 0 for state in df["Committee_Election_State"].unique() if type(state) == str}
    df_clean.apply(lambda row: addDonationAmt(state_amt_dict, row['Committee_Election_State'], row['Quarterly_Contribution']), axis=1)

    # print(state_amt_dict)

    above_avg_state = {k: v for (k, v) in sorted(state_amt_dict.items(), key=lambda elem: elem[1]) if v > avg_year_amt}
    print("States who gave more than the average:\n\t {}".format(above_avg_state.items()))
    print()
    below_avg_state = {k: v for (k, v) in sorted(state_amt_dict.items(), key=lambda elem: elem[1]) if v <= avg_year_amt}
    print("States who gave more less than the average:\n\t {}".format(below_avg_state.items()))

    

if __name__ == '__main__':
    main()