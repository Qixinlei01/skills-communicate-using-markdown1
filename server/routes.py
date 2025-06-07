from flask import Blueprint, request, jsonify
import mysql.connector

bp = Blueprint('routes', __name__)

@bp.route('/books_by_name/<name>')
def books_by_name(name):
    # 连接到数据库
    conn = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()

    # 使用参数化查询防止 SQL 注入
    query = "SELECT * FROM books WHERE name LIKE %s"
    cursor.execute(query, (name,))  # 第 16 行的修改
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results)

@bp.route('/books_by_author/<author>')
def books_by_author(author):
    # 连接到数据库
    conn = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()

    # 使用参数化查询防止 SQL 注入
    query = "SELECT * FROM books WHERE author LIKE %s"  # 第 22 行的修改
    cursor.execute(query, (author,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results)
