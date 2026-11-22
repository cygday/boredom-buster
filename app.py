from datetime import datetime
import random
from flask import Flask, jsonify

app = Flask(__name__)

WORKOUTS = {
    "morning": [
        "10-Min Energy Flow: 20 Jumping Jacks, 10 Push-ups, 15 Squats (3 rounds)",
        "Desk-Breaker Mobility: 5-Min Sun Salutations + 2-Min Plank Hold",
        "Cardio Wakeup: 30s High Knees, 30s Rest (Repeat 8 times)",
    ],
    "evening": [
        "Stress-Melter Stretch: 10-Min Deep Hip & Hamstring Yoga",
        "Boredom Buster Core: 20 Bicycle Crunches, 15 Leg Raises, 20 Russian Twists (3 rounds)",
        "Shadowboxing Burn: 3-Min Shadowboxing, 1-Min Squat Hold (3 rounds)",
    ],
}


@app.route("/")
def get_workout():
    current_hour = datetime.now().hour
    period = "morning" if 5 <= current_hour < 17 else "evening"
    routine = random.choice(WORKOUTS[period])
    return jsonify({
        "time_of_day": period,
        "boredom_buster_workout": routine,
        "tip": "Refresh the page for a new random routine!",
    })


@app.route("/<period>")
def get_specific_workout(period):
    period = period.lower()
    if period not in WORKOUTS:
        return jsonify({"error": "Use /morning or /evening"}), 400
    return jsonify({
        "time_of_day": period,
        "boredom_buster_workout": random.choice(WORKOUTS[period]),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
