import os
import pandas as pd
import math

# Given values
viewing_distance_mm = 450  # in millimeters (45 cm)
minutes_of_arc = 5

# Convert minutes of arc to radians
theta = (math.pi / 180) * (minutes_of_arc / 60)

# Calculate the corresponding physical size on the screen
mm_per_arc_minute = viewing_distance_mm * theta

# Function to calculate velocity with the mm_per_arc_minute factor
def calculate_velocity(x1, y1, x2, y2, t1, t2, mm_per_arc_minute):
    # Calculate the distance in pixels
    pixel_distance_x = x2 - x1
    pixel_distance_y = y2 - y1
    distance_px = (pixel_distance_x**2 + pixel_distance_y**2) ** 0.5
    
    # Convert pixel distance to millimeters using the arc minute resolution
    distance_mm = distance_px * mm_per_arc_minute
    time_diff = (t2 - t1)/1000
    velocity = distance_mm / time_diff
    return velocity

# Function to process a single CSV file
def process_csv_file(csv_file):
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    # Drop rows with any empty cells in the required columns
    df = df.dropna(subset=['T', 'AVG_X', 'AVG_Y'])

    # Print the first 10 values of T, AVG_X, and AVG_Y
    print("First 10 values of T, AVG_X, and AVG_Y:")
    print(df[['T', 'AVG_X', 'AVG_Y']].head(10))

    # Initialize variables
    fixations = []
    saccades = []
    current_fixation = []
    current_saccade = []
    velocity_threshold = 500  # mm/s
    duration_threshold = 50  # milliseconds
    
    # Loop through the eye-tracking data
    for i in range(len(df) - 1):
        velocity = calculate_velocity(df['AVG_X'].iloc[i], df['AVG_Y'].iloc[i], df['AVG_X'].iloc[i+1], df['AVG_Y'].iloc[i+1], df['T'].iloc[i], df['T'].iloc[i+1], mm_per_arc_minute)
        print("velocity: ",velocity)
        
        if velocity < velocity_threshold :
            print("TRUE at: ",i)
            if current_saccade:
                saccades.append(current_saccade)
                current_saccade = []
            current_fixation.append(df[['T', 'AVG_X', 'AVG_Y']].iloc[i].values)
        else:
            print("FALSE at: ",i)
            if current_fixation:
                fixations.append(current_fixation)
                current_fixation = []
            current_saccade.append(df[['T', 'AVG_X', 'AVG_Y']].iloc[i].values)
    
    # Append the last fixation or saccade
    if current_fixation:
        fixations.append(current_fixation)
    if current_saccade:
        saccades.append(current_saccade)
    
    # Print the first 2 elements of fixations and saccades for debugging
    print("fixation 1:",fixations[0])
    print("saccades1:",saccades[0])

    # Extract features
    fixation_start_times = [fixation[0][0] for fixation in fixations] if fixations else []
    avg_fixation_durations = [sum([point[0] for point in fixation]) / len(fixation) for fixation in fixations] if fixations else []
    avg_saccade_durations = [sum([point[0] for point in saccade]) / len(saccade) for saccade in saccades] if saccades else [0]
    total_fixations = len(fixations)
    total_saccades = len(saccades)
    saccade_fixation_ratio = total_saccades / total_fixations if total_fixations > 0 else 0
    
    # Construct feature dictionary
    features = {
        'First Fixation Start Time': min(fixation_start_times) if fixation_start_times else 0,
        'Average Fixation Duration': sum(avg_fixation_durations) / len(avg_fixation_durations) if avg_fixation_durations else 0,
        'Average Saccade Duration': sum(avg_saccade_durations) / len(avg_saccade_durations) if len(avg_saccade_durations) > 0 else 0,
        'Total Fixations': total_fixations,
        'Total Saccades': total_saccades,
        'Saccade-Fixation Ratio': saccade_fixation_ratio
    }
    return features

# Process the specified CSV file
file_path = "D:/Grad Projroj/test.csv"
features = process_csv_file(file_path)
print("Extracted features:")
print(features)  # Print the extracted features
