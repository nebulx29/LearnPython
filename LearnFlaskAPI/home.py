from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
#     localhost:5000/
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)