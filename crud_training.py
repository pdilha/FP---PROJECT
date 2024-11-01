workouts = []

def create_workout(name, date, distance, time, localization, weather):
    new_workout = {
        "id": len(workouts) + 1,
        "nome": name,
        "date":  date,
        "distance": distance,
        "time": time,
        "localization": localization,
        "weather": weather
    } 
    workouts.append(new_workout)

def read_workout():
    for workout in workouts:
        print(workouts)