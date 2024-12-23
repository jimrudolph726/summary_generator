import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
from maps import *
import urllib.parse

def create_boxplot(df, column, title, parameter):
    """Generate a vertical boxplot for the given DataFrame and column with parameter in the title."""
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[column].dropna(), patch_artist=True)  # Default is vertical boxplot
    plt.title(f"{title} - {parameter}")  # Include parameter in title
    plt.ylabel(column)  # Set y-axis label
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return buffer

def main():
    station_list = []
    parameters_url = []
    st.title("Data Summary Generator")

    # Dropdown for station selection
    st.write("### Select a Station:")
    station = st.selectbox("", options=list(station_map.keys()))
    station_number = station_map[station]
    if station_number not in station_list:
        station_list.append(station_number)

    # Dropdown for second station selection
    st.write("### Select a Second Station:")
    station2 = st.selectbox(" ", options=list(station_map.keys()))
    station_number2 = station_map[station2]
    if station_number2 not in station_list:
        station_list.append(station_number2)

    st.write("### Select a Parameter:")
    parameter = st.selectbox("Parameter", options=list(parameter_map.keys()))
    parameter_url = parameter_map[parameter]

    # parameters_urls = parameters_urls.append(parameter_url)
    # parameters_urls = ','.join([p for p in parameters_urls if p])

    # Calendar widget for selecting start and end dates
    st.write("### Select a Start Date and End Date:")
    start_date = st.date_input("Start Date", key="start_date")
    end_date = st.date_input("End Date", key="end_date")
    start_date_formatted = datetime.datetime.strptime(str(start_date), "%Y-%m-%d").strftime("%Y-%m-%d")
    end_date_formatted = datetime.datetime.strptime(str(end_date), "%Y-%m-%d").strftime("%Y-%m-%d")
    
    # URL-encode the date strings
    start_date_encoded = urllib.parse.quote(start_date_formatted)
    end_date_encoded = urllib.parse.quote(end_date_formatted)

    # Determine measuring program based on station type
    measuring_program = "lake" if "Lake" in station else "storm"

    # Initialize DataFrames
    df1 = None
    df2 = None

    if st.button("Submit"):
        # Validate the selected dates
        if start_date > end_date:
            st.error("The start date cannot be after the end date. Please select valid dates.")
        else:
            try:
                # Generate URLs for the first and second stations
                url1 = (
                    f"https://waterdata.capitolregionwd.org/KiWIS/KiWIS?datasource=0&service=kisters"
                    f"&type=queryServices&request=getWqmSampleValues&station_no={station_number}"
                    f"&parametertype_name={parameter_url}&measuringprog_name={measuring_program}"
                    f"&from={start_date_encoded}&to={end_date_encoded}"
                    f"&returnfields=measuringprog_name,parametertype_name,station_name,timestamp,"
                    f"sample_timestamp,value,value_sign,value_quality,value_remark,unit_name,"
                    f"unit_symbol,method_name,sample_depth&format=csv&dateformat=yyyy-MM-dd%20HH:mm:ss"
                    f"&csvdiv=,&maxquality=120&orderby=timestamp"
                )

                url2 = (
                    f"https://waterdata.capitolregionwd.org/KiWIS/KiWIS?datasource=0&service=kisters"
                    f"&type=queryServices&request=getWqmSampleValues&station_no={station_number2}"
                    f"&parametertype_name={parameter_url}&measuringprog_name={measuring_program}"
                    f"&from={start_date_encoded}&to={end_date_encoded}"
                    f"&returnfields=measuringprog_name,parametertype_name,station_name,timestamp,"
                    f"sample_timestamp,value,value_sign,value_quality,value_remark,unit_name,"
                    f"unit_symbol,method_name,sample_depth&format=csv&dateformat=yyyy-MM-dd%20HH:mm:ss"
                    f"&csvdiv=,&maxquality=120&orderby=timestamp"
                )

                # Fetch and store data for the first and second stations
                df1 = pd.read_csv(url1)
                df2 = pd.read_csv(url2)
                st.success(f"Report generated successfully for {station} and {station2}!")

                # Create boxplots for the "value" column, with the parameter in the title
                plot1 = create_boxplot(df1, "value", f"Boxplot for {station}", parameter)
                plot2 = create_boxplot(df2, "value", f"Boxplot for {station2}", parameter)

                # Create an Excel file with the data and boxplots
                output = BytesIO()
                with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                    # Writing dataframes to Excel
                    df1.to_excel(writer, index=False, sheet_name=station)
                    df2.to_excel(writer, index=False, sheet_name=station2)

                    # Creating a new sheet for Boxplots
                    workbook = writer.book
                    boxplot_sheet = workbook.add_worksheet("Boxplots")

                    # Insert the boxplots into the "Boxplots" sheet
                    boxplot_sheet.insert_image("A1", f"Boxplot for {station} - {parameter}.png", {"image_data": plot1})
                    boxplot_sheet.insert_image("A30", f"Boxplot for {station2} - {parameter}.png", {"image_data": plot2})

                output.seek(0)

                # Provide download button for the Excel file
                st.download_button(
                    label="Download Excel File with Boxplots",
                    data=output,
                    file_name="data_with_boxplots.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            except Exception as e:
                st.error(f"An error occurred while processing the data: {e}")

if __name__ == "__main__":
    main()
