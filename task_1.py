import pandas as pd

df = pd.read_csv('Medical_appointment.csv')
print(df.head())

#identifying and handling the missing values
df.fillna({
    col: df[col].mean() if df[col].dtype in ['float64', 'int64'] else 'Unknown'
    for col in df.columns
}, inplace=True)

#remove duplicates 
df.drop_duplicates(inplace=True)

#Standardize text values
# Gender column: lowercase and map to full names
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.lower().replace({
        'f': 'female',
        'm': 'male'
    })
# Neighbourhood: title case
if 'Neighbourhood' in df.columns:
    df['Neighbourhood'] = df['Neighbourhood'].str.strip().str.title()

# Convert date formats to dd-mm-yyyy
date_columns = ['ScheduledDay', 'AppointmentDay']
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%d-%m-%Y')

#Rename column headers: lowercase, no spaces
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

#Fix Data Types
# Convert 'age' to integer
if 'age' or 'scholarship' or 'hipertension' or 'diabetes' or 'alcoholism' or 'handcap' or 'sms_received' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)
# Convert date columns back to datetime for further analysis
for col in ['scheduledday', 'appointmentday']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format='%d-%m-%Y', errors='coerce')

#Save the cleaned data to a new CSV
df.to_csv('cleaned_medical_appointment.csv', index=False)

print("Data cleaning complete. Saved as 'cleaned_medical_appointment.csv'")


# print(dir(pd))