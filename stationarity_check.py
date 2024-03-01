from ib_insync import IB, Stock, util
from statsmodels.tsa.stattools import adfuller, kpss
import os
import numpy as np
from scipy import stats, optimize
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to Interactive Brokers
def connect_to_ib():
    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)  # Adjust host and port if necessary
    return ib

# Fetch historical data
# To fect a specific time frame replace "duration" with: start_date, end_date,
def fetch_data(ib, symbol, duration, bar_size, start_date, end_date):
    contract = Stock(symbol, 'SMART', 'USD')
    ib.qualifyContracts(contract)
    #..........................................................................
	#for specific time frames uncomment the following:
    #Format dates
    #dt_format = "%Y-%m-%d"
    #start_date_dt = datetime.strptime(start_date, dt_format)
    #end_date_dt = datetime.strptime(end_date, dt_format)
    #Calculate duration
    #duration_days = (end_date_dt - start_date_dt).days
    #duration_str = f"{duration_days} D"
	#.........................................................................
	
	#.........................................................................
	#For specific time frames instead of durations, comment out the following:...
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='', #20240223 15:59:59 US/Eastern
        durationStr=duration,
        barSizeSetting=bar_size,
        whatToShow='MIDPOINT',
        useRTH=True,
        formatDate=1)
    return [bar.close for bar in bars]
	#....and uncomment the following instead:
    #bars = ib.reqHistoricalData(
    #    contract,
    #    endDateTime=end_date_dt.strftime('%Y%m%d') + " 15:59:59",  # Ensure we cover the end day
    #    durationStr=duration_str,
    #    barSizeSetting=bar_size,
    #    whatToShow='MIDPOINT',
    #    useRTH=True,
    #    formatDate=1)
    
    # Convert to DataFrame for easier handling
    #df = util.df(bars)
    #return df
	#.....................................................

# ADF test for stationarity
def adf_test(series):
    result = adfuller(series, regression='ct', autolag='AIC') #autolag='AIC' maxlag=0
    print("ADF Test Result:")
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print(f'Number of lags used: {result[2]}')
    for key, value in result[4].items():
        print(f'Critical Value ({key}): {value}')
    # Summary
    if result[1] < 0.05:
        print("Evidence suggests the series is stationary.")
        time = np.arange(len(series))  # Generate time indices if not already provided
        time_squared = time ** 2  # Square of time indices for the quadratic component

		# Fit a quadratic model (second-degree polynomial)   
        coefficients, residuals, _, _, _ = np.polyfit(time, series, 2, full=True)
		#Alternative:
		#params, _ = optimize.curve_fit(lambda t, a, b, c: a + b*t + c*t**2, time, data)

		# Calculate the fitted values
        fitted_values = np.polyval(coefficients, time)
		#Alternative
		#fitted_values = params[0] + params[1]*time + params[2]*time**2

		# Calculate residuals (actual - fitted)
        residuals = series - fitted_values

		# Calculate the mean of the residuals
        mean_residual = np.mean(residuals)
		
        detrended_mean = np.mean(residuals)
        latest_deviation = residuals[-1] - detrended_mean
        print(f"Mean around the quadratic trend: {mean_residual}")
        print(f"Detrended Mean: {detrended_mean}")
        print(f"Latest Deviation from Detrended Mean: {latest_deviation}")
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(time, series, label='Original Series')
        plt.plot(time, fitted_values, label='Quadratic Trend', linestyle='--')
        plt.title('Series and Fitted Quadratic Trend')
        plt.xlabel('Time')
        plt.ylabel('Series Value')
        plt.legend()
        plt.show()
    else:
        print("Evidence suggests the series is not stationary.")

# KPSS test for stationarity
def kpss_test(series):
    result = kpss(series, regression='ct', nlags='auto')
    print("\nKPSS Test Result:")
    print(f'KPSS Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    for key, value in result[3].items():
        print(f'Critical Value ({key}): {value}')
    # Summary
    if result[1] < 0.05:
        print("Evidence suggests the series is not stationary.")
    else:
        print("Evidence suggests the series is stationary.")

# Main function to run the tests
def main(symbol, duration, bar_size, start_date, end_date):
    ib = connect_to_ib()
    try:
        series = fetch_data(ib, symbol, duration, bar_size, start_date, end_date)
        if series:
            adf_test(series)
            kpss_test(series)
        else:
            print("No data fetched. Please check your parameters or connection.")
    finally:
        ib.disconnect()

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    # Assume the operating system is Linux or Mac
    else:
        os.system('clear')

# Example usage
if __name__ == "__main__":
    symbol = 'SPY'  # Enter the symbol
	
	# Time span of all the bars. Examples: ‘60 S’, ‘30 D’, ‘13 W’, ‘6 M’, ‘10 Y’.
    duration = '3 D'  
    start_date = '2024-02-05'
    end_date = '20240214-20:59:59'
	
	#barSizeSetting (str) – Time period of one bar. Must be one of: 
	#‘1 secs’, ‘5 secs’, ‘10 secs’ 15 secs’, ‘30 secs’, ‘1 min’, ‘2 mins’, ‘3 mins’, ‘5 mins’, ‘10 mins’, ‘15 mins’, ‘20 mins’, ‘30 mins’, 
	#‘1 hour’, ‘2 hours’, ‘3 hours’, ‘4 hours’, ‘8 hours’, ‘1 day’, ‘1 week’, ‘1 month’.
    bar_size = '5 secs'  # Daily bars
    
    clear_screen()
	
	# To fect a specific time frame replace "duration" with: start_date, end_date,
    main(symbol, duration, bar_size, start_date, end_date)
