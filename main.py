from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
API_KEY = '2f151d0fc4b9be61f32863baca136d71'
API_LINK = "https://api.themoviedb.org/3/search/movie"


class Form(FlaskForm):
    new_rating = StringField("Your Rating out of 10. eg 7.5", validators=[DataRequired()])
    new_review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Done")


class Add_form(FlaskForm):
    movie_title = StringField("Movie Title")
    add_movie = SubmitField("Add Movie")


db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6dozWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap5(app)
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(1000))
    img_url = db.Column(db.String(500))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(result)):
        result[i].ranking = len(result) - i
        # print(result[i].ranking)
    db.session.commit()
    return render_template("index.html", result=result)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = Form()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get_or_404(movie_id)
    if form.validate_on_submit():
        movie_selected.rating = form.new_rating.data
        movie_selected.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_selected, form=form)


@app.route("/delete", methods=["GET","POST"])
def delete():
    movie_id = request.args.get('id')
    movie_selected = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = Add_form()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        response = requests.get(API_LINK, params={"api_key": API_KEY, "query": movie_title})
        a = response.json()["results"]
        return render_template("select.html", title=a)
    return render_template("add.html", form=form)

@app.route('/find')
def find():
    movie_id = request.args.get('id')
    if movie_id:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params={"api_key": API_KEY})
        title = response.json()["original_title"]
        img_url = f"https://image.tmdb.org/t/p/original/{response.json()['poster_path']}"
        description = response.json()["overview"]
        year = response.json()["release_date"].split("-")[0]
        movies = Movie(title=title, img_url=img_url, description=description, year=year, rating=5, ranking=4, review="enjoy")
        db.session.add(movies)
        db.session.commit()
        # movie_selected = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar()
        # form = Form()
        # return render_template("edit.html", movie=movie_selected, form=form)
        return redirect(url_for('edit', id=movies.id))


if __name__ == '__main__':
    app.run(debug=True)
