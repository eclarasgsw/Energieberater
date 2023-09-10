from flask import Flask, render_template, request
import json

app = Flask(__name__)

JSON_DATA = {
  "results": [{
    'id': 1,
    'adresse': 'Vadianstrasse 8, 9000 St.Gallen',
    'waerme': 'Fernwärme',
    'solar_potential': 'sehr gut'
  }, {
    'id': 2,
    'adresse': 'Vadianstrasse 10, 9000 St.Gallen',
    'waerme': 'Holzheizung',
    'solar_potential': 'schlecht',
  }]
}


@app.route("/")
def home():
  data = JSON_DATA["results"]
  return render_template('home.html', data=data)


#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask#using-json-data


@app.route("/search", methods=['POST'])
def search():
  try:
    with open("data/input_data.json", 'r') as json_file:
      data = json.load(json_file)

    searched_string = request.form.get('query')
    filtered_data = []

    print('data: ', data)

    for record in data:
      if searched_string in record['adresse']:
        filtered_data.append(record)
        print("your word has been found and appended to filtered_data")

    #for record in filtered_data:
      #print(record)
    print(filtered_data)
    return render_template("search_results.html",
                           searched_string=searched_string,
                           filtered_data=filtered_data)

  except FileNotFoundError:
    print("File 'data/input_data.json' not found.")
  except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")

  #data=JSON_DATA["results"]

  #filtered_data = data.query(filterdata.adresse.like(searched_string)).all()

  #return render_template("search_results.html", searched_string=searched_string, filtered_data=filtered_data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
