from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

SECRET_KEY = 'minha_senha' 
app.config['SECRET_KEY'] = SECRET_KEY

class Formulario(FlaskForm):
    altura = FloatField('altura', validators=[DataRequired()])
    largura = FloatField('largura', validators=[DataRequired()])
    tipoCortina =  SelectField(u'Tipo Curtina', choices=[('oxford','Oxford'), ('tergal: ','Tergal'), ('gabardine: ', 'Gabardine')])

@app.route("/", methods=["GET", "POST"])
def home():
    formulario = Formulario()
    if formulario.validate_on_submit():
        largura = formulario.largura.data
        altura = formulario.altura.data
        tipoCortina = formulario.tipoCortina.data
        metro_quadrado = altura * largura
        Oxford = metro_quadrado * 83
        Tergal = metro_quadrado * 62
        Gabardine = metro_quadrado * 105
       

        return ("Preços para orçamento: ") + ("<p>Oxford: ") + (str(Oxford)) + (" reais por m²") + ("<p>Tergal: ") + (str(Tergal)) + (" reais por m²") + ("<p>Gabardine: ") + (str(Gabardine)) + (" reais por m²")
    return render_template('home.html', form=formulario)





#Oxford: 83 reais por m²
#Tergal: 62 reais por m²
#Gabardine: 105 reais por m²