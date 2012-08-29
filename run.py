import os, fnmatch
from datetime import datetime

from markdown import markdown

from flask import Flask, Markup, render_template, abort

app = Flask(__name__)


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------


def format_post(item):
    bits = item.split('_', 1)

    date = datetime.strptime(bits[0], '%Y%m%d')
    title = bits[1].replace('_', ' ').replace('.md', '').title()
    slug = title.lower().replace(' ', '-')

    return {'date': date, 'title': title, 'slug': slug}


def get_post_dir():
    return os.path.dirname(os.path.abspath(__file__)) + '/templates/posts'
    

def get_post_items():
    items = os.listdir(get_post_dir())
    items.sort(reverse=True)
    return items


def get_posts():
    posts = []

    for item in get_post_items():
        if item[0] == '.':
            continue

        post = format_post(item)
        posts.append(post)

    return posts


# ---------------------------------------------------------------------------
# FILTERS
# ---------------------------------------------------------------------------


@app.template_filter('date_format')
def date_format(timestamp):
    def suffix(d):
        return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

    def custom_format(format, t):
        return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

    return custom_format('%B {S}, %Y', timestamp)


# ---------------------------------------------------------------------------
# ROUTES (VIEWS)
# ---------------------------------------------------------------------------


@app.route('/')
def index():
    return render_template('index.html', posts=get_posts())


@app.route('/page/<slug>')
def page(slug):
    try:
        clean_slug = slug.replace('-', '_')
        content = app.open_resource('templates/pages/%s.md' % clean_slug, 'r').read()
        content = Markup(markdown(content))

        title = slug.replace('-', ' ').title()
        return render_template('page.html', content=content, page_title=title)
    except Exception, e:
        abort(404)


@app.route('/post/<slug>')
def post(slug):
    try:
        clean_slug = slug.replace('-', '_')
        post = None
        
        for item in get_post_items():
            if fnmatch.fnmatch(item, '*_%s.md' % clean_slug):
                post = item
                break

        content = app.open_resource('templates/posts/%s' % post, 'r').read()
        content = Markup(markdown(content))

        title = format_post(post)['title']
        return render_template('post.html', content=content, page_title=title)
    except Exception, e:
        abort(404)


if __name__ == '__main__':
    app.run()
