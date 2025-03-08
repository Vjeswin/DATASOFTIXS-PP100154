import pandas as pd
import matplotlib.pyplot as plt
import os
def analyze_csv(salary_data):
    if not os.path.exists(salary_data):
        print("Error: File not found. Please check the file path.")
        return
    try:
        df = pd.read_csv(salary_data)
        if df.empty:
            print("Error: The CSV file is empty.")
            return
        print("\nAvailable columns:")
        for i, col in enumerate(df.columns, 1):
            print(f"{i}. {col}")       
        try:
            col_index = int(input("Enter the column number to analyze: ").strip()) - 1
            if col_index not in range(len(df.columns)):
                print("Error: Invalid column number.")
                return
            column = df.columns[col_index]
        except ValueError:
            print("Error: Please enter a valid number.")
            return   
        df[column] = pd.to_numeric(df[column], errors='coerce')
        df = df.dropna(subset=[column])
        if df[column].empty:
            print("Error: No valid numerical data in the selected column.")
            return
        avg_value = df[column].mean()
        max_value = df[column].max()
        min_value = df[column].min()
        print(f"\nStatistics for column '{column}':")
        print(f"Average: {avg_value:.2f}")
        print(f"Maximum: {max_value}")
        print(f"Minimum: {min_value}")
        visualize = input("\nWould you like to visualize the data? (yes/no): ").strip().lower()
        if visualize == 'yes':
            unique_values = df[column].nunique()
            plt.figure(figsize=(8, 5))
            if unique_values < 10:
                df[column].value_counts().plot(kind='bar', edgecolor='black')
                plt.ylabel('Count')
            else:
                plt.hist(df[column], bins=20, edgecolor='black')
                plt.ylabel('Frequency')
            plt.xlabel(column)
            plt.title(f'Distribution of {column}')
            plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    salary_data = input("Enter the path to the CSV file: ").strip()
    analyze_csv(salary_data)

