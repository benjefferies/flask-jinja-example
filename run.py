from flask import Flask, render_template

app = Flask(__name__) # Create flask app


@app.route("/") # Define route at http://localhost:5000
def template_test():
    return render_template('template.html', my_string="Some stuff here!") # render template using model


if __name__ == '__main__':
    app.run(debug=True) # Start flask server
