from flask import Flask, render_template, request, jsonify
import sqlite3
import os



app = Flask(__name__)




@app.route('/')
def index(): 
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    posts = conn.execute('SELECT * FROM posts')
    return render_template('index.html', posts=posts)




@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    conn = sqlite3.connect('db/database.db')
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    return 'Message deleted succesfully'





@app.route('/api/items/', methods=['POST'])
def add_item():
    conn = sqlite3.connect('db/database.db')
    item = request.json['item']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (item) VALUES (?)", (item,))
    cursor.execute("SELECT last_insert_rowid()")
    conn.commit()
    item_id = cursor.fetchone()[0]
    return jsonify({'id': item_id, 'message': 'Message added succesfully'})