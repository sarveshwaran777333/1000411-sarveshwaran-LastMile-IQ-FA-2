import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🚚 LastMile IQ",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#0E1117"

def get_text_color(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)
    return "#000000" if brightness > 186 else "#FFFFFF"

def get_secondary_color(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)

    if brightness > 186:
        return "#F2F2F2"

    return "#1C1F26"

def get_active_tab_colors(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)

    if brightness > 186:
        return "#1C1F26", "#FFFFFF"

    return "#F2F2F2", "#000000"

def set_background(color):
    text_color = get_text_color(color)
    secondary_color = get_secondary_color(color)
    active_tab_color, active_tab_text = get_active_tab_colors(color)

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
            color: {text_color};
        }}

        .main {{
            background-color: {color};
        }}

        [data-testid="stSidebar"] {{
            background-color: {secondary_color};
        }}

        [data-testid="stSidebar"] * {{
            color: {text_color} !important;
        }}

        h1, h2, h3, h4, h5, h6,
        p, span, label {{
            color: {text_color} !important;
        }}

        .dashboard-title {{
            font-size: 42px;
            font-weight: 800;
            color: {text_color};
            margin-bottom: 0px;
        }}

        .dashboard-subtitle {{
            font-size: 16px;
            color: {text_color};
            opacity: 0.75;
            margin-bottom: 25px;
        }}

        .section-title {{
            font-size: 22px;
            font-weight: 700;
            color: {text_color};
            margin-top: 10px;
            margin-bottom: 8px;
        }}

        .kpi-card {{
            background-color: {secondary_color};
            border-radius: 14px;
            padding: 20px;
            min-height: 125px;
            border: 1px solid rgba(128,128,128,0.25);
        }}

        .kpi-title {{
            font-size: 14px;
            color: {text_color};
            opacity: 0.7;
            margin-bottom: 8px;
        }}

        .kpi-value {{
            font-size: 30px;
            font-weight: 800;
            color: {text_color};
        }}

        .info-card {{
            background-color: {secondary_color};
            border-radius: 14px;
            padding: 18px;
            border: 1px solid rgba(128,128,128,0.25);
            margin-bottom: 15px;
        }}

        .stButton > button {{
            border-radius: 8px;
            font-weight: 600;
            background-color: {secondary_color} !important;
            color: {text_color} !important;
            border: 1px solid rgba(128,128,128,0.35) !important;
        }}

        .stButton > button p,
        .stButton > button span {{
            color: {text_color} !important;
        }}

        .stButton > button:hover {{
            background-color: {active_tab_color} !important;
            color: {active_tab_text} !important;
            border-color: {active_tab_color} !important;
        }}

        .stButton > button:hover p,
        .stButton > button:hover span {{
            color: {active_tab_text} !important;
        }}

        [data-baseweb="tab-list"] {{
            display: flex !important;
            gap: 8px !important;
            border-bottom: none !important;
            padding: 4px !important;
        }}

        [data-baseweb="tab"] {{
            background-color: transparent !important;
            border-radius: 8px !important;
            padding: 10px 18px !important;
            border: 1px solid transparent !important;
            color: {text_color} !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }}

        [data-baseweb="tab"]:hover {{
            background-color: rgba(128,128,128,0.15) !important;
        }}

        [data-baseweb="tab"][aria-selected="true"] {{
            background-color: {active_tab_color} !important;
            color: {active_tab_text} !important;
            border: 1px solid {active_tab_color} !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
        }}

        [data-baseweb="tab"][aria-selected="true"] p,
        [data-baseweb="tab"][aria-selected="true"] span {{
            color: {active_tab_text} !important;
        }}

        [data-baseweb="tab-highlight"] {{
            background-color: transparent !important;
            height: 0px !important;
        }}

        [data-baseweb="tab-border"] {{
            background-color: transparent !important;
        }}

        [data-baseweb="select"] > div {{
            background-color: {secondary_color} !important;
            color: {text_color} !important;
        }}

        input, textarea {{
            background-color: {secondary_color} !important;
            color: {text_color} !important;
        }}

        [data-testid="stMetricValue"] {{
            color: {text_color} !important;
        }}

        [data-testid="stMetricLabel"] {{
            color: {text_color} !important;
        }}

        [data-testid="stDataFrame"] {{
            border-radius: 10px;
            overflow: hidden;
        }}

        .graph-help-button {{
            display: flex;
            justify-content: flex-end;
            align-items: center;
            height: 100%;
        }}

        div[data-testid="stPopover"] button {{
            width: 34px !important;
            height: 34px !important;
            min-height: 34px !important;
            padding: 0px !important;
            border-radius: 50% !important;
            font-size: 17px !important;
            font-weight: 800 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background(st.session_state.bg_color)

@st.cache_data
def load_data():
    df = pd.read_csv("Last mile Delivery Data.csv")

    df["Agent_Age"] = pd.to_numeric(
        df["Agent_Age"],
        errors="coerce"
    )

    df["Agent_Rating"] = pd.to_numeric(
        df["Agent_Rating"],
        errors="coerce"
    )

    df["Delivery_Time"] = pd.to_numeric(
        df["Delivery_Time"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "Delivery_Time",
            "Agent_Age"
        ]
    )

    if df["Agent_Rating"].isna().any():
        df["Agent_Rating"] = df["Agent_Rating"].fillna(
            df["Agent_Rating"].median()
        )

    df["Weather"] = df["Weather"].fillna("Unknown")
    df["Traffic"] = df["Traffic"].fillna("Unknown")
    df["Vehicle"] = df["Vehicle"].fillna("Unknown")
    df["Area"] = df["Area"].fillna("Unknown")
    df["Category"] = df["Category"].fillna("Unknown")

    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "The file 'Last mile Delivery Data.csv' was not found."
    )
    st.info(
        "Keep app.py and Last mile Delivery Data.csv in the same folder."
    )
    st.stop()
except Exception as e:
    st.error(
        f"Unable to load the dataset: {e}"
    )
    st.stop()

mean_delivery = df["Delivery_Time"].mean()
std_delivery = df["Delivery_Time"].std()
late_threshold = mean_delivery + std_delivery

df["Late_Delivery"] = (
    df["Delivery_Time"] > late_threshold
)

def create_age_group(age):
    if age < 25:
        return "<25"
    elif age <= 40:
        return "25–40"
    else:
        return "40+"

df["Age_Group"] = df["Agent_Age"].apply(
    create_age_group
)

with st.sidebar:
    st.markdown("## 🚚 LastMile IQ")
    st.markdown(
        "Delivery Analytics Dashboard"
    )

    st.divider()

    st.markdown("### Filters")

    weather_options = sorted(
        df["Weather"].dropna().unique()
    )

    traffic_options = sorted(
        df["Traffic"].dropna().unique()
    )

    vehicle_options = sorted(
        df["Vehicle"].dropna().unique()
    )

    category_options = sorted(
        df["Category"].dropna().unique()
    )

    area_options = sorted(
        df["Area"].dropna().unique()
    )

    selected_weather = st.multiselect(
        "Weather",
        weather_options,
        default=weather_options
    )

    selected_traffic = st.multiselect(
        "Traffic",
        traffic_options,
        default=traffic_options
    )

    selected_vehicle = st.multiselect(
        "Vehicle",
        vehicle_options,
        default=vehicle_options
    )

    selected_category = st.multiselect(
        "Category",
        category_options,
        default=category_options
    )

    selected_area = st.multiselect(
        "Area",
        area_options,
        default=area_options
    )

    st.divider()

    st.markdown(
        "### 🎨 Dashboard Appearance"
    )

    new_color = st.color_picker(
        "Pick a background colour",
        st.session_state.bg_color
    )

    if st.button(
        "Apply Background Color",
        use_container_width=True
    ):
        st.session_state.bg_color = new_color
        st.rerun()

    st.divider()

    st.caption("LastMile IQ")
    st.caption("FA-2 Data Analytics Project")

filtered_df = df[
    df["Weather"].isin(selected_weather)
    & df["Traffic"].isin(selected_traffic)
    & df["Vehicle"].isin(selected_vehicle)
    & df["Category"].isin(selected_category)
    & df["Area"].isin(selected_area)
].copy()

text_color = get_text_color(
    st.session_state.bg_color
)

secondary_color = get_secondary_color(
    st.session_state.bg_color
)

st.markdown(
    '<div class="dashboard-title">🚚 LastMile IQ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">Smart Last-Mile Delivery Analytics Dashboard</div>',
    unsafe_allow_html=True
)

if filtered_df.empty:
    st.warning(
        "No deliveries match the selected filters."
    )
    st.stop()

total_deliveries = len(filtered_df)

average_delivery = filtered_df[
    "Delivery_Time"
].mean()

late_deliveries = filtered_df[
    "Late_Delivery"
].sum()

late_rate = (
    late_deliveries /
    total_deliveries
) * 100

average_rating = filtered_df[
    "Agent_Rating"
].mean()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">
                TOTAL DELIVERIES
            </div>
            <div class="kpi-value">
                {total_deliveries:,}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">
                AVERAGE DELIVERY TIME
            </div>
            <div class="kpi-value">
                {average_delivery:.1f} min
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">
                LATE DELIVERY RATE
            </div>
            <div class="kpi-value">
                {late_rate:.1f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">
                AVERAGE AGENT RATING
            </div>
            <div class="kpi-value">
                {average_rating:.2f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

tab_dashboard, tab_analysis, tab_data = st.tabs(
    [
        "📊 Interactive Dashboard",
        "📐 Mathematical Analysis",
        "📋 Raw Dataset"
    ]
)

def style_plot(fig):
    fig.update_layout(
        paper_bgcolor=secondary_color,
        plot_bgcolor=secondary_color,
        font=dict(
            color=text_color,
            size=12
        ),
        title_font=dict(
            color=text_color,
            size=18
        ),
        margin=dict(
            l=60,
            r=30,
            t=60,
            b=50
        ),
        legend=dict(
            font=dict(
                color=text_color
            )
        )
    )

    fig.update_xaxes(
        title_font=dict(
            color=text_color
        ),
        tickfont=dict(
            color=text_color
        ),
        gridcolor="rgba(128,128,128,0.2)",
        zerolinecolor="rgba(128,128,128,0.2)"
    )

    fig.update_yaxes(
        title_font=dict(
            color=text_color
        ),
        tickfont=dict(
            color=text_color
        ),
        gridcolor="rgba(128,128,128,0.2)",
        zerolinecolor="rgba(128,128,128,0.2)"
    )

    return fig

def graph_header(title, explanation):
    title_col, help_col = st.columns(
        [12, 1],
        vertical_alignment="center"
    )

    with title_col:
        st.markdown(
            f'<div class="section-title">{title}</div>',
            unsafe_allow_html=True
        )

    with help_col:
        st.markdown(
            '<div class="graph-help-button">',
            unsafe_allow_html=True
        )

        with st.popover("?"):
            st.markdown(
                "### What does this graph show?"
            )
            st.write(explanation)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

with tab_dashboard:

    graph_header(
        "01 · Delay Analyzer",
        "This graph shows the average Delivery Time under different Weather and Traffic conditions. Compare the bars to identify which combinations are associated with longer or shorter delivery times."
    )

    delay_data = (
        filtered_df
        .groupby(
            ["Weather", "Traffic"],
            as_index=False
        )["Delivery_Time"]
        .mean()
    )

    fig_delay = px.bar(
        delay_data,
        x="Weather",
        y="Delivery_Time",
        color="Traffic",
        barmode="group",
        title="Average Delivery Time by Weather and Traffic",
        labels={
            "Delivery_Time":
                "Average Delivery Time (minutes)",
            "Weather":
                "Weather",
            "Traffic":
                "Traffic"
        }
    )

    fig_delay = style_plot(
        fig_delay
    )

    st.plotly_chart(
        fig_delay,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        graph_header(
            "02 · Vehicle Comparison",
            "This graph compares the average Delivery Time for each Vehicle type. A taller bar means that deliveries using that vehicle type take longer on average."
        )

        vehicle_data = (
            filtered_df
            .groupby(
                "Vehicle",
                as_index=False
            )["Delivery_Time"]
            .mean()
            .sort_values(
                "Delivery_Time"
            )
        )

        fig_vehicle = px.bar(
            vehicle_data,
            x="Vehicle",
            y="Delivery_Time",
            title="Average Delivery Time by Vehicle",
            labels={
                "Delivery_Time":
                    "Average Delivery Time (minutes)",
                "Vehicle":
                    "Vehicle"
            }
        )

        fig_vehicle = style_plot(
            fig_vehicle
        )

        st.plotly_chart(
            fig_vehicle,
            use_container_width=True
        )

    with col2:

        graph_header(
            "03 · Agent Performance",
            "This scatter plot shows the relationship between Agent Age and Delivery Time. Each dot represents a delivery. The colours show three age groups: below 25, 25–40, and above 40."
        )

        fig_agent = px.scatter(
            filtered_df,
            x="Agent_Age",
            y="Delivery_Time",
            color="Age_Group",
            title="Agent Age vs Delivery Time",
            labels={
                "Agent_Age":
                    "Agent Age",
                "Delivery_Time":
                    "Delivery Time (minutes)",
                "Age_Group":
                    "Age Group"
            },
            hover_data=[
                "Agent_Rating",
                "Vehicle",
                "Traffic",
                "Area"
            ]
        )

        fig_agent = style_plot(
            fig_agent
        )

        st.plotly_chart(
            fig_agent,
            use_container_width=True
        )

    graph_header(
        "04 · Area Heatmap",
        "This heatmap shows the average Delivery Time for different Areas under different Traffic conditions. Each cell represents an average delivery time, making it easier to compare areas and traffic conditions."
    )

    area_heatmap_data = (
        filtered_df
        .groupby(
            ["Area", "Traffic"]
        )["Delivery_Time"]
        .mean()
        .reset_index()
    )

    area_pivot = area_heatmap_data.pivot(
        index="Traffic",
        columns="Area",
        values="Delivery_Time"
    )

    fig_area = px.imshow(
        area_pivot,
        title="Average Delivery Time Across Areas",
        labels={
            "x": "Area",
            "y": "Traffic",
            "color":
                "Average Delivery Time"
        },
        aspect="auto"
    )

    fig_area = style_plot(
        fig_area
    )

    st.plotly_chart(
        fig_area,
        use_container_width=True
    )

    graph_header(
        "05 · Category Visualizer",
        "This horizontal boxplot shows the distribution of Delivery Time for each Category. The line inside each box represents the median. The box shows the middle part of the data, while the whiskers show the wider spread of delivery times."
    )

    category_order = (
        filtered_df
        .groupby(
            "Category"
        )["Delivery_Time"]
        .median()
        .sort_values()
        .index
        .tolist()
    )

    fig_category = px.box(
        filtered_df,
        x="Delivery_Time",
        y="Category",
        category_orders={
            "Category":
                category_order
        },
        title="Delivery Time Distribution Across Categories",
        labels={
            "Delivery_Time":
                "Delivery Time (minutes)",
            "Category":
                "Category"
        },
        points=False,
        orientation="h"
    )

    fig_category = style_plot(
        fig_category
    )

    fig_category.update_layout(
        height=max(
            650,
            len(category_order) * 45
        ),
        margin=dict(
            l=120,
            r=30,
            t=60,
            b=60
        )
    )

    fig_category.update_yaxes(
        categoryorder="array",
        categoryarray=category_order,
        automargin=True,
        title="Category"
    )

    fig_category.update_xaxes(
        title="Delivery Time (minutes)"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

with tab_analysis:

    st.markdown(
        '<div class="section-title">Mathematical Analysis</div>',
        unsafe_allow_html=True
    )

    analysis_col1, analysis_col2 = st.columns(2)

    with analysis_col1:

        st.markdown(
            f"""
            <div class="info-card">
                <b>Mean Delivery Time</b><br>
                {mean_delivery:.2f} minutes
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="info-card">
                <b>Standard Deviation</b><br>
                {std_delivery:.2f} minutes
            </div>
            """,
            unsafe_allow_html=True
        )

    with analysis_col2:

        st.markdown(
            f"""
            <div class="info-card">
                <b>Late Delivery Threshold</b><br>
                {late_threshold:.2f} minutes
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="info-card">
                <b>Late Deliveries</b><br>
                {int(df["Late_Delivery"].sum()):,} deliveries
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "### Late Delivery Rule"
    )

    st.latex(
        r"\text{Late Delivery if Delivery Time} > \bar{x} + \sigma"
    )

    st.write(
        f"Mean Delivery Time = {mean_delivery:.2f} minutes"
    )

    st.write(
        f"Standard Deviation = {std_delivery:.2f} minutes"
    )

    st.write(
        f"Late Delivery Threshold = "
        f"{mean_delivery:.2f} + "
        f"{std_delivery:.2f} = "
        f"{late_threshold:.2f} minutes"
    )

    st.markdown(
        "### Filtered Dataset Statistics"
    )

    statistics = pd.DataFrame(
        {
            "Metric": [
                "Deliveries",
                "Average Delivery Time",
                "Minimum Delivery Time",
                "Maximum Delivery Time",
                "Standard Deviation",
                "Average Agent Age",
                "Average Agent Rating"
            ],
            "Value": [
                len(filtered_df),
                round(
                    filtered_df[
                        "Delivery_Time"
                    ].mean(),
                    2
                ),
                round(
                    filtered_df[
                        "Delivery_Time"
                    ].min(),
                    2
                ),
                round(
                    filtered_df[
                        "Delivery_Time"
                    ].max(),
                    2
                ),
                round(
                    filtered_df[
                        "Delivery_Time"
                    ].std(),
                    2
                ),
                round(
                    filtered_df[
                        "Agent_Age"
                    ].mean(),
                    2
                ),
                round(
                    filtered_df[
                        "Agent_Rating"
                    ].mean(),
                    2
                )
            ]
        }
    )

    st.dataframe(
        statistics,
        use_container_width=True,
        hide_index=True
    )

with tab_data:

    st.markdown(
        '<div class="section-title">Raw Dataset</div>',
        unsafe_allow_html=True
    )

    st.write(
        f"Showing {len(filtered_df):,} filtered records."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=600
    )

st.divider()

st.caption(
    "LastMile IQ · FA-2 Data Analytics Dashboard · "
    "Built with Python, Pandas, Plotly and Streamlit"
)
