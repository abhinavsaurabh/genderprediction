import csv
from flask import Flask, render_template, jsonify, request
from gender_predictor import GenderPredictor
app = Flask(__name__)
data_location = 'gender-data/genders.csv'


def find_gender(name):
    genders = []
    with open(data_location) as fp:
        reader = csv.DictReader(fp)
        for line in reader:
            if line['name'] == name:
                genders.append(line)
    return genders

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api():
    name = request.args.get('name')
    data = getfile(data_location)
    gender_dict = json_list(data, name)
    return jsonify({"list": gender_dict})


@app.route('/search', methods=['POST'])
def search():
    gp = GenderPredictor()
    accuracy = gp.train_and_test(training_percent=0.80)*100
    features = gp.get_most_informative_features(n=10)
    name = request.form['query'].lower()
    finalgender=gp.classify_name(name)

    gender_dict = find_gender(name)
    if finalgender[0]=='Male':
        return render_template("male.html")
    else: return render_template("female.html")
   # return jsonify({"You are": finalgender})

 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run()
