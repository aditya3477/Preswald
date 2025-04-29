from preswald import connect, get_df, query, text, table, slider, plotly, alert, tabs
import plotly.express as px

alert.success("Dataset loaded successfully!")
alert.warning("This is a sample warning alert.")

if tab_choice == "Analysis":
    text("## Interactive Analysis")
    # your analysis code here
elif tab_choice == "Summary":
    text("## Dataset Summary")
    table(df.describe(), title="Summary Statistics")
else:
    text("## About This App")
    text("Created for Structured Labs coding assessment.")


# Initialize connection and load the dataset
connect()
df = get_df("Iris.csv")

# UI Heading
text("Iris Dataset Analysis")

# Interactive slider for dynamic filtering based on 'sepal_length'
threshold = slider("Sepal Length Threshold", min_val=float(df["SEPALLENGTHCM"].min()), 
                   max_val=float(df["SEPALLENGTHCM"].max()), default=5.0)

# Dynamic data filtering using the slider
filtered_df = df[df["SEPALLENGTHCM"] > threshold]

# Display filtered data table dynamically
table(filtered_df, title=f"Iris data with Sepal Length > {threshold}")

# SQL Query Example
sql = f"SELECT * FROM Iris WHERE SEPALWIDTHCM > 3.0"
sql_filtered_df = query(sql, "Iris")

# Display SQL-filtered data table
table(sql_filtered_df, title="Iris Data (SEPALWIDTHCM > 3.0) - SQL Query Result")

# Visualization with Plotly
fig = px.scatter(filtered_df, x="SEPALLENGTHCM", y="PETALLENGTHCM",
                 title="Sepal Length vs Petal Length")
plotly(fig)
