import pandas as pd

print("SALES.CSV\n")
df = pd.read_csv("1_sales.csv")
print(df)
print("\nREAD FIRST VALUE FROM THE DATA RETRIEVED FROM FILE")
print(df.head(1))

print("\nSALES_OUTPUT.CSV")
df.to_csv("1_Sales_output.csv", index=False)
df_out = pd.read_csv("1_Sales_output.csv")
print(df_out)

print("\nSTUDENT_SCORE.XLSX")
# If sheet_name not given, then prints all sheets of the Excel file
read_excel = pd.read_excel("1_StudentsScore.xlsx", sheet_name="data")
print("\nHEAD -->STUDENT_SCORE.XLSX")
print(read_excel.head())
print("\nHEAD 15 -->STUDENT_SCORE.XLSX")
print(read_excel.head(15))
print("\nSTUDENT_SCORE.XLSX")
print(read_excel)

print("\nSTUDENT_SCORE_OUTPUT.XLSX")
read_excel.to_excel("1_StudentsScore_output.xlsx", sheet_name="myData")
read_excel_out = pd.read_excel("1_StudentsScore_output.xlsx", sheet_name="myData")
print(read_excel_out)

