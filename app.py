from flask import Flask, render_template

app = Flask(__name__)

sonlar = [14, 8, 33, 5, 71, 22, 9, 46]
maxi = max(sonlar)
mini = min(sonlar)
summ = sum(sonlar)
orta = summ/len(sonlar)

@app.route("/")
def sonlar():
    return render_template(
        'statistika.html', maxi=maxi, 
        mini=mini, summ=summ, orta=orta)





if __name__ == '__main__':
    app.run(debug=True)
