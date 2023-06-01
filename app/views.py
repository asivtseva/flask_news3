from flask import render_template, redirect

from .models import News, Category
from .forms import NewsForm
from . import app, db


@app.route('/')
def index():
    news = News.query.all()
    return render_template('index.html', news=news, categories=Category.query.all())


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = db.session.get(News, id)
    return render_template('news_detail.html', news=news, categories=Category.query.all())


@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    return render_template(
        'category.html',
        category_name=category.title,
        news=category.news,
        categories=Category.query.all()
    )



@app.route('/add_news', methods=['POST', 'GET'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        category = form.category.data
        news = News(title=title, text=text, category=category)
        db.session.add(news)
        db.session.commit()
        return redirect('/')
    return render_template('add_news.html', form=form, categories=Category.query.all())
