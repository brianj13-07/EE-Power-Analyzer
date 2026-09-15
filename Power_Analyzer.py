import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("electrical_data.csv")
print(data)
def calculate_power(data):
    data["Power"]= data["Voltage"]*data["Current"]
    return(data)
data= calculate_power(data)
print(data)
def calculate_statistics(data):
    average_Voltage= data["Voltage"].mean()
    average_Current= (data["Current"]).mean()
    average_Power= (data["Power"]).mean()
    Max_Power= (data["Power"]).max()
    Min_Power= (data["Power"]).min()
    print(f"Average Volatge: {average_Voltage:.2f} V")
    print(f"Average Current: {average_Current:.2f} A")
    print(f"Average Power: {average_Power:.2f} W")
    print(f"Maximum Power: {Max_Power:.2f} W")
    print(f"Minimum Power: {Min_Power:.2f} W")
    return(data)
calculate_statistics(data)
def create_graphs(data):
    plt.figure()
    plt.plot(data["Time"], data["Voltage"])
    plt.title("Voltage Vs Time")
    plt.xlabel("Time(s)")
    plt.ylabel("Voltage(V)")
    plt.figure()
    plt.plot(data["Time"], data["Current"])
    plt.title("Current Vs Time")
    plt.xlabel("Time(s)")
    plt.ylabel("Current(A)")
    plt.figure()
    plt.plot(data["Time"], data["Power"])
    plt.title("Power Vs Time")
    plt.xlabel("Time(s)")
    plt.ylabel("Power(W)")
    plt.show()
    return(data)
create_graphs(data)
def calculate_resistance(data):
    if (data["Current"] == 0).any():
        print("Undefined")
    else:
        data["Resistance"]= data["Voltage"]/data["Current"]
        average_resistance= data["Resistance"].mean()
        max_resistance= data["Resistance"].max()
        min_resistance= data["Resistance"].min()
        print(data)
        print(f"Average Resistance: {average_resistance:.2f} Ω")
        print(f"Maximum Resistance: {max_resistance:.2f} Ω")
        print(f"Minimum Resistance: {min_resistance:.2f} Ω")
    return(data)
data= calculate_resistance(data)
data.to_csv("analyzed_data.csv", index=False)

