from preswald import connect, get_df
connect()
df = get_df("my_dataset")

# Initalizing the UI COMPONENTS
from preswald import sidebar, selectbox, checkbox, text_input, slider, text, table, plotly, alert
import plotly.express as px

sidebar(defaultopen=True)

# 1. Selectbox for item selection
item_list = df["Item"].unique().tolist()
selected_item = selectbox("Select an Item", options=item_list, default=item_list[0])

# 2. Checkbox to show all data or just filtered
show_all = checkbox("Show all items (ignores filters)", default=False)

# 3. Text input to search item name
search_term = text_input("Search item name", placeholder="e.g., Item A")

# 4. Sliders for price and quantity thresholds
price_threshold = slider("Min Price", min_val=0, max_val=200, default=50)
quantity_threshold = slider("Min Quantity", min_val=0, max_val=20, default=5)

# --- FILTERING LOGIC ---
if show_all:
    filtered_df = df
else:
    filtered_df = df[
        (df["Price"] >= price_threshold) &
        (df["Quantity"] >= quantity_threshold) &
        (df["Item"].str.contains(search_term, case=False)) &
        (df["Item"] == selected_item)
    ]

# --- MAIN DISPLAY ---
text("# 📊 Item Dashboard")

if filtered_df.empty:
    alert("No items match the selected criteria.", level="warning")
else:
    table(filtered_df, title="Filtered Items")

    # Scatter plot of all data for context
    fig = px.scatter(
        df,
        x="Quantity",
        y="Price",
        text="Item",
        title="Quantity vs. Price",
        labels={"Quantity": "Quantity", "Price": "Price"}
    )
    fig.update_traces(textposition='top center')
    plotly(fig)
