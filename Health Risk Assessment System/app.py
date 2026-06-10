from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ==========================================
# SMART HEALTH ADVISOR
# ==========================================

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health_report', methods=['POST'])
def health_report():

    data = request.get_json()

    name = data["name"]
    gender = data["gender"]

    age = int(data["age"])
    weight = float(data["weight"])
    height = float(data["height"])

    water = int(data["water"])
    exercise = int(data["exercise"])

    smoking = data["smoking"]
    diabetes = data["diabetes"]
    bp = data["bp"]

    # ==========================================
    # BMI CALCULATION
    # ==========================================

    bmi = round(
        weight / ((height / 100) ** 2),
        2
    )

    if bmi < 18.5:
        bmi_status = "Underweight"

    elif bmi < 25:
        bmi_status = "Normal Weight"

    elif bmi < 30:
        bmi_status = "Overweight"

    else:
        bmi_status = "Obese"

    # ==========================================
    # DISEASE RISK ASSESSMENT
    # ==========================================

    risk_points = 0

    if age > 50:
        risk_points += 20

    if smoking == "yes":
        risk_points += 25

    if diabetes == "yes":
        risk_points += 20

    if bp == "yes":
        risk_points += 20

    if bmi >= 30:
        risk_points += 15

    if risk_points >= 60:
        risk = "High"

    elif risk_points >= 30:
        risk = "Moderate"

    else:
        risk = "Low"

    # ==========================================
    # HEALTH SCORE
    # ==========================================

    score = 100

    if bmi < 18.5:
        score -= 15

    elif bmi >= 30:
        score -= 25

    elif bmi >= 25:
        score -= 10

    if water < 8:
        score -= 10

    if exercise < 30:
        score -= 15

    if smoking == "yes":
        score -= 25

    if diabetes == "yes":
        score -= 15

    if bp == "yes":
        score -= 15

    if age > 50:
        score -= 10

    if score < 0:
        score = 0

    # ==========================================
    # HEALTH STATUS
    # ==========================================

    if score >= 80:
        health_status = "Good Health"

    elif score >= 60:
        health_status = "Moderate Health"

    else:
        health_status = "Poor Health"

    # ==========================================
    # HEALTH TIPS
    # ==========================================

    tips = []

    if bmi >= 25:
        tips.append(
            "Reduce junk food and maintain a healthy diet."
        )

    if water < 8:
        tips.append(
            "Drink at least 8 glasses of water daily."
        )

    if exercise < 30:
        tips.append(
            "Exercise at least 30 minutes every day."
        )

    if smoking == "yes":
        tips.append(
            "Avoid smoking and tobacco products."
        )

    if diabetes == "yes":
        tips.append(
            "Monitor blood sugar levels regularly."
        )

    if bp == "yes":
        tips.append(
            "Reduce salt intake and monitor blood pressure."
        )

    if len(tips) == 0:
        tips.append(
            "Excellent health habits. Keep it up!"
        )

    # ==========================================
    # RESPONSE
    # ==========================================

    return jsonify({

        "name": name,

        "gender": gender,

        "age": age,

        "bmi": bmi,

        "bmi_status": bmi_status,

        "water": water,

        "exercise": exercise,

        "risk": risk,

        "health_score": score,

        "health_status": health_status,

        "tips": tips

    })


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)