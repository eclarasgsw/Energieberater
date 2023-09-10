from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
  #data = JSON_DATA["results"]
  return render_template('home.html')


#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask#using-json-data


@app.route("/search", methods=['POST'])
def search():
  try:
    with open("data/input_data.json", 'r') as json_file:
      data = json.load(json_file)

    searched_string = request.form.get('query')
    print(searched_string)
    filtered_data = []

    for record in data:
      if searched_string in record['adresse']:
        filtered_data.append(record)
        print("your word has been found and appended to filtered_data")
      
      else:
        print("this string hasn't been found")


    print(filtered_data)
    return render_template("search_results.html",
                           searched_string=searched_string,
                           filtered_data=filtered_data)

  except FileNotFoundError:
    print("File 'data/input_data.json' not found.")
  except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
