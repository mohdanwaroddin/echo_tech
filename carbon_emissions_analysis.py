import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import json
import requests
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
        if not self.power_data:
            print("No power data available to display.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.power_data, marker='o')
        plt.title('Real-Time Power Usage')
        plt.xlabel('Time (s)')
        plt.ylabel('Power Usage (kW)')
        plt.grid(True)
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
        if not self.power_data or not self.carbon_data:
            print("Insufficient data to generate report.")
            return
        
        report = {
            'Device ID': self.device_id,
            'Total Power Consumption (kWh)': sum(self.power_data),
            'Total Carbon Emission (kgCO2e)': sum(self.carbon_data),
        }
        with open(f'report_device_{self.device_id}.json', 'w') as f:
            json.dump(report, f, indent=4)
        print(f'Report generated for Device {self.device_id}')

# API Interaction (Example with Carbon Interface API)
class CarbonInterfaceAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def estimate_emissions(self, energy_consumed):
        url = "https://www.carboninterface.com/api/v1/estimates"
        data = {
            "type": "electricity",
            "electricity_unit": "kwh",
            "electricity_value": energy_consumed,
            "country": "us"
        }
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
        return None

# Visualization Functions
def plot_power_consumption_over_time():
    try:
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
    except FileNotFoundError:
        print("File not found. Please ensure the dataset file is available.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

def plot_total_carbon_emissions_by_device():
    try:
        data = pd.read_csv('total_carbon_emissions_by_device.csv')
        plt.figure(figsize=(10, 6))
        plt.bar(data['Device'], data['Total_Emissions'], color='skyblue')
        plt.xlabel("Device Type")
        plt.ylabel("Total Carbon Emissions (kgCO2e)")
        plt.title("Total Carbon Emissions by Device")
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("File not found. Please ensure the dataset file is available.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

def plot_power_consumption_distribution():
    try:
        data = pd.read_csv('power_consumption_distribution.csv')
        plt.figure(figsize=(8, 8))
        plt.pie(data['Power_Consumption'], labels=data['Device'], autopct='%1.1f%%',
                colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title("Power Consumption Distribution")
        plt.show()
    except FileNotFoundError:
        print("File not found. Please ensure the dataset file is available.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

def plot_carbon_emissions_reduction_potential():
    try:
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
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("File not found. Please ensure the dataset file is available.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

def plot_real_time_emissions_monitoring():
    try:
        data = pd.read_csv('real_time_emissions_monitoring.csv')
        total_emissions_today = data['Current_Emissions'].sum()

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        axs[0, 0].plot(data['Timestamp'], data['Current_Power'], marker='o')
        axs[0, 0].set_title('Current Power Usage (kW)')
        axs[0, 0].set_ylim(0, 0.06)

        axs[0, 1].plot(data['Timestamp'], data['Current_Power'], label="Power Usage")
        axs[0, 1].set_title('Real-Time Power Consumption')
        axs[0, 1].set_xlabel("Time")
        axs[0, 1].set_ylabel("Power Usage (kW)")
        axs[0, 1].legend()

        axs[1, 0].bar(data['Timestamp'], data['Current_Emissions'], color='green')
        axs[1, 0].set_title('Real-Time Carbon Emissions (kgCO2e)')
        axs[1, 0].set_xlabel("Time")
        axs[1, 0].set_ylabel("Emissions (kgCO2e)")

        axs[1, 1].text(0.5, 0.5, f'Total Emissions Today: {total_emissions_today:.4f} kgCO2e', fontsize=16, ha='center')
        axs[1, 1].axis('off')

        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("File not found. Please ensure the dataset file is available.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

def plot_carbon_emissions_over_time():
    try:
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
    except FileNotFoundError:
        print("File not found. Please ensure the dataset file is available.")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

# Usage Example for Real-Time Power Tracking and Dashboard
device_id = "Laptop123"
tracker = RealTimePowerTracker(device_id)
power_data = tracker.track_power(duration=60)

# Using Carbon Interface API
api_key = "VOPqQ16QxmdfsKnrdHfLbQ"
carbon_api = CarbonInterfaceAPI(api_key)
emission_data = carbon_api.estimate_emissions(energy_consumed=sum(power_data))

if emission_data:
    print("Carbon Emission Estimate:", emission_data)

# Generate an analytics dashboard
dashboard = AnalyticsDashboard(power_data)
dashboard.display_power_usage()

# Example plotting functions
plot_power_consumption_over_time()
plot_total_carbon_emissions_by_device()
plot_power_consumption_distribution()
plot_carbon_emissions_reduction_potential()
plot_real_time_emissions_monitoring()
plot_carbon_emissions_over_time()
