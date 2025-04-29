from preswald import connect, get_df, query, text, table, slider, plotly, alert, tabs
import plotly.express as px

# Initialize connection and load the dataset
connect()
df = get_df("Iris")

# Alerts after successful data loading
alert.success("Dataset loaded successfully!")
alert.warning("Make sure to explore different tabs!")

# Tabs for navigation
tab_choice = tabs(["Analysis", "Summary", "About"])

if tab_choice == "Analysis":
    text("Interactive Iris Analysis")

    # Interactive slider for dynamic filtering based on 'SepalLengthCm'
    threshold = slider(
        "Sepal Length Threshold (cm)",
        min_val=float(df["SEPALLENGTHCM"].min()), 
        max_val=float(df["SEPALLENGTHCM"].max()),
        default=5.0
    )

    # Dynamic data filtering using slider
    filtered_df = df[df["SEPALLENGTHCM"] > threshold]

    # Display filtered data table dynamically
    table(filtered_df, title=f"Iris Data (SEPALLENGTHCM > {threshold} cm)")

    # Visualization with Plotly (scatter plot)
    fig = px.scatter(
        filtered_df,
        x="SEPALLENGTHCM",
        y="PETALLENGTHCM",
        color="SPECIES",
        title="Sepal Length vs Petal Length (Filtered Data)"
    )
    plotly(fig)

elif tab_choice == "Summary":
    text("Dataset Summary")
    table(df.describe(), title="Summary Statistics of Iris Data")

else:
    text("About This App")
    text("This app is created for the Structured Labs coding assessment.\n\n"
         "**Dataset:** Iris flower measurements\n\n"
         "**Features:** Interactive filtering, visualization, SQL queries, and data exploration.")

# Example SQL Query and Table (always shown)
sql = "SELECT * FROM Iris WHERE SepalWidthCm > 3.0"
sql_filtered_df = query(sql, "Iris")
table(sql_filtered_df, title="SQL Query: Iris Data (Sepal Width > 3.0 cm)")

