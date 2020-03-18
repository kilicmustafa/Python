from flask import Flask ,render_template ,flash ,redirect ,url_for, request ,session 
from flask_mysqldb import MySQL
from wtforms import Form ,StringField ,TextAreaField ,PasswordField ,validators  
from passlib.hash import sha256_crypt
from functools import wraps

#kullanıcı giriş kontrol decoratorü
def login_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "login" in session :
            return function(*args, **kwargs)

        else:
            flash("Bu sayfayı görüntülemeye hakkınız yok lütfen giriş yapınız.." ,"warning")
            return redirect(url_for("login"))
    return decorated_function


class RegisterForm(Form):
    FirstName = StringField("İsminiz :" ,validators=[validators.length(min=3 ,max=15 ,message="Lütfen isminizi giriniz")])
    LastName = StringField("Soyisminiz :" ,validators=[validators.length(min=2 ,max=15 ,message ="Lütfen soyisminizi giriniz")])
    UserName = StringField("Kullanıcı adı :" ,validators=[validators.DataRequired(message="Lütfen Kullanıcı Adınızı Giriniz")])
    Email = StringField("Email :",validators=[validators.Email(message="Lütfen geçerli bir email adresi giriniz")])
    PhoneNumber = StringField("Telefon Numaranız :", validators=[validators.length(min=9 ,max=10 ,message="Lütfen telefon numaranızı başında sıfır olmadan giriniz")])
    Password = PasswordField("Parola :" ,validators=[
        validators.length(min= 6 ,max=40 ,message="Minimum 6 maxsimium 60 karakterden oluşan bir şifre belirleyiniz"),
        validators.EqualTo(fieldname="confirm" ,message="Parolalar uyuşmuyor...")
    ])
    confirm = PasswordField("Parola doğrula :")  
    
    
    
class LoginForm(Form):
    UserName = StringField("Kullanıcı adı :")
    Password = PasswordField("Parola :")



class ArticleForm(Form):
    title = StringField("Makale Başlığı" ,validators=[validators.DataRequired(message="Lütfen bir makale başlığı belirleyiniz")])
    content = TextAreaField("Makale içeriği" ,validators=[validators.DataRequired(message="Lütfen makale içeriğini doldurunuz")])


class AcceptForm(Form):

    accept = StringField("Bu makaleyi silmek için Kutucuğun içireisine 'ONAYLA' yazınız ",validators=[validators.DataRequired(message="Lütfen bu alanı doldurunuz")])




app = Flask(__name__)
app.secret_key = "key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "newdb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register" , methods =["GET" ,"POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():

        FirstName = form.FirstName.data
        LastName = form.LastName.data
        UserName = form.UserName.data
        Email = form.Email.data
        PhoneNumber = form.PhoneNumber.data
        Password = form.Password.data
        
        
        
        query = "INSERT INTO users(UserName ,Password ,FirstName ,LastName, Email ,PhoneNumber) VALUES(%s ,%s ,%s ,%s ,%s ,%s)"

        cursor = mysql.connection.cursor()
        cursor.execute(query ,(UserName , sha256_crypt.encrypt(Password) ,FirstName ,LastName ,Email ,int(PhoneNumber)))

        mysql.connection.commit()

        cursor.close()


        
        
        
        flash("Başarılı bir şekilde kayıt oldunuz" ,"success")
        return redirect(url_for("index"))


    return render_template("register.html" ,form = form)


@app.route("/login", methods=["GET" ,"POST"])
def login():

    form = LoginForm(request.form)


    if request.method == "POST":

        UserName = form.UserName.data
        user_password = form.Password.data


        query = "SELECT * FROM users WHERE UserName = %s"

        cursor = mysql.connection.cursor()

        feedback = cursor.execute(query ,(UserName,))

        if feedback > 0 :

            db_content = cursor.fetchone()
            
            cursor.close()
            real_password = db_content["Password"]

            if sha256_crypt.verify(user_password ,real_password):
                session["login"] = True
                session["username"] = UserName
                flash("Başarılı bir şekilder giriş yaptınız" ,"success")
                return redirect(url_for("index"))


            else:
                flash("Hatalı parola","danger")
                return redirect(url_for("login"))



        else:
            flash("Böyle bir kullanıcı bulunmuyor ... ","danger")
            return redirect(url_for("login"))

    return render_template("login.html" ,form = form)
        
         



@app.route("/logout")
def logout():
    session.clear()
    flash("Başarılı bir şekilde çıkışınız yapıldı ... ","success")
    return redirect(url_for("index"))


