from flask import Flask, jsonify
import csv

app = Flask(__name__)

# Função para carregar eventos do CSV
def load_events_from_csv():
    events = []
    
    with open('linea_tiempo2.csv', mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')  # Define ';' como delimitador
        
        for row in csv_reader:


            event = {
                "start_date": {
                    "year": int(row["start_year"])
                },
                "end_date": {
                    "year": int(row["end_year"])
                },
                "text": {
                    "headline": row["title"],
                    "text": row["text"]
                },
                "media": {
                     "url": row["media"]
                },

            }
            events.append(event)
    
    return events



# Rota que retorna os eventos em formato JSON, incluindo o título principal da timeline
@app.route("/timeline")
def get_timeline():
    events = load_events_from_csv()
    timeline_data = {
            "title": {
            "media": {
                "url": "",  # Pode adicionar uma imagem de fundo aqui, se quiser
                "caption": "Historia de Galicia",
                "credit": "Fuente: Documentos Históricos"
            },
            "text": {
                "headline": "Historia Medieval Gallego-Portuguesa",
                "text": "<p>Una línea del tiempo sobre los eventos más importantes en la historia de Galicia, desde la época romana hasta la Edad Media.</p>"
            }
        },
        "events": events
    }
    
    return jsonify(timeline_data)

if __name__ == "__main__":
    app.run(debug=True)