from flask import Flask, jsonify, request 


app = Flask(__name__)

@app.route("/")

def home():
     return "WUZZZZAAAAAAAAP"

@app.route("/about")
def about():
     return [1,2,3,4,5,6,]

@app.route("/hackathon")

def hackathon ():
    return jsonify({
         "event": "GDC Hackathon", 
         "date": "November 14",
         "my_skills": ["python","design"]
    })
    
people = [
    {"id": 1, "name": "Aarushi", "skills": ["python"]},
    {"id": 2, "name": "Sammy the Slug", "skills": ["design"]},
]

@app.route("/people")
def get_people():
     skill = request.arge.get("skill")
     if skill :
          return jsonify([p for p in people if skill in p["skills"]])
     return jsonify(people) 

@app.route("/people", methods=["POST"])
def add_person():
     data = request.get.json()
     if not data or "name" not in data:
          return jsonify({"error": "name is required"}), 400

     new_person ={
        "id": len(people) + 1,
        "name": data["name"],
        "skills": data.get("skills", []),
        "idea": data.get("idea", ""),
     }
     people.append(new_person)
     return jsonify(new_person), 201

ideas = []

@app.route("/ideas", methods=["POST"])
def add_idea():
    data = request.get_json()
    ideas.append(data["text"])
    return jsonify(ideas), 201

@app.route("/ideas")
def get_ideas():
    return jsonify(ideas)



if __name__ == "__main__":
    app.run(debug=True)