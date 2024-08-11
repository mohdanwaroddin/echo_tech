import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import json
import numpy as np

# Carbon Footprint Calculator
class CarbonFootprintCalculator:
    def __init__(self, device_type, usage_hours_per_day, energy_source_emission_factor):
        self.device_type = device_type
        self.usage_hours_per_day = usage_hours_per_day
        self.energy_source_emission_factor = energy_source_emission_factor

    def calculate_daily_footprint(self, power_rating):
        daily_energy_consumption = self.usage_hours_per_day * power_rating  # kWh
        daily_carbon_emission = daily_energy_consumption * self.energy_source_emission_factor  # kgCO2e
        return daily_carbon_emission

# Real-Time Power Tracker
class RealTimePowerTracker:
    def __init__(self, device_id):
        self.device_id = device_id
        self.power_consumption_data = []

    def track_power(self, duration=60):
        for _ in range(duration):
            current_power_usage = random.uniform(0.01, 0.1)  # Simulate power usage in kW
            self.power_consumption_data.append(current_power_usage)
            print(f'Device {self.device_id} - Current Power Usage: {current_power_usage:.3f} kW')
            time.sleep(1)  # Simulate real-time data collection every second
        return self.power_consumption_data

# Analytics Dashboard
class AnalyticsDashboard:
    def __init__(self, power_data):
        self.power_data = power_data

    def display_power_usage(self):
        plt.plot(self.power_data, marker='o')
        plt.title('Real-Time Power Usage')
        plt.xlabel('Time (s)')
        plt.ylabel('Power Usage (kW)')
        plt.show()

# Reduction Strategies
class ReductionStrategies:
    def __init__(self, current_usage):
        self.current_usage = current_usage

    def optimize_device_usage(self):
        optimized_usage = self.current_usage * 0.9  # Assume a 10% reduction through optimization
        return optimized_usage

# Emission Report
class EmissionReport:
    def __init__(self, device_id, power_data, carbon_data):
        self.device_id = device_id
        self.power_data = power_data
        self.carbon_data = carbon_data

    def generate_report(self):
        report = {
            'Device ID': self.device_id,
            'Total Power Consumption (kWh)': sum(self.power_data),
            'Total Carbon Emission (kgCO2e)': sum(self.carbon_data),
        }
        with open(f'report_device_{self.device_id}.json', 'w') as f:
            json.dump(report, f, indent=4)
        print(f'Report generated for Device {self.device_id}')

