import os
import pandas as pd

# Function to calculate the dispersion
def calculate_dispersion(gaze_points):
    x_coords = [point[1] for point in gaze_points]
    y_coords = [point[2] for point in gaze_points]
    dispersion = (max(x_coords) - min(x_coords)) + (max(y_coords) - min(y_coords))
    return dispersion

def process_gaze_info(gazeDataArray , ppi):

    dispersion_threshold=33

    # Convert the array of dictionaries into a DataFrame
    df = pd.DataFrame(gazeDataArray)
    
    # Drop rows with any empty cells in the required columns
    df = df.dropna(subset=['timestamp', 'x', 'y'])

    # Initialize variables
    fixations = []
    saccades = []
    i = 0
    while i < len(df):
        current_fixation = [df[['timestamp', 'x', 'y']].iloc[i].values.tolist()]
        j = i + 1
        while j < len(df):
            candidate_fixation = current_fixation + [df[['timestamp', 'x', 'y']].iloc[j].values.tolist()]
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