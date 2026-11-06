import pandas as pd
import matplotlib.pyplot as plt

data = {
    "hour": [
        "07:00",
        "08:00",
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00",
    ],
    "glucose_mg_dl": [
        90,
        95,
        135,
        120,
        100,
        98,
        145,
        130,
        105,
        95,
        92,
        140,
        125,
        100,
        95,
    ],
    "food": [
        None,
        "Scrambled eggs, bread",
        None,
        None,
        None,
        "Chicken salad, risotto",
        None,
        None,
        None,
        None,
        "Salmon with buckwheat",
        None,
        None,
        None,
        None,
    ],
}

df = pd.DataFrame(data)

results_list = []

for i in range(len(df)):
    if pd.notna(df.loc[i, "food"]):
        base = df.loc[i, "glucose_mg_dl"]
        food = df.loc[i, "food"]

        # 1. Print the food we are examining
        print(f"\n--- Examining: {food} (Index: {i}, Base: {base}) ---")

        future_slice = df.loc[i + 1 :]
        subsequent_meals = future_slice[future_slice["food"].notna()]

        if not subsequent_meals.empty:
            next_meal_idx = subsequent_meals.index[0]
            future = df.loc[i + 1 : next_meal_idx - 1]
        else:
            future = df.loc[i + 1 :]

        print("Future window:")
        print(future[["hour", "glucose_mg_dl"]])

        if not future.empty:
            m_val = future["glucose_mg_dl"].max()
            spike = m_val - base

            # Searching for return with tolerance
            target_limit = base + 5
            recovery_rows = future[future["glucose_mg_dl"] <= target_limit]

            print(f"Searching for limit <= {target_limit}. Found rows: {len(recovery_rows)}")

            if not recovery_rows.empty:
                recovery_row = recovery_rows.iloc[0]
                recovery_time = recovery_row["hour"]
                recovery_index = recovery_rows.index[0]
                duration = recovery_index - i
                print(
                    f"Return found! Time: {recovery_time}, Duration: {duration} hours."
                )
            else:
                recovery_time = "Did not return"
                duration = None
                print("Return not found -> duration = None")

            results_list.append({
                "Food": food,
                "Base": base,
                "Peak": m_val,
                "Spike": spike,
                "Duration": duration,
            })

core = pd.DataFrame(results_list)
print("\nFINAL TABLE:")
print(core)

# Making the plot
plt.plot(df['hour'], df['glucose_mg_dl'], marker='o', markersize=2, linestyle='-')
plt.xlabel('Time, h')
plt.ylabel('Glucose, mg/dl')
plt.xticks(rotation=45) 
plt.title('Glucose Fluctuations')
plt.minorticks_on()
plt.grid(True)

# Adjust limits as needed to fit your actual data bounds

plt.savefig('glucose_plot.png', dpi=300, bbox_inches='tight')
print("Plot saved as glucose_plot.png")
