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
    tipoCortina =  SelectField(u'Tipo Curtina', choices=[('oxford','Oxford'), ('tergal','Tergal'), ('gabardine', 'Gabardine')])

@app.route("/", methods=["GET", "POST"])
def home():
    formulario = Formulario()
    if formulario.validate_on_submit():
        largura = formulario.largura.data
        altura = formulario.altura.data
        tipoCortina = formulario.tipoCortina.data
        metro_quadrado = altura * largura
        preco = 0
        if (tipoCortina == "oxford"):
            preco = metro_quadrado * 83
       
        if (tipoCortina == "tergal"):
            preco = metro_quadrado * 62
        
        if (tipoCortina == "gabardine"):
            preco = metro_quadrado * 105
            
        return ("<h2>Resultado da pesquisa:</h2>") + ("<p>O orçamento da cortina tipo  </p>" + tipoCortina.format()) + (" é de <b>R$ ") + str(preco)
    return render_template('home.html', form=formulario)


#Oxford: 83 reais por m²
#Tergal: 62 reais por m²
#Gabardine: 105 reais por m²