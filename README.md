# Project
INTERNSHIP PROJECT 
# Financial KPI Analysis for a Startup

## 🧭 Project Overview

This project delivers a data-driven analysis of a startup's financial and customer performance using five critical metrics:

* **Monthly Revenue & Expenses**
* **Burn Rate** (Cash usage efficiency)
* **Customer Acquisition Cost (CAC)**
* **Customer Lifetime Value (LTV)**
* **LTV\:CAC Ratio** (Profitability indicator)

Tools used include **Excel**, **Python (Pandas/Matplotlib)**, and **Power BI** to extract actionable insights from financial data.

---

## 📊 Key Business Questions Answered

* How efficiently is the startup acquiring customers?
* What’s the burn rate trend over the year?
* Are customers returning enough value (LTV) to justify CAC?
* When was acquisition most profitable?
* Are there warning zones for spending or retention?

---


## 🧮 KPIs Engine (Python)

The `kpi_engine.py` script performs:

* Monthly **Burn Rate** computation
* CAC and ARPU calculations
* LTV = ARPU × 6 (assumed retention)
* LTV\:CAC Ratio computation
* Clean export to CSV for visualization

This allows real-time tracking and future integration with APIs for live dashboards.

---

## 📈 Dashboard Preview

Visuals include:

* Revenue vs Expenses vs Burn (line chart)
* CAC & LTV over months (dual axis)
* LTV\:CAC Ratio (bar chart with threshold line)
* Customers acquired by month (bar)

**Filters**: Month range slicer | KPI selector

---

## 📌 Insights & Recommendations

* **LTV\:CAC Ratio > 5** in multiple months indicates highly efficient acquisition.
* **April** shows peak expenses → review ROI of campaigns.
* **Burn rate volatility** signals need for better cost forecasting.
* **Consistent ARPU** = healthy monetization, solid PMF.

---

## 🔧 Tools Used

* **Power BI** – Visual storytelling & executive dashboards
* **Python** – Data engineering, KPI logic
* **Excel** – Early-stage analysis, formatting



---

## 📬 Future Scope

* Live API integration (Stripe, CRM)
* CAC segmentation by source/channel
* ML-based LTV forecasting
* Automated retention cohort heatmaps


