import pandas as pd

# Set the option to display all columns and rows
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # No line truncation

# Full data dictionary
data = {
    "Candidate Name": [
        "ABHANG HARSH MOHAN", "BALAPURWALA TAHA MURTUZA", "BANSOD SHUBHANSHU SHARAD", 
        "BHANPURAWALA HUSSAIN FIROZ", "BHISE PRATHMESH SHASHIKANT", "CHIDRAWAR SHYAM GAJANAN", 
        "CHOPDEKAR CHINTAN VIRENDRA", "CHOUGALE ADESH GANGARAM", "CHOUGULE VAIJANATH MAHADEV", 
        "DWIVEDI SAGAR RAMLAL", "GADGE ATHARVA SUNIL MADHURI", "GARJE MANOJ KERABA", 
        "GARUD SHEKHAR DNYANESHWAR", "GHUTAKE SHREYASH RAJESH", "IGAVE ROHAN AMAR", 
        "KALAMBE PRANAV SANDEEP", "KATARE SARVESH SIDDHARTH", "KHANDELWAL UTKARSH RAJESH", 
        "LANJULKAR OM BHANUDAS", "LIMKAR YASHRAJ BHAVESH", "MADRI ANIRUDH SHREEKESH", 
        "MAHAJAN HARSH SURESH", "MANDAVKAR SHUBHAM SHANKAR", "MANSOORI NEYAZ REYAZ", 
        "MISHRA ANIKET VIJAY", "PAI KUSH MITHIL", "PAKHARE PRATIK MOHAN", 
        "PANDERE HARSH MAHESH", "PARDHI ADITYA RAJU", "PATHAK VARAD PRASHANT", 
        "PAWAR BHUPENDRASING PUNDLIK", "RATHOD ADITYA SATISH", "RAUT SARVADNYA DIGAMBAR", 
        "ROHEKAR SARTHAK RAJENDRA", "SARODE CHUNAY MURLIDHAR", "SAWANT KUNAL DATTARAM", 
        "SAWANT SHANTANU SUCHIT", "SHAIKH ARBAZ RAHIMAN", "SHIKALGAR MOHAMMADSAAD NASIM", 
        "SINGH SHUBHAM BRAHAMJEET", "TANDEL SHUBHAM DEVIDAS", "TAURO JASON EDWARD", 
        "TIWARI PARTHESH ASHWIN", "TIWARI SUMIT MURLIDHAR", "TORANGI SHRINATH BASAVRAJ", 
        "VEJARE YASH JITENDRA", "VISAVE PRANIT PRAKASH", "YADAV JAGANNATH RAMAWADH", 
        "ZORE SHAILESH JAGANNATH", "KHAIRNAR YUKTA SAHEBRAO", "CHAREGAONKAR SHRADDHA SUBHASH", 
        "DWIVEDI PRACHI PRASHANT", "GAWANDE ANUSHKA NARENDRA", "GUPTA NANDINI SANJAY", 
        "HARCHEKAR MANSI MANDAR", "JUMDE PRADNYA SUSHIL", "KHARE TANVI TUSHAR", 
        "MENGAJI SEJAL MOHAN", "RAINA UDITI SURAJ", "SAKE SHWETA RAJENDRA", 
        "SARODE ANURADHA ASHOK", "SHINDE PRITI DATTATRAYA", "SIDDIQUI ATIBA ATHARUDDIN", 
        "SINGH TANYA RAJESH", "SURYAWANSHI JYOTSNA SHANTARAM", "TAMBVE RIA JAYANT", 
        "THAKRE ANUSHRI MOHAN", "TRIKARWAR NAYANSI RAMESH", "VIRA ZEAL NILESH", 
        "BHAGAT BHARGAVI PRAVIN"
    ],
    "CT1 (20)": [
    17, 16, 17, 16, 16, 15, 16, 18, 19, 15, 13, 14, 13, 12, 14, 19, 12, 15, 13, 16, 
    0, 16, 16, 14, 17, 15, 13, 16, 10, 12, 11, 13, 15, 17, 16, 14, 16, 18, 16, 17, 
    15, 14, 17, 18, 17, 11, 0, 15, 8, 19, 17, 15, 13, 16, 17, 17, 15, 16, 14, 15, 
    14, 15, 15, 17, 14, 17, 16, 14, 11, 16
    ],
    "MST (40)": [
    27, 30, 34, 28, 27, 24, 18, 26, 35, 19, 24, 24, 22, 22, 22, 25, 26, 34, 18, 29, 23, 28, 21, 31, 
    26, 32, 31, 27, 21, 34, 23, 21, 19, 22, 30, 35, 28, 23, 31, 29, 18, 30, 30, 23, 32, 16, 29, 17, 
    14, 21, 32, 35, 18, 30.5, 23, 27, 28, 28, 29, 29, 25, 26, 30, 35, 29, 18, 27, 21, 36, 36
    ],
    "ESE (100)": [
    51.5, 61, 68, 51, 47.5, 56.5, 47.5, 44, 75.5, 63, 49.5, 52.5, 46.5, 63.5, 71, 46, 42.5, 77, 
    63, 58.5, 60, 61, 62.5, 74.5, 69.5, 80, 51.5, 64.5, 55, 81, 38, 57, 58, 58, 59.5, 61, 44.5, 55, 65.5, 
    69.5, 40.5, 48, 72, 53.5, 58, 0, 0, 40, 51, 44.5, 58.5, 54.5, 61, 65.5, 68, 62, 58, 83, 62, 60.5, 
    52.5, 44.5, 63, 77, 64.5, 62.5, 61.5, 62.5, 53, 56
    ]
}

# Check lengths of all columns
max_length = max(len(col) for col in data.values())

# Pad shorter columns with 0 to match the max length
for key in data:
    if len(data[key]) < max_length:
        data[key].extend([0] * (max_length - len(data[key])))

# Create DataFrame
df = pd.DataFrame(data)

# Function to calculate total marks
def calculate_marks(row):
    mst_out_of_30 = (row["MST (40)"] / 40) * 30
    ese_out_of_50 = (row["ESE (100)"] / 100) * 50
    ct_out_of_20 = (row["CT1 (20)"] / 20) * 20
    return mst_out_of_30 + ese_out_of_50 + ct_out_of_20

# Add a new column for total marks
df["Total Marks (100)"] = df.apply(calculate_marks, axis=1)

# Print the resulting DataFrame
print(df)

# Extract candidate names and their total marks
final_results = df[["Candidate Name", "Total Marks (100)"]]

# Sort the results in descending order of total marks
sorted_results = final_results.sort_values(by="Total Marks (100)", ascending=False)

# Add a serial number column
sorted_results.insert(0, "Sr. No.", range(1, len(sorted_results) + 1))

# Print the sorted results with serial numbers
print(sorted_results)


