import os
import pandas as pd
import math

# Function to calculate velocity with the mm_per_arc_minute factor
def calculate_velocity(x1, y1, x2, y2, t1, t2):
    # Calculate the distance in pixels
    distance_x = x2 - x1
    distance_y = y2 - y1
    distance_mm = (distance_x**2 + distance_y**2) ** 0.5
    
    time_diff = (t2 - t1)/1000
    velocity = distance_mm / time_diff
    return velocity

# Function to process a single CSV file
def process_csv_file(csv_file):
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    # Drop rows with any empty cells in the required columns
    df = df.dropna(subset=['T', 'AVG_X', 'AVG_Y'])

    # Initialize variables
    saccade_duration=[]
    fixations = []
    saccades = []
    current_fixation = []
    current_saccade = []
    velocity_threshold = 500  # mm/s
    min_fixation_duration=150
    
    # Loop through the eye-tracking data
    for i in range(len(df) - 1):
        velocity = calculate_velocity(df['AVG_X'].iloc[i], df['AVG_Y'].iloc[i], df['AVG_X'].iloc[i+1], df['AVG_Y'].iloc[i+1], df['T'].iloc[i], df['T'].iloc[i+1])
        #print("velocity: ",velocity)
        duration = df['T'].iloc[i+1] - df['T'].iloc[i]
        
        if velocity < velocity_threshold :
            #print(velocity ,'TRUE')
            if current_saccade:
                if len(current_saccade)==1:
                   duration = df['T'].iloc[i] - df['T'].iloc[i-1]
 
                saccades.append(current_saccade)
                saccade_duration.append(duration)
                current_saccade = []
            current_fixation.append(df[['T', 'AVG_X', 'AVG_Y']].iloc[i].values)
        else:
            #print("FALSE at: ",i)
            if current_fixation:
                fixations.append(current_fixation)
                current_fixation = []
            current_saccade.append(df[['T', 'AVG_X', 'AVG_Y']].iloc[i].values)
    
    # Append the last fixation or saccade
    if current_fixation:
        fixations.append(current_fixation)
    if current_saccade:
        saccades.append(current_saccade)

    new_saccades = []
    for i in range(len(saccades)-1):  
        if saccade_duration[i] > min_fixation_duration:
            fixations.append(saccades[i])
        else:
            new_saccades.append(saccades[i])
    # Update the saccades list
    saccades = new_saccades
    

    # Extract features
    avg_fixation_durations = [fixation[-1][0] - fixation[0][0] for fixation in fixations]
    avg_saccade_durations = [saccade[-1][0] - saccade[0][0] for saccade in saccades]
    total_fixations = len(fixations)
    total_saccades = len(saccades)
    
    # Construct feature dictionary
    features = {
        'Total Time':df['T'].iloc[len(df)-1]-df['T'].iloc[0],
        'Average Fixation Duration': sum(avg_fixation_durations) / len(avg_fixation_durations) if avg_fixation_durations else 0,
        'Average Saccade Duration': sum(avg_saccade_durations) / len(avg_saccade_durations) if avg_saccade_durations else 0,
        'Total Fixations': total_fixations,
        'Total Saccades': total_saccades,
        'Saccades to Fixations Ratio': total_saccades/total_fixations
    }
    return features

# Function to extract gender and dyslexic status from file name
def extract_info_from_filename(filename):
    code = filename.split('.')[0][-1]
    if code in ['1', '3']:
        gender = 'male'
    else:
        gender = 'female'
    
    if code in ['1', '2']:
        dyslexic = 'yes'
    else:
        dyslexic = 'no'
    
    return gender, dyslexic

# Process all CSV files in the directory
directory_path = "D:/Grad Projroj/Recording Data/"
csv_files = [file for file in os.listdir(directory_path) if file.endswith(".csv")]
data = []

for file in csv_files:
    file_path = os.path.join(directory_path, file)
    features = process_csv_file(file_path)
    gender, dyslexic = extract_info_from_filename(file)
    features['Participant Code']=file.split('.')[0]
    features['Gender'] = gender
    features['Dyslexic'] = dyslexic
    data.append(features)

# Create DataFrame from the processed data
df_final = pd.DataFrame(data)

# Reorder columns to place 'Gender' first and 'Dyslexic' last
df_final = df_final[['Participant Code','Gender','Total Time',  'Average Fixation Duration', 'Average Saccade Duration', 'Total Fixations', 'Total Saccades','Saccades to Fixations Ratio', 'Dyslexic']]

# Save the final DataFrame to a CSV file
output_file = "D:/Grad Projroj/Eye_Tracking_Dataset.csv"
df_final.to_csv(output_file, index=False, header=[
    'Participant Code','Gender','Total_Time', 'Avg_Fix_Duration', 'Avg_Sacc_Duration', 'Total_Fix', 'Total_Sacc','Sacc_Fix_Ratio','Dyslexic'
])

# Print the final DataFrame to the console
print("Extracted features for all files:")
print(df_final)

