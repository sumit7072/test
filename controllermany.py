from flask import request,render_template
from many2many.many_2_many import*

def dummy_prod():
    return Product(id=0,pname="",pqty=0)



@app.route("/prod/welcome/")
def wel_page():
    return render_template("prod.html",prod=dummy_prod(),products=Product.query.all())

@app.route('/prod/save/', methods=["POST"])
def add_update():
    id=int(request.form["id"])
    if id==0:
        prodd=Product(**request.form)
        db.session.add(prodd)
        db.session.commit()
        # prodd.id=int(request.form["id"])
        msg="Product <{}> added succesfully...!"
    else:
       prodd=Product.query.filter_by(id=id).first()
    if prodd:
        prodd.pname=request.form['pname']
        prodd.pqty=request.form["pqty"]
        db.session.commit()
        msg="Product <{}> record updated succesfully...!"
    return render_template("prod.html",prod=dummy_prod(),products=Product.query.all(),amsg=msg)

@app.route("/prod/edit/<int:id>",methods=["GET"])
def edit_prod(id):
    prodd = Product.query.filter_by(id=id).first()
    # db.session.commit()
    return render_template("prod.html",prod=prodd,products=Product.query.all())

@app.route("/prod/delete/<int:id>",methods=["GET"])
def delete_prod(id):
    prodd = Product.query.filter_by(id=id).first()
    db.session.delete(prodd)
    db.session.commit()
    msg="Product <{}> deledted succesfully...!"
    return render_template("prod.html",prod=dummy_prod(),products=Product.query.all(),amsg=msg.format(prodd.id))


# if __name__ == '__main__':
    # app.run(debug=True)
