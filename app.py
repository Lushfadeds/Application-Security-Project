from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('admin_dashboard.html')
    # Remember to change the render_template ah... I just testing my own side lol
    # Idk how to fix the footer sia i try so hard but i scared sekali you guys need to adjust also
    # Love, Kerndall


if __name__ == '__main__':
    app.run(debug='True')