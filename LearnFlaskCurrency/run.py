from flask import Flask, render_template, request
app = Flask(__name__)

class CurrConv():
    def __init__(self, curr1, curr2, fxrate):
        self.curr1 = curr1
        self.curr2 = curr2
        if fxrate == None:
            self.fxrate = 0.0
        else:
            self.fxrate = float(fxrate)
        
    def exchange(self, amount):
        #print("Currconv().exchange(" + str(amount) + ") invoked")
        return amount * self.fxrate    

@app.route("/currconv")
def currconv():
    cc = CurrConv(request.args.get("curr1"), request.args.get("curr2"), request.args.get("fxrate"))
    return render_template("currconv.html", cc=cc)   
