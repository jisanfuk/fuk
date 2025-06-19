
from flask import Flask, render_template, request

app = Flask(__name__)

def predict_result(inputs):
    # Simple logic: if BIG > SMALL, return BIG else SMALL
    big_count = inputs.count("BIG")
    small_count = inputs.count("SMALL")
    return "BIG" if big_count >= small_count else "SMALL"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        input1 = request.form.get("input1", "").strip().upper()
        input2 = request.form.get("input2", "").strip().upper()
        input3 = request.form.get("input3", "").strip().upper()
        input4 = request.form.get("input4", "").strip().upper()
        inputs = [input1, input2, input3, input4]
        if all(i in ["BIG", "SMALL"] for i in inputs):
            prediction = predict_result(inputs)
        else:
            prediction = "Invalid input. Use BIG or SMALL only."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
