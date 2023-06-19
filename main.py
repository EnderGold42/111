from flask import Flask, render_template, request, make_response, flash, redirect 
#
app = Flask(__name__)
#                                            

@app.route("/")
def index():
    strng = request.cookies.get('strng')
    if strng is None:
        user = "Курсант"
    else:
        user = strng
    resp = make_response(render_template('index.html', name=user))
    return resp
#

@app.route("/about")
def about():
    return render_template('about.html', title='About')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
