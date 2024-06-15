import os
import pandas as pd

# Function to calculate the dispersion
def calculate_dispersion(gaze_points):
    x_coords = [point[1] for point in gaze_points]
    y_coords = [point[2] for point in gaze_points]
    dispersion = (max(x_coords) - min(x_coords)) + (max(y_coords) - min(y_coords))
    return dispersion

# Function to process a single CSV file
def process_csv_file(csv_file):

    dispersion_threshold=(33/300)*25.4
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    # Drop rows with any empty cells in the required columns
    df = df.dropna(subset=['T', 'AVG_X', 'AVG_Y'])

    # Initialize variables
    fixations = []
    saccades = []
    i = 0
    while i < len(df):
        current_fixation = [df[['T', 'AVG_X', 'AVG_Y']].iloc[i].values.tolist()]
        j = i + 1
        while j < len(df):
            candidate_fixation = current_fixation + [df[['T', 'AVG_X', 'AVG_Y']].iloc[j].values.tolist()]
            dispersion = calculate_dispersion(candidate_fixation)
            if dispersion <= dispersion_threshold:
                current_fixation = candidate_fixation
                j += 1
            else:
                break
        fixations.append(current_fixation)
        i = j

    # Calculate saccades as the intervals between fixations
    for k in range(1, len(fixations)):
        saccade = [fixations[k-1][-1], fixations[k][0]]
        saccades.append(saccade)

    # Extract features
    
    avg_fixation_durations = [fixation[-1][0] - fixation[0][0] for fixation in fixations]
    avg_saccade_durations = [saccade[1][0] - saccade[0][0] for saccade in saccades]
    total_fixations = len(fixations)
    total_saccades = len(saccades)
    

    # Construct feature dictionary
    features = {
        
        'Average Fixation Duration': sum(avg_fixation_durations) / len(avg_fixation_durations) if avg_fixation_durations else 0,
        'Average Saccade Duration': sum(avg_saccade_durations) / len(avg_saccade_durations) if avg_saccade_durations else 0,
        'Total Fixations': total_fixations,
        'Total Saccades': total_saccades,
        
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
    features['Gender'] = gender
    features['Dyslexic'] = dyslexic
    data.append(features)

# Create DataFrame from the processed data
df_final = pd.DataFrame(data)

# Reorder columns to place 'Gender' first and 'Dyslexic' last
df_final = df_final[['Gender', 'Average Fixation Duration', 'Average Saccade Duration', 'Total Fixations', 'Total Saccades', 'Dyslexic']]

# Save the final DataFrame to a CSV file
output_file = "D:/Grad Projroj/Eye_Tracking_Dataset.csv"
df_final.to_csv(output_file, index=False, header=[
    'Gender', 'Avg_Fix_Duration', 'Avg_Sacc_Duration', 'Total_Fix', 'Total_Sacc',  'Dyslexic'
])

# Print the final DataFrame to the console
print("Extracted features for all files:")
print(df_final)
