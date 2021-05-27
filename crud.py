from flask import *
import sqlite3
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/product")
def product():
    return render_template("Productsone.html")

@app.route("/products")
def products():
    return render_template("Productstwo.html")
@app.route("/order")
def order():
    return render_template("Order.html")


@app.route("/submit",methods = ["POST","GET"])
def submit():
    if request.method == "POST":
        try:
            Name = request.form["Name"]
            Email = request.form["email"]
            Phonenumber = request.form["phone number"]
            Address = request.form["address"]
            name = request.form["name"]
            Quantity = request.form["Quantity"]
            with sqlite3.connect("factory.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into products (Name, email, phone number, address, name, Quantity) values (?,?,?,?,?,?)",(Name,Email,Phonenumber,Address,name,Quantity))
                con.commit()
                msg = "Order Placed Successfully"
        except:
            con.rollback()
            msg = "Give details properly"
        finally:
            return render_template("Success.html", msg = msg)
            con.close()


if __name__=="__main__":
    app.run(debug = True)
            
                    
            
                
            
