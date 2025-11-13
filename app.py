from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # --- IMPORTANTE ---
    # Coloque aqui o nome EXATO do seu arquivo CSV
    # (Aquele que você subiu para o GitHub no Passo 2)
    # Pela análise que fiz, o nome dele é 'dados.csv.csv'
    file_name = 'dados.csv' 

    try:
        # Lê o arquivo CSV que está NA MESMA PASTA do app.py
        # Pela análise que fiz, o seu arquivo usa VÍRGULA (,) como separador
        df = pd.read_csv(file_name, sep=',') 
        
    except FileNotFoundError:
        # Mensagem de erro se o arquivo não for encontrado no repositório
        return "<h1>Erro: Arquivo CSV não encontrado!</h1><p>Verifique se o arquivo '{}' está no repositório.</p>".format(file_name)
    except Exception as e:
        # Outro erro (ex: separador errado)
        return "<h1>Erro ao ler o CSV</h1><p>{}</p>".format(e)

    # Renderiza o template, passando a tabela HTML
    # (Vou assumir que o template se chama 'display.html', que deve estar no projeto original)
    return render_template('display.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
