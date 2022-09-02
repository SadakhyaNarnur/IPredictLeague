from prediction import predict
from flask import Flask, render_template, request, flash
import os
pic=os.path.join('static\\images','team_logo')
app = Flask(__name__)
app.config['SECRET_KEY'] = pic



@app.route('/', methods=['POST', 'GET'])
def get_data():
    return render_template('index.html')

@app.route('/index.html', methods=['POST', 'GET'])
def home():
    return render_template('index.html')
@app.route('/csk.html', methods=['POST', 'GET'])
def csk():
    return render_template('csk.html')
@app.route('/msd.html', methods=['POST', 'GET'])
def msd():
    return render_template('msd.html')
@app.route('/imran.html', methods=['POST', 'GET'])
def imran():
    return render_template('imran.html')
@app.route('/scott.html', methods=['POST', 'GET'])
def scott():
    return render_template('scott.html')
@app.route('/sam.html', methods=['POST', 'GET'])
def sam():
    return render_template('sam.html')
@app.route('/david.html', methods=['POST', 'GET'])
def david():
    return render_template('david.html')
@app.route('/murali.html', methods=['POST', 'GET'])
def murali():
    return render_template('murali.html')
@app.route('/jadeja.html', methods=['POST', 'GET'])
def jadeja():
    return render_template('jadeja.html')
@app.route('/deepak.html', methods=['POST', 'GET'])
def deepak():
    return render_template('deepak.html')
@app.route('/raina.html', methods=['POST', 'GET'])
def raina():
    return render_template('raina.html')
@app.route('/km.html', methods=['POST', 'GET'])
def km():
    return render_template('km.html')
@app.route('/shardul.html', methods=['POST', 'GET'])
def shardul():
    return render_template('shardul.html')
@app.route('/dhruv.html', methods=['POST', 'GET'])
def dhruv():
    return render_template('dhruv.html')
@app.route('/mohit.html', methods=['POST', 'GET'])
def mohit():
    return render_template('mohit.html')
@app.route('/faf.html', methods=['POST', 'GET'])
def faf():
    return render_template('faf.html')
@app.route('/bravo.html', methods=['POST', 'GET'])
def bravo():
    return render_template('bravo.html')
@app.route('/karn.html', methods=['POST', 'GET'])
def karn():
    return render_template('karn.html')
@app.route('/watson.html', methods=['POST', 'GET'])
def watson():
    return render_template('watson.html')
@app.route('/rayudu.html', methods=['POST', 'GET'])
def rayudu():
    return render_template('rayudu.html')
@app.route('/bajji.html', methods=['POST', 'GET'])
def bajji():
    return render_template('bajji.html')
@app.route('/jadhav.html', methods=['POST', 'GET'])
def jadhav():
    return render_template('jadhav.html')
@app.route('/mitchell.html', methods=['POST', 'GET'])
def mitchell():
    return render_template('mitchell.html')

@app.route('/dc.html', methods=['POST', 'GET'])
def dc():
    return render_template('dc.html')
@app.route('/kkr.html', methods=['POST', 'GET'])
def kkr():
    return render_template('kkr.html')
@app.route('/mi.html', methods=['POST', 'GET'])
def mi():
    return render_template('mi.html')
@app.route('/srh.html', methods=['POST', 'GET'])
def srh():
    return render_template('srh.html')
@app.route('/rr.html', methods=['POST', 'GET'])
def rr():
    return render_template('rr.html')
@app.route('/punjab.html', methods=['POST', 'GET'])
def punjab():
    return render_template('punjab.html')
@app.route('/ra.html', methods=['POST', 'GET'])
def ra():
    return render_template('ra.html')
@app.route('/ma.html', methods=['POST', 'GET'])
def ma():
    return render_template('ma.html')
@app.route('/ass.html', methods=['POST', 'GET'])
def ass():
    return render_template('ass.html')
@app.route('/mash.html', methods=['POST', 'GET'])
def mash():
    return render_template('mash.html')
@app.route('/samc.html', methods=['POST', 'GET'])
def samc():
    return render_template('samc.html')
@app.route('/harb.html', methods=['POST', 'GET'])
def harb():
    return render_template('harb.html')
@app.route('/mois.html', methods=['POST', 'GET'])
def mois():
    return render_template('mois.html')
@app.route('/sfk.html', methods=['POST', 'GET'])
def sfk():
    return render_template('sfk.html')
