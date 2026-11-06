import matplotlib.pyplot as plt
import pandas as pd

# Load 3-day dataset from data folder
df = pd.read_csv("../data/trial_3d.csv")

results_list = []

# Group by date so each day is analyzed independently
for date_val, df_day in df.groupby("date"):
  # Reset index for this specific day so 0, 1, 2... start fresh each morning
  df_day = df_day.reset_index(drop=True)

  for i in range(len(df_day)):
    if pd.notna(df_day.loc[i, "food"]):
      base = df_day.loc[i, "glucose_mg_dl"]
      food = df_day.loc[i, "food"]
      salad = (
          df_day.loc[i, "salads"]
          if pd.notna(df_day.loc[i, "salads"])
          else "No salad"
      )

      # Future window within this specific day
      future_slice = df_day.loc[i + 1 :]
      subsequent_meals = future_slice[future_slice["food"].notna()]

      if not subsequent_meals.empty:
        next_meal_idx = subsequent_meals.index[0]
        future = df_day.loc[i + 1 : next_meal_idx - 1]
      else:
        future = df_day.loc[i + 1 :]

      if not future.empty:
        m_val = future["glucose_mg_dl"].max()
        spike = m_val - base

        # Search for return with tolerance
        target_limit = base + 5
        recovery_rows = future[future["glucose_mg_dl"] <= target_limit]

        if not recovery_rows.empty:
          recovery_row = recovery_rows.iloc[0]
          recovery_time = recovery_row["hour"]
          recovery_index = recovery_rows.index[0]
          duration = recovery_index - i
        else:
          recovery_time = "Did not return"
          duration = None

        results_list.append({
            "Date": date_val,
            "Time": df_day.loc[i, "hour"],
            "Food": food,
            "Salad": salad,
            "Base": base,
            "Peak": m_val,
            "Spike": spike,
            "Duration": duration,
        })

# Create final summary DataFrame
core = pd.DataFrame(results_list)
print("\n--- FINAL ANALYSIS TABLE ---")
print(core.to_string())

# Plotting using continuous timestamps to prevent day overlap
df["timestamp"] = pd.to_datetime(df["date"] + " " + df["hour"])

plt.figure(figsize=(10, 5))
plt.plot(
    df["timestamp"],
    df["glucose_mg_dl"],
    marker="o",
    markersize=3,
    linestyle="-",
    color="teal",
)
plt.xlabel("Date & Time")
plt.ylabel("Glucose, mg/dl")
plt.xticks(rotation=45)
plt.title("Continuous Glucose Fluctuations")
plt.minorticks_on()
plt.grid(True)

plt.savefig("glucose_plot.png", dpi=300, bbox_inches="tight")
print("\nPlot saved as glucose_plot.png")

# adding vegetables comparison table

food_counts=core['Food'].value_counts()
food_repeat=food_counts[food_counts>1].index
comparison_subset=core[core["Food"].isin(food_repeat)]
print("\n--- COMPARISON FOR REPEATED FOODS ---")
print(comparison_subset[["Food", "Salad", "Spike", "Duration"]])

      
  