# Function to plot Power Consumption Over Time (Line Chart)
def plot_power_consumption_over_time():
    data = pd.read_csv('power_consumption_over_time.csv')
    plt.figure(figsize=(10, 6))
    plt.plot(data['Timestamp'], data['Laptop'], label='Laptop')
    plt.plot(data['Timestamp'], data['Desktop'], label='Desktop')
    plt.plot(data['Timestamp'], data['Monitor'], label='Monitor')
    plt.plot(data['Timestamp'], data['Smartphone'], label='Smartphone')
    plt.xlabel("Time")
    plt.ylabel("Power Usage (kW)")
    plt.title("Power Consumption Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot Total Carbon Emissions by Device (Bar Chart)
def plot_total_carbon_emissions_by_device():
    data = pd.read_csv('total_carbon_emissions_by_device.csv')
    plt.figure(figsize=(10, 6))
    plt.bar(data['Device'], data['Total_Emissions'], color='skyblue')
    plt.xlabel("Device Type")
    plt.ylabel("Total Carbon Emissions (kgCO2e)")
    plt.title("Total Carbon Emissions by Device")
    plt.show()

# Function to plot Power Consumption Distribution (Pie Chart)
def plot_power_consumption_distribution():
    data = pd.read_csv('power_consumption_distribution.csv')
    plt.figure(figsize=(8, 8))
    plt.pie(data['Power_Consumption'], labels=data['Device'], autopct='%1.1f%%',
            colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title("Power Consumption Distribution")
    plt.show()

# Function to plot Carbon Emissions Reduction Potential (Stacked Bar Chart)
def plot_carbon_emissions_reduction_potential():
    data = pd.read_csv('carbon_emissions_reduction_potential.csv')
    r = np.arange(len(data['Device']))
    plt.figure(figsize=(10, 6))
    plt.bar(r, data['Current_Emissions'], color='blue', edgecolor='grey', width=0.5, label='Current Emissions')
    plt.bar(r, data['Reduction_Emissions'], bottom=data['Current_Emissions'], color='orange', edgecolor='grey', width=0.5, label='Post-Reduction Emissions')
    plt.xlabel("Device Type")
    plt.ylabel("Carbon Emissions (kgCO2e)")
    plt.title("Carbon Emissions Reduction Potential")
    plt.xticks(r, data['Device'])
    plt.legend()
    plt.show()

# Function to plot Real-Time Emissions Monitoring Dashboard (Multiple Widgets)
def plot_real_time_emissions_monitoring():
    data = pd.read_csv('real_time_emissions_monitoring.csv')
    total_emissions_today = data['Current_Emissions'].sum()

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Gauge-like chart for current power usage (emulating a gauge)
    axs[0, 0].plot(data['Timestamp'], data['Current_Power'], marker='o')
    axs[0, 0].set_title('Current Power Usage (kW)')
    axs[0, 0].set_ylim(0, 0.06)

    # Line chart for real-time power consumption
    axs[0, 1].plot(data['Timestamp'], data['Current_Power'], label="Power Usage")
    axs[0, 1].set_title('Real-Time Power Consumption')
    axs[0, 1].set_xlabel("Time")
    axs[0, 1].set_ylabel("Power Usage (kW)")
    axs[0, 1].legend()

    # Bar chart for real-time carbon emissions
    axs[1, 0].bar(data['Timestamp'], data['Current_Emissions'], color='green')
    axs[1, 0].set_title('Real-Time Carbon Emissions (kgCO2e)')
    axs[1, 0].set_xlabel("Time")
    axs[1, 0].set_ylabel("Emissions (kgCO2e)")

    # Text/Number display for total carbon emissions today
    axs[1, 1].text(0.5, 0.5, f'Total Emissions Today: {total_emissions_today:.4f} kgCO2e', fontsize=16, ha='center')
    axs[1, 1].axis('off')

    plt.tight_layout()
    plt.show()

# Function to plot Stacked Area Chart for Carbon Emissions Over Time
def plot_carbon_emissions_over_time():
    # Load data
    data = pd.read_csv('power_consumption_over_time.csv')
    
    # Calculate carbon emissions for each device (assuming an emission factor)
    emission_factor = 0.5  # kgCO2e per kWh
    data['Laptop_Emissions'] = data['Laptop'] * emission_factor
    data['Desktop_Emissions'] = data['Desktop'] * emission_factor
    data['Monitor_Emissions'] = data['Monitor'] * emission_factor
    data['Smartphone_Emissions'] = data['Smartphone'] * emission_factor
    
    # Prepare data for stacked area plot
    emissions_data = data[['Laptop_Emissions', 'Desktop_Emissions', 'Monitor_Emissions', 'Smartphone_Emissions']]
    timestamps = data['Timestamp']
    
    # Plot the stacked area chart
    plt.figure(figsize=(10, 6))
    plt.stackplot(timestamps, 
                  emissions_data['Laptop_Emissions'], 
                  emissions_data['Desktop_Emissions'], 
                  emissions_data['Monitor_Emissions'], 
                  emissions_data['Smartphone_Emissions'],
                  labels=['Laptop', 'Desktop', 'Monitor', 'Smartphone'],
                  colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    
    plt.xlabel("Time")
    plt.ylabel("Carbon Emissions (kgCO2e)")
    plt.title("Device Carbon Emissions Over Time")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Load sample data
    power_consumption_df = pd.read_csv('power_consumption_over_time.csv')
    emission_data_df = pd.read_csv('total_carbon_emissions_by_device.csv')
    reduction_potential_df = pd.read_csv('carbon_emissions_reduction_potential.csv')

    # Example: Carbon Footprint Calculation for a Laptop
    laptop_calculator = CarbonFootprintCalculator(device_type='Laptop', usage_hours_per_day=8, energy_source_emission_factor=0.5)
    daily_footprint = laptop_calculator.calculate_daily_footprint(power_rating=0.05)
    print(f'Daily Carbon Footprint for Laptop: {daily_footprint:.4f} kgCO2e')

    # Example: Real-Time Power Tracking for a Device
    tracker = RealTimePowerTracker(device_id=1)
    power_data = tracker.track_power(duration=10)

    # Example: Display Analytics Dashboard
    dashboard = AnalyticsDashboard(power_data=power_data)
    dashboard.display_power_usage()

    # Example: Generate Emission Report
    emission_report = EmissionReport(device_id=1, power_data=power_data, carbon_data=[0.02 * p for p in power_data])
    emission_report.generate_report()

    # Plotting the visualizations
    plot_power_consumption_over_time()
    plot_total_carbon_emissions_by_device()
    plot_power_consumption_distribution()
    plot_carbon_emissions_reduction_potential()
    plot_real_time_emissions_monitoring()
    plot_carbon_emissions_over_time()
