from flask import request,render_template
from many2many.controllermany import *
from many2many.many_2_many import *


def dummy_shop():
    return Shop(id=0, sname="", sadr='',sowner='')

def sortbyname(prod):
    return prod.pname

def get_products():
    products=Product.query.all()
    products.sort(key=sortbyname)
    return products

@app.route('/shop/welcome/')
def Wel_page():
    shop=Shop.query.all()
    if shop==None:
        shop=dummy_shop()
    return render_template("shop.html",products=Product.query.all(),shop=dummy_shop(),shops=shop,)

@app.route('/shop/save/' , methods=["POST"])
def save_shop():
    print(request.form)

    pids=request.form.getlist('produ')

    shopp=Shop(sname=request.form['sname'],sowner=request.form['sowner'],sadr=request.form['sadr'])
    if pids:
       for id in pids:
          dbprod=Product.query.filter_by(id=int(id)).first()
          shopp.product.append(dbprod)
    db.session.add(shopp)
    db.session.commit()
    msg = "Shop added added succesfully...!"
    if int(request.form['id']) > 0:
        shopob = Shop.query.filter_by(id=int(request.form['id'])).first()
        shopob.sname = request.form['sname']
        shopob.sowner = request.form['sowner']
        shopob.sadr = request.form['sadr']

        db.session.commit()
        msg = "shop Updated succesfully..."
    return render_template('shop.html', products=get_products(),shop=dummy_shop(), msg=msg,shops=Shop.query.all())


@app.route("/shop/edit/<int:id>")
def shop_edit(id):
    shopob = Shop.query.filter_by(id=id).first()
    return render_template("shop.html", products=get_products(),
                           shop=shopob, msg='msg', shops=Shop.query.all())


@app.route('/shop/delete/<int:id>')
def shop_delete(id):
    shopob = Shop.query.filter_by(id=id).first()
    db.session.delete(shopob)
    msg = "shop deleted succesfully...!"
    return render_template("shop.html", shop=dummy_shop(),
                           products=get_products(), msg=msg, shops=Shop.query.all())




# if __name__ == '__main__':
#     app.run(debug=True)