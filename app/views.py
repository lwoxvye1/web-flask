from app import app
from flask import Flask, render_template, request
import pymysql
import json


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index', methods=["GET"])
def index2():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def getValue():
    username = request.form["username"]
    password = request.form["password"]
    print("599874")
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "select 用户名,密码 from 账号"
    cursor.execute(sql)
    truedata = cursor.fetchall()
    for i in range(len(truedata)):
        if username == truedata[i][0]:
            if password == truedata[i][1]:
                cursor.close()
                db.close()
                return render_template("index.html", username=username)
            else:
                cursor.close()
                db.close()
                return render_template("会员登录.html", tip="输入的密码有误！请重新输入")
    cursor.close()
    db.close()
    return render_template("会员登录.html", tip="输入的用户名不存在！请重新输入")


@app.route('/register', methods=["GET"])
def register():
    return render_template("会员注册.html")


@app.route('/register_success', methods=["POST"])
def register_success():
    telephone = request.form["telephone"]
    username = request.form["username"]
    password = request.form["password"]
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    sql = "INSERT INTO 账号 VALUES(%s, %s, %s)"
    par = (telephone, username, password)
    cursor = db.cursor()
    try:
        cursor.execute(sql, par)
        db.commit()
    except:
        db.rollback()
        return render_template("会员注册.html", warn="该手机号已被注册！请重新注册")
    cursor.close()
    return render_template("会员注册.html", cong="注册成功！请登录")


@app.route('/login', methods=["GET"])
def login():
    return render_template("会员登录.html")


@app.route('/search', methods=["GET"])
def search():
    return render_template("search.html")


@app.route('/look', methods=["GET"])
def look():
    return render_template("try-reading.html")


@app.route('/discount', methods=["GET"])
def discount():
    return render_template("sales.html")


@app.route('/news', methods=["GET"])
def news():
    return render_template(r"news/news.html")


@app.route('/books1', methods=["GET"])
def books1():
    return render_template(r"books/财政学.html")


@app.route('/books2', methods=["GET"])
def books2():
    return render_template(r"books/电工电子学实践教程.html")


@app.route('/books3', methods=["GET"])
def books3():
    return render_template(r"books/起重机金属结构设计.html")


@app.route('/books4', methods=["GET"])
def books4():
    return render_template(r"books/系统工程导论.html")


@app.route('/books5', methods=["GET"])
def books5():
    return render_template(r"books/企业会计制度设计.html")


@app.route('/books6', methods=["GET"])
def books6():
    return render_template(r"books/化工机械及设备.html")


@app.route('/books7', methods=["GET"])
def books7():
    return render_template(r"books/物流自动化技术及应用.html")


@app.route('/books8', methods=["GET"])
def books8():
    return render_template(r"books/项目管理知识体系指南.html")


@app.route('/books9', methods=["GET"])
def books9():
    return render_template(r"books/电工学.html")


@app.route('/books10', methods=["GET"])
def books10():
    return render_template(r"books/系统工程导论.html")


@app.route('/books11', methods=["GET"])
def books11():
    return render_template(r"books/工程经济学.html")


@app.route('/books12', methods=["GET"])
def books12():
    return render_template(r"books/结构力学.html")


@app.route('/books13', methods=["GET"])
def books13():
    return render_template(r"books/起重机金属结构设计.html")


@app.route('/books14', methods=["GET"])
def books14():
    return render_template(r"books/企业会计制度设计.html")


@app.route('/books15', methods=["GET"])
def books15():
    return render_template(r"books/团队管理.html")


@app.route('/books16', methods=["GET"])
def books16():
    return render_template(r"books/工程造价编制与职业素养.html")


@app.route('/books17', methods=["GET"])
def books17():
    return render_template(r"books/系统工程导论.html")


@app.route('/books18', methods=["GET"])
def books18():
    return render_template(r"books/管理信息系统.html")


@app.route('/books19', methods=["GET"])
def books19():
    return render_template(r"books/虚拟仪器原理及应用.html")


@app.route('/books20', methods=["GET"])
def books20():
    return render_template(r"books/工程经济学.html")


@app.route('/books21', methods=["GET"])
def books21():
    return render_template(r"books/虚拟仪器原理及应用.html")


@app.route('/books22', methods=["GET"])
def books22():
    return render_template(r"books/系统工程导论.html")


@app.route('/books23', methods=["GET"])
def books23():
    return render_template(r"books/化工机械及设备.html")


@app.route('/books24', methods=["GET"])
def books24():
    return render_template(r"books/电工学.html")


@app.route('/books25', methods=["GET"])
def books25():
    return render_template(r"books/电力电子技术.html")


@app.route('/books26', methods=["GET"])
def books26():
    return render_template(r"books/海事法.html")


@app.route('/books27', methods=["GET"])
def books27():
    return render_template(r"books/国际航运管理国际航运管理.html")


@app.route('/books28', methods=["GET"])
def books28():
    return render_template(r"books/电子商务系统分析与设计.html")


@app.route('/bottom_payment', methods=["GET"])
def bottom_payment():
    return render_template(r"bottom/payment.html")


@app.route('/bottom_zhuanzhang', methods=["GET"])
def bottom_zhuanzhang():
    return render_template(r"bottom/zhuanzhang.html")


@app.route('/bottom_lianxi', methods=["GET"])
def bottom_lianxi():
    return render_template(r"bottom/lianxi.html")


@app.route('/bottom_tousu', methods=["GET"])
def bottom_tousu():
    return render_template(r"bottom/tousu.html")


@app.route('/bottom_introduction', methods=["GET"])
def bottom_introduction():
    return render_template(r"bottom/introduction.html")


@app.route('/bottom_lianmeng', methods=["GET"])
def bottom_lianmeng():
    return render_template(r"bottom/lianmeng.html")


@app.route('/look_book1', methods=["GET"])
def look_book1():
    return render_template(r"try-reading/财政学试读.html")


@app.route('/look_book2', methods=["GET"])
def look_book2():
    return render_template(r"try-reading/管理信息系统试读.html")


@app.route('/look_book3', methods=["GET"])
def look_book3():
    return render_template(r"try-reading/虚拟仪器原理及应用.html")


@app.route('/look_book4', methods=["GET"])
def look_book4():
    return render_template(r"try-reading/企业研究方法试读.html")


@app.route('/catalog_财务与会计系', methods=["GET"])
def catalog_财务与会计系():
    return render_template(r"catalog/财务与会计系.html")


@app.route('/catalog_工商与公共管理系', methods=["GET"])
def catalog_工商与公共管理系():
    return render_template(r"catalog/工商与公共管理系.html")


@app.route('/catalog_管理科学系', methods=["GET"])
def catalog_管理科学系():
    return render_template(r"catalog/管理科学系.html")


@app.route('/catalog_计算机科学系', methods=["GET"])
def catalog_计算机科学系():
    return render_template(r"catalog/计算机科学系.html")


@app.route('/catalog_电子工程系', methods=["GET"])
def catalog_电子工程系():
    return render_template(r"catalog/电子工程系.html")


@app.route('/catalog_信息与计算机科学系', methods=["GET"])
def catalog_信息与计算机科学系():
    return render_template(r"catalog/信息与计算机科学系.html")


@app.route('/catalog_艺术设计系', methods=["GET"])
def catalog_艺术设计系():
    return render_template(r"catalog/艺术设计系.html")


@app.route('/catalog_行政管理系', methods=["GET"])
def catalog_行政管理系():
    return render_template(r"catalog/行政管理系.html")


@app.route('/catalog_环境与安全工程系', methods=["GET"])
def catalog_环境与安全工程系():
    return render_template(r"catalog/环境与安全工程系.html")


@app.route('/catalog_港口与航道工程系', methods=["GET"])
def catalog_港口与航道工程系():
    return render_template(r"catalog/港口与航道工程系.html")


@app.route('/catalog_管理系', methods=["GET"])
def catalog_管理系():
    return render_template(r"catalog/管理系.html")


@app.route('/catalog_交通工程系', methods=["GET"])
def catalog_交通工程系():
    return render_template(r"catalog/交通工程系.html")


@app.route('/catalog_国际航运系', methods=["GET"])
def catalog_国际航运系():
    return render_template(r"catalog/国际航运系.html")


@app.route('/catalog_航海系', methods=["GET"])
def catalog_航海系():
    return render_template(r"catalog/航海系.html")


@app.route('/catalog_轮机工程系', methods=["GET"])
def catalog_轮机工程系():
    return render_template(r"catalog/轮机工程系.html")


@app.route('/catalog_英语系', methods=["GET"])
def catalog_英语系():
    return render_template(r"catalog/英语系.html")


@app.route('/catalog_日语系', methods=["GET"])
def catalog_日语系():
    return render_template(r"catalog/日语系.html")


@app.route('/catalog_机械工程系', methods=["GET"])
def catalog_机械工程系():
    return render_template(r"catalog/机械工程系.html")


@app.route('/catalog_工业工程系', methods=["GET"])
def catalog_工业工程系():
    return render_template(r"catalog/工业工程系.html")


@app.route('/catalog_电气自动化系', methods=["GET"])
def catalog_电气自动化系():
    return render_template(r"catalog/电气自动化系.html")


@app.route('/catalog_法律系', methods=["GET"])
def catalog_法律系():
    return render_template(r"catalog/法律系.html")


@app.route('/news1', methods=["GET"])
def news1():
    return render_template(r"news/news1.html")


@app.route('/news2', methods=["GET"])
def news2():
    return render_template(r"news/news2.html")


@app.route('/news3', methods=["GET"])
def news3():
    return render_template(r"news/news3.html")


@app.route('/news4', methods=["GET"])
def news4():
    return render_template(r"news/news4.html")


@app.route('/news5', methods=["GET"])
def news5():
    return render_template(r"news/news5.html")


@app.route("/to_liuyan", methods=["post"])
def to_liuyan():
    idliuyan = request.get_json()["idliuyan"]
    shijian = request.get_json()["shijian"]
    book = request.get_json()["book"]
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "INSERT INTO liuyan VALUES(%s, %s, %s)"
    par = (idliuyan, shijian, book)
    try:
        cursor.execute(sql, par)
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()
    return render_template(r"books/财政学.html")


@app.route("/to_shopping_cart", methods=["POST"])
def to_shopping_cart():
    name = request.get_json()["name"]
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "SELECT itemname,ISBN,author,price,link FROM item where itemname= %s "
    par = name
    cursor.execute(sql, par)
    data = cursor.fetchall()
    itemname = data[0][0]
    ISBN = data[0][1]
    author = data[0][2]
    price = data[0][3]
    link = data[0][4]
    sql = "INSERT INTO cart VALUES(%s, %s, %s, %s, %s)"
    par = (itemname, ISBN, author, price, link)
    try:
        cursor.execute(sql, par)
        db.commit()
    except:
        db.rollback()
    cursor.close()
    return render_template("book1.html")


@app.route('/liuyan', methods=["GET"])
def liuyan():
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "SELECT idliuyan,shijian,book FROM liuyan ORDER BY shijian DESC"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    dict1 = {}
    for i in range(len(data)):
        dict1[i] = data[i]
    return render_template("liuyan.html", dict1=dict1)


@app.route("/shoppingcart", methods=["GET"])
def shoppingcart():
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "SELECT name,ISBN,author,price,link FROM cart  "
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    dict1 = {}
    sum = 0
    for i in range(len(data)):
        dict1[i] = data[i]
        sum += data[i][3]
    return render_template("shopping cart.html", dict1=dict1, sum=sum, len=len(dict1))


@app.route("/del1", methods=["POST"])
def del1():
    num = request.get_json()["code"]
    code = num[-13:]
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "DELETE FROM cart WHERE ISBN= %s "
    par = code
    try:
        cursor.execute(sql, par)
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()
    return render_template("shopping cart.html")


@app.route("/checkstand", methods=["GET"])
def checkstand():
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "SELECT name,ISBN,author,price,link,amount,sum FROM checkstand  "
    cursor.execute(sql)
    data = cursor.fetchall()
    dict1 = {}
    sum = 0
    for i in range(len(data)):
        dict1[i] = data[i]
        sum += data[i][6]
    cursor.close()
    db.close()
    return render_template("checkstand.html", dict1=dict1, sum=sum)


@app.route("/to_checkstand", methods=["POST"])
def to_checkstand():
    ISBN = []
    list = request.get_json()["0"]
    amount = request.get_json()["1"]
    sum = request.get_json()["2"]
    for i in range(len(list)):
        ISBN.append(list[i][-13:])
    db = pymysql.connect("localhost", "root", "password", "会员管理")
    cursor = db.cursor()
    sql = "DELETE   FROM  checkstand"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    for i in range(len(ISBN)):
        sql = "SELECT itemname,ISBN,author,price,link FROM item where ISBN= %s "
        par = ISBN[i]
        cursor.execute(sql, par)
        data = cursor.fetchall()
        sql = "INSERT INTO checkstand VALUES(%s, %s, %s, %s, %s, %s, %s)"
        par = (data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], amount[i], sum[i])
        try:
            cursor.execute(sql, par)
            db.commit()
        except:
            db.rollback()

    sql = "SELECT name,ISBN,author,price,link,amount,sum FROM checkstand  "
    cursor.execute(sql)
    data = cursor.fetchall()
    dict1 = {}
    sum = 0
    for i in range(len(data)):
        dict1[i] = data[i]
        sum += data[i][6]
    cursor.close()
    db.close()
    return render_template("checkstand.html", dict1=dict1)


@app.route("/del2", methods=["POST"])
def del2():
        db = pymysql.connect("localhost", "root", "password", "会员管理")
        cursor = db.cursor()
        sql = "SELECT ISBN FROM checkstand  "
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in range(len(data)):
            sql = "DELETE   FROM  cart WHERE ISBN=%s"
            par = data[i][0]
            try:
                cursor.execute(sql, par)
                db.commit()
            except:
                db.rollback()
        cursor.close()
        db.close()


@app.route("/purchase", methods=["GET"])
def purchase():
    return render_template("purchase.html")


@app.route("/to_success", methods=["GET"])
def to_success():
    return render_template("success.html")


@app.route("/transport", methods=["GET"])
def transport():
    return render_template("transport.html")