from flask import Flask,render_template, request
import requests

app = Flask(__name__)


url = "https://api.github.com/users/"

@app.route("/" ,methods=["GET" ,"POST"])
def index():


    if request.method == "POST":
        githubname= request.form.get("githubname")
        newurl = url + githubname

        response_user = requests.get(newurl)
        response_repos = requests.get(newurl+"/repos")



        app.logger.info(response_user)
        app.logger.info(response_repos)

        user_information = response_user.json()
        repos = response_repos.json()

        app.logger.info(user_information)
        app.logger.info(repos)


        if "messagge" in user_information:
            return render_template("index.html" ,error = "Böyle bir kullanıcı bulunamadı")

        else:
            return render_template("index.html" ,info = user_information ,repos = repos)
  
         

    else:

        return render_template("index.html")


    



if __name__ == "__main__":

    app.run(debug=True)

