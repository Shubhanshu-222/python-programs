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
    "CT1 (30)": [
        18, 19, 19, 0, 19, 17, 17, 22, 21, 22, 18, 24, 19, 16, 22, 20, 
        17, 22, 25, 23, 22, 18, 26, 23, 19, 22, 17, 16, 14, 25, 17, 22, 18, 
        16, 19, 17, 17, 20, 0, 23, 17, 26, 20, 16, 19, 20, 22, 20, 11, 19, 
        28, 20, 27, 24, 15, 25, 22, 26, 16, 18, 23, 15, 21, 18, 22, 16, 20, 24, 19
    ],
    "MST (40)": [
        26, 25, 34, 17, 22, 19, 17, 20, 19, 33, 25, 14, 10, 25, 20, 21, 10, 
        17, 31, 22, 27, 26, 36, 24, 30, 24, 17, 21, 10, 30, 21, 21, 21, 25, 
        25, 32, 21, 15, 21, 29, 18, 31, 26, 21, 21, 12, 27, 18, 16, 27, 35, 27, 
        33, 24, 25, 31, 34, 24, 26, 27, 27, 17, 28, 26, 26, 20, 33, 24, 33, 31
    ],
    "CT2 (30)": [
        15, 17, 16, 19, 10, 13, 11, 6, 17, 20, 16, 13, 14, 19, 16, 14, 12, 
        14, 17, 15, 15, 11, 23, 19, 17, 20, 0, 14, 10, 15, 8, 15, 12, 16, 
        13, 15, 13, 15, 13, 26, 13, 20, 13, 12, 11, 10, 0, 18, 8, 14, 20, 16, 
        19, 14, 12, 18, 15, 14, 13, 16, 9, 13, 17, 16, 13, 22, 15, 16, 16, 14
    ],
    "ESE (100)": [
        72, 85, 79, 71, 54, 51, 37, 62, 80, 77, 64, 70, 62, 72, 46, 69, 24, 
        77, 66, 71, 56, 63, 84, 72, 84, 87, 58, 78, 28, 91, 46, 71, 66, 62, 
        68, 84, 61, 49, 68, 82, 41, 80, 84, 35, 70, 0, 0, 41, 48, 59, 82, 47, 
        85, 71, 70, 73, 67, 72, 65, 64, 65, 57, 85, 92, 73, 51, 72, 64, 88, 79
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
    ct_out_of_20 = (max(row["CT1 (30)"], row["CT2 (30)"]) / 30) * 20
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


