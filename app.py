from flask import Flask, render_template, request, jsonify
import sqlite3
import os



app = Flask(__name__)


def custom_render_template(template_name):
    with open(template_name, 'r', encoding='utf-8') as template_file:
        template = template_file.read()
    return template




@app.route('/')
def index(): 
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    posts = conn.execute('SELECT * FROM posts')
    return render_template('index.html', posts=posts)

@app.route('/doc')
def doc():
    return custom_render_template('templates/DOC.html')




@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    conn = sqlite3.connect('db/database.db')
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return 'Message deleted succesfully'





@app.route('/api/items/', methods=['POST'])
def add_item():
    conn = sqlite3.connect('db/database.db')
    item = request.json['item']
    #seleziona il database, e immagazzina il playload desiderato in una var

    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (item) VALUES (?)", (item,))
    cursor.execute("SELECT last_insert_rowid()")
    conn.commit()
    #crea un cursore per permettere più comandi sql insieme e commit everything

    item_id = cursor.fetchone()[0] 
    # sintassi utilizzata per recuperare una singola riga di risultati da una query SQL eseguita tramite un cursore.
    
    conn.close()
    return jsonify({'id': item_id, 'message': 'Message added succesfully'})
    
#ESEMPIO DI API CHE:
#ASCOLTA LA RICHIESTA MANDATA ALL'INDIRIZZO
#ITERA ATTRAVERSO UNA SELEZIONE PER RESTITUIRE UN DATO (in questo esempio in
    # realtà non itera ma l'accoppiata "SELECT last_insert_rowid()" è il
    # parallelo con $rows=mysqli_row())
#RESTITUISCE UNA RISPOSTA CHE VERRà ASCOLTATA DA JS