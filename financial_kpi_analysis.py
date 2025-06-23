
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style="whitegrid")

DATA_PATH = "startup_financials.csv"
OUTPUT_DIR = Path("output_kpi_reports")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_data(path):
    df = pd.read_csv(path, parse_dates=['Month'])
    df.sort_values('Month', inplace=True)
    return df

def calculate_kpis(df):
    df['Burn Rate'] = df['Expenses'] - df['Revenue']
    df['Run Rate'] = df['Revenue'].iloc[-1] * 12  # Assuming last month is representative
    df['LTV:CAC'] = df['LTV'] / df['CAC']
    df['Cohort'] = df['Month'].dt.to_period('M')
    return df

def cohort_retention(df):
    df['Customer_ID'] = df.groupby('Cohort').cumcount() + 1  # fake customer index
    cohort_pivot = pd.pivot_table(
        df,
        index='Cohort',
        columns='Customer_ID',
        values='Revenue',
        aggfunc='count'
    ).fillna(0).cumsum(axis=1)
    cohort_retention = cohort_pivot.divide(cohort_pivot.iloc[:, 0], axis=0)
    return cohort_retention

def plot_kpis(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Month'], df['Revenue'], label='Revenue', marker='o')
    plt.plot(df['Month'], df['Expenses'], label='Expenses', marker='o')
    plt.plot(df['Month'], df['Burn Rate'], label='Burn Rate', marker='o')
    plt.title('Revenue, Expenses and Burn Rate Over Time')
    plt.xlabel('Month')
    plt.ylabel('INR')
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_expenses_burnrate.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.plot(df['Month'], df['CAC'], label='CAC', marker='o', color='purple')
    plt.plot(df['Month'], df['LTV'], label='LTV', marker='o', color='green')
    plt.title('CAC vs LTV')
    plt.xlabel('Month')
    plt.ylabel('INR')
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "cac_vs_ltv.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=df['Month'].dt.strftime('%b-%Y'), y=df['LTV:CAC'], palette='coolwarm')
    plt.axhline(3, color='gray', linestyle='--', label='Benchmark: 3')
    plt.title('LTV:CAC Ratio by Month')
    plt.ylabel('Ratio')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "ltv_cac_ratio.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    plt.bar(df['Month'].dt.strftime('%b-%Y'), df['Customers Acquired'], color='skyblue')
    plt.title('Monthly Customers Acquired')
    plt.xticks(rotation=45)
    plt.ylabel('Number of Customers')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "customers_acquired.png")
    plt.close()

def generate_summary(df):
    summary = {
        'Total Revenue': df['Revenue'].sum(),
        'Total Expenses': df['Expenses'].sum(),
        'Average Burn Rate': df['Burn Rate'].mean(),
        'Latest Run Rate': df['Run Rate'].iloc[-1],
        'Average CAC': df['CAC'].mean(),
        'Average LTV': df['LTV'].mean(),
        'Average LTV:CAC': df['LTV:CAC'].mean()
    }
    report_path = OUTPUT_DIR / "summary_metrics.txt"
    with open(report_path, "w") as f:
        for k, v in summary.items():
            f.write(f"{k}: {v:,.2f}\n")
    print(f"[✓] Summary saved to {report_path}")

def main():
    print("[...] Loading data...")
    df = load_data(DATA_PATH)

    print("[✓] Calculating metrics...")
    df = calculate_kpis(df)

    print("[✓] Generating KPI plots...")
    plot_kpis(df)

    print("[✓] Generating summary report...")
    generate_summary(df)

    print("[✓] All done! Output saved to:", OUTPUT_DIR.resolve())

if __name__ == "__main__":
    main()
