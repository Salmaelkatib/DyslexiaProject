import pandas as pd

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
def process_gaze_info(gazeDataArray , ppi):

     # Convert the array of dictionaries into a DataFrame
    df = pd.DataFrame(gazeDataArray)
    
    # Drop rows with any empty cells in the required columns
    df = df.dropna(subset=['timestamp', 'x', 'y'])

    # Initialize variables
    fixations = []
    saccades = []
    current_fixation = []
    current_saccade = []
    saccade_duration=[]

    print('ppi',ppi)
    velocity_threshold =(500*ppi)/25.4 # px/s 
    print('Velocity Threshold:',velocity_threshold)
    min_fixation_duration = 150 # milliseconds
    print('Duration Threshold:',min_fixation_duration)
    
    # Loop through the eye-tracking data
    for i in range(len(df) - 1):
        velocity = calculate_velocity(df['x'].iloc[i], df['y'].iloc[i], df['x'].iloc[i+1], df['y'].iloc[i+1], df['timestamp'].iloc[i], df['timestamp'].iloc[i+1])
        duration = df['timestamp'].iloc[i+1] - df['timestamp'].iloc[i]

        if velocity < velocity_threshold :
            print(velocity ,'TRUE')
            if current_saccade:
                if len(current_saccade)==1:
                   duration = df['timestamp'].iloc[i] - df['timestamp'].iloc[i-1]
  
                saccades.append(current_saccade)
                saccade_duration.append(duration)
                current_saccade = []
            current_fixation.append(df[['timestamp', 'x', 'y']].iloc[i].values)
        else:
            print(velocity ,'FALSE')
            if current_fixation :
                fixations.append(current_fixation)
                current_fixation = []
            current_saccade.append(df[['timestamp', 'x', 'y']].iloc[i].values)

    # Append the last current fixation or saccade if not empty
    if current_fixation:
        fixations.append(current_fixation)
    if current_saccade:
        saccades.append(current_saccade)

    
    new_saccades = []
    for i in range(len(saccades)-1):  
        print('saccade_duration', saccade_duration[i])
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
        'Average Fixation Duration': sum(avg_fixation_durations) / len(avg_fixation_durations) if avg_fixation_durations else 0,
        'Average Saccade Duration': sum(avg_saccade_durations) / len(avg_saccade_durations) if avg_saccade_durations else 0,
        'Total Fixations': total_fixations,
        'Total Saccades': total_saccades,
    }
    return features