@app.route('/man.html', methods=['POST', 'GET'])
def man():
    return render_template('man.html')
@app.route('/dm.html', methods=['POST', 'GET'])
def dm():
    return render_template('dm.html')
@app.route('/mohs.html', methods=['POST', 'GET'])
def mohs():
    return render_template('mohs.html')
@app.route('/mur.html', methods=['POST', 'GET'])
def mur():
    return render_template('mur.html')
@app.route('/kn.html', methods=['POST', 'GET'])
def kn():
    return render_template('kn.html')
@app.route('/np.html', methods=['POST', 'GET'])
def np():
    return render_template('np.html')

@app.route('/punjab.html', methods=['POST', 'GET'])
def ppp():
    return render_template('punjab.html')
@app.route('/cg.html', methods=['POST', 'GET'])
def cg():
    return render_template('cg.html')
@app.route('/vk.html', methods=['POST', 'GET'])
def vk():
    return render_template('vk.html')
@app.route('/rcb.html', methods=['POST', 'GET'])
def rcb():
    return render_template('rcb.html')
@app.route('/dinesh karthick.html', methods=['POST', 'GET'])
def dkk():
    return render_template('dinesh karthick.html')

@app.route('/carlos.html', methods=['POST', 'GET'])
def carl():
    return render_template('carlos.html')

@app.route('/Cariappa.html', methods=['POST', 'GET'])
def cappa():
    return render_template('Cariappa.html')

@app.route('/piyush chawla.html', methods=['POST', 'GET'])
def pch():
    return render_template('piyush chawla.html')

@app.route('/predict.html', methods=['POST', 'GET'])
def pred():
    return render_template('predict.html')






def res():
    return render_template('predict.html')
    '''if request.method == 'POST':
        home_team = request.form['homeTeam']
        away_team = request.form['awayTeam']
        city = request.form['city']
        toss_winner = request.form['tossWinner']
        toss_decision = request.form['selector1']
        print(home_team, away_team, city, toss_winner, toss_decision)
        winner_team = predict(home_team, away_team, city, toss_winner, toss_decision).__str__()
        print("Winning Team is -> " + winner_team)
        home_team_name = convert_back_to_team_names(home_team).__str__()
        away_team_name = convert_back_to_team_names(away_team).__str__()
        winner=os.path.join(app.config['SECRET_KEY'],winner_team+'.jpg')
        flash("Match Prediction between " + home_team_name + " and " + away_team_name + " : ")
        flash("Winner:")
        flash(winner_team)
    
        #winner = 'C:\\Users\\jaravin1\\Desktop\\ipl\\IPL-ML-2018-master\\IPL-ML-2018-master\\static\\images\\team_logo'+winner_team+'.jpg'
    #return render_template('index.html')'''
    
@app.route('/submit', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        home_team = request.form['homeTeam']
        away_team = request.form['awayTeam']
        city = request.form['city']
        toss_winner = request.form['tossWinner']
        toss_decision = request.form['selector1']
        print(home_team, away_team, city, toss_winner, toss_decision)
        winner_team = predict(home_team, away_team, city, toss_winner, toss_decision).__str__()
        print("Winning Team is -> " + winner_team)
        home_team_name = convert_back_to_team_names(home_team).__str__()
        away_team_name = convert_back_to_team_names(away_team).__str__()
        winner=os.path.join(app.config['SECRET_KEY'],winner_team+'.jpg')
        flash("Match Prediction between " + home_team_name + " and " + away_team_name + " : ")
        flash("Winner:")
        flash(winner_team)
    return render_template('predict.html',winner1=winner)


@app.route('/team.html', methods=['POST', 'GET'])
def team():
    return render_template('team.html')

@app.route('/top.html', methods=['POST', 'GET'])
def top():
    return render_template('top.html')

@app.route('/record.html', methods=['POST', 'GET'])
def record():
    return render_template('record.html')
def convert_back_to_team_names(team):
    team_name = ""

    if team == 'Kolkata':
        team_name = "KKR"
    if team == "Bangalore":
        team_name = "RCB"
    if team == "Pune":
        team_name = "CSK"
    if team == "Jaipur":
        team_name = "RR"
    if team == "Delhi":
        team_name = "DD"
    if team == "Dharamshala":
        team_name = "KXIP"
    if team == "Hyderabad":
        team_name = "SRH"
    if team == "Mumbai":
        team_name = "MI"

    return team_name


if __name__ == '__main__':
    app.run()
