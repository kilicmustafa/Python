from flask import Flask ,render_template,request
import requests

app = Flask(__name__)
url = "http://data.fixer.io/api/latest?access_key=9819cea4d566b30b7c6d5ef9e6e91fe7"

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") # USD
        secondCurrency = request.form.get("secondCurrency") # TRY

        amount = request.form.get("amount") # 15


        
        response = requests.get(url)
        app.logger.info(response)

        infos =  response.json()

        app.logger.info(infos)

        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue / firstValue) * float(amount)

        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result


        return render_template("index.html" ,info = currencyInfo)





    else:
        return render_template("index.html")



    
    



if __name__ == "__main__":
    app.run(debug=True)