@app.route("/dashboard")
@login_required
def dashboard():

    username = session["username"]

    query= "SELECT * FROM articles WHERE author= %s"

    cursor = mysql.connection.cursor()

    feedback = cursor.execute(query ,(username,))

    if feedback > 0 :

        articles = cursor.fetchall()
        
        

        return render_template("dashboard.html" ,articles = articles )



    else: 

        return render_template("dashboard.html")

    

    


@app.route("/addarticle" ,methods=["GET" ,"POST"])
@login_required
def addarticle():

    form = ArticleForm(request.form)


    if request.method == "POST" and form.validate():
    
        title = form.title.data
        content = form.content.data

        username = session["username"] 

        
        cursor = mysql.connection.cursor()

        query = "INSERT INTO articles(title ,author ,content) VALUES(%s ,%s ,%s)"

        cursor.execute(query ,(title ,username ,content))

        mysql.connection.commit()
       
        cursor.close()


        flash("Makaleniz başarılı bir şekilde eklendi" ,"success")

        return redirect(url_for("dashboard"))



    return render_template("addarticle.html" ,form = form) 

@app.route("/articles")
def articles():

    cursor = mysql.connection.cursor()

    query = "SELECT * FROM articles"

    feedback = cursor.execute(query)

    if feedback > 0 :
        articles = cursor.fetchall()
        return render_template("articles.html" ,articles = articles)

    else:
        return render_template("articles.html")



@app.route("/article-<string:id>")
def article(id):

    query = "SELECT * FROM articles WHERE id = %s"

    cursor = mysql.connection.cursor()

    feedback = cursor.execute(query ,(id,))

    if feedback > 0 :

        article = cursor.fetchone()

        return render_template("article.html" , article = article)

    else:
        
        return render_template("article.html")

    
@app.route("/deleted-<string:id>" ,methods=["GET" ,"POST"]) 
@login_required
def deleted(id):
    
    query = "SELECT * FROM articles WHERE id = %s" 


    cursor = mysql.connection.cursor()
    feedback = cursor.execute(query ,(id,))
    form = AcceptForm(request.form)

    if feedback > 0:

        
        article = cursor.fetchone()
        
        if request.method == "POST" and form.validate() :
            
            if form.accept.data == "ONAYLA":

        
                if article["author"] == session["username"]:
                    
                    query_second = "DELETE from articles WHERE id = %s"

                    cursor.execute(query_second ,(id,))
                    mysql.connection.commit()
                    
                    flash("Makaleniz başarıyla silindi " ,"success")
                    return redirect(url_for("dashboard"))


                else:
                    
                    if session["login"]:
                        flash("Bu makaleyi silmeye yetkiniz yok" ,"warning")
                        return redirect(url_for("dashboard"))

                    else:
                        flash("Makale sileme işlemi için oturum açınız" ,"danger")
                        return redirect(url_for("login"))



            else:
                flash("Lütfen silmek için kutucuğa 'ONAYLA' yazınız " ,"danger")
                
    else :
        flash("Böyle bir makale bulunamadı ")
        return redirect(url_for("dashboard"))


    return render_template("deleted.html" , article  = article , form = form)

@app.route("/update-<string:id>" ,methods=["GET" ,"POST"])
@login_required
def update(id):



    if request.method == "GET":
       
        query = "SELECT * FROM articles WHERE id= %s"
        cursor = mysql.connection.cursor()

        feedback = cursor.execute(query ,(id,))

        if feedback > 0 :

            article = cursor.fetchone()

            form = ArticleForm()
            form.title.data = article["title"]
            form.content.data = article["content"]
            

            if article["author"] == session["username"] : 

                return render_template("update.html" ,form = form)
            else:

                if session["login"]:
                    flash("Bu Makaleyi düzenleme izniniz bulunmuyor" ,"warning")
                    return redirect(url_for("dashboard"))

                else: 
                    flash("Makale güncelleme işlemi için önce giriş yapınız" ,"warning")
                    return redirect(url_for("login"))

        else:

            flash("Böyle bir makale bulunamadı")
            return redirect(url_for("dashboard"))


    else:
        form = ArticleForm(request.form)

        newTitle = form.title.data
        newContent = form.content.data

        query_second = "UPDATE articles SET title = %s , content = %s WHERE id= %s"

        cursor = mysql.connection.cursor()
        cursor.execute(query_second ,(newTitle ,newContent ,id))

        mysql.connection.commit()


        flash("Makaleniz başarıyla güncellenmiştir" ,"success")
        return redirect(url_for("dashboard"))


    return render_template("update.html" , form = form)



@app.route("/search" ,methods=["GET" ,"POST"])
@login_required
def search():
    if request.method == "GET":
        return render_template("search.html")

    else:
        
        
        keyword = request.form.get("keyword")

        query = "SELECT * FROM articles WHERE title like '%" + keyword + "%'"
        cursor = mysql.connection.cursor()

        feedback = cursor.execute(query)

        if feedback > 0 :

            articles = cursor.fetchall()


            return render_template("search.html" ,articles = articles)

        else: 
            flash("Aradığınız kıriterlerde sonuc bulunamadı" ,"warning")

            return redirect(url_for("search"))



@app.route("/frendFind" ,methods = ["GET" ,"POST"])
@login_required
def frendFind():

    if request.method == "GET":

        return render_template("frendFind.html")


    else :

        keyword = request.form.get("keyword")

        
        cursor = mysql.connection.cursor()



        query= "SELECT * FROM frends WHERE me = %s"    

        cursor.execute(query ,(session["username"],))
        frends = cursor.fetchall()
        fsize = len(frends)  



        querty_second = "SELECT FrendRequest FROM users WHERE UserName = %s"
        cursor.execute(querty_second ,(session["username"],))
        #requestText = cursor.fetchone()

        #requests = requestText["FrendRequest"].split(",")
        #size = len(requests)

        cursor = mysql.connection.cursor()

        query_third =  "SELECT * FROM users WHERE UserName like '%" + keyword + "%'  or  FirstName like '%" + keyword + "%'  or LastName like '%" + keyword + "%'"

        

        feedback = cursor.execute(query_third) 

        if feedback > 0 :
            
            users = cursor.fetchall()

            


            return render_template("frendFind.html" ,users = users , frends = frends  ,fsize = fsize)

        else: 
            flash("Aradığınız kriterlere uygun sonuc buluunamadı" , "warning")
            return redirect(url_for("frendFind"))


@app.route("/FrendRequest-<string:UserName>" ) 
@login_required
def FrendRequest(UserName):


    query = "UPDATE users SET FrendRequest =%s WHERE UserName = %s"

    
    cursor = mysql.connection.cursor()

    

    cursor.execute(query ,(session["username"]+"," ,UserName ))
    mysql.connection.commit()

    cursor.close()

    flash("Arkadaşlık isteği başarıyla gönderildi" ,"success")
    return redirect(url_for("frendFind"))



@app.route("/FrendRequestDelete-<string:UserName>")
@login_required
def FrendRequestDelete(UserName):


    query_first = "SELECT FrendRequest FROM users WHERE UserName = %s"   

    cursor = mysql.connection.cursor()

    cursor.execute(query_first ,(UserName,))

    FrendRequest = cursor.fetchone()

    Requests = FrendRequest["FrendRequest"].split(",")


    NewRequests = list()

    for Request in Requests :
        if Request != session["username"]:
            
            NewRequests.append(Request+",")


    text = ""
    for NewRequest in NewRequests:
        text += NewRequest


        


    query_second = "UPDATE users set FrendRequest = %s WHERE UserName = %s"

    cursor.execute(query_second ,(text ,UserName))
    mysql.connection.commit()
    cursor.close()
    flash("Arkadaşlık isteğiniz geri çekildi")
    return redirect(url_for("frendFind"))




@app.route("/LoginAdmin" ,methods = ["GET" ,"POST"])
def LoginAdmin():


    if request.method == "GET":
        return render_template("LoginAdmin.html")


    else:

        UserName = request.form.get("username")
        Password = request.form.get("pass")

        query = "SELECT * FROM users WHERE UserName = %s"

        
        cursor = mysql.connection.cursor()

        feedback = cursor.execute(query, (UserName,))

        if feedback > 0:
            data = cursor.fetchone()
            RealPassword = data["Password"]

            if sha256_crypt.verify(Password ,RealPassword):
                session["username"] = UserName
                session["login"] = True
                flash("Giriş başarılı..." ,"success")
                return redirect(url_for("index"))

            else: 
                flash("Hatalı Parola..." ,"danger") 
                return redirect(url_for("LoginAdmin"))           
        else: 
            flash("Böyle bir kullanıcı bulunmuyor" ,"warning")
            return redirect(url_for("LoginAdmin"))

"""
@app.route("MeProfile")
@login_required
def MeProfile():
    query = "SELECT * FROM users WHERE UserName = %s"

    cursor = mysql.connection.cursor()

    cursor.execute(query , (session["username"],))

    user = cursor.fetchone()
    return render_template("MeProfile.html" ,user = user)"""

if __name__ == "__main__":
    app.run(debug=True)
