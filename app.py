from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        content = request.form['content']
        author = request.form['author']

        try:
            cur = mysql.connection.cursor()
            query = """
                INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(query, (name, date_of_birth, date_of_death, content, author))
            mysql.connection.commit()
            cur.close()

            flash('Obituary successfully submitted!', 'success')
            return redirect(url_for('obituaries_list'))
        except Exception as e:
            flash(f"An error occurred: {e}", 'error')

    return render_template('obituary_form.html')

@app.route('/obituaries_list')
def obituaries_list():
    try:
        cur = mysql.connection.cursor()
        query = "SELECT * FROM obituaries"
        cur.execute(query)
        obituaries = cur.fetchall()
        cur.close()
        return render_template('obituaries_list.html', obituaries=obituaries)
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
