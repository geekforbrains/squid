Squid
=====

Squid is a static blog site generator built on Flask. One creates Markdown pages and posts and Squid maps those
files to routes. 

Squid was created as a pet project to play with and learn [Flask](http://flask.pocoo.org). It is not meant to be 
a full featured static site generator. If you're looking for something like that, check out [Octopress](http://octopress.org).


Installation
------------

To use Squid, you should first have [virtualenv](http://pypi.python.org/pypi/virtualenv) installed. If you don't, you can install it 
easily via `pip` or `easy_install`

    $ sudo pip install virtualenv

Once you have virtualenv installed, clone a copy of this repo. Make sure you're in the projects root directory and create a new environment.

    $ virtualenv env

This will create a directory named `env` with an isolated Python environment. To use it, run:

    $ source env/bin/activate

You can tell that you're in the virtual environment by the (env) at the beginning of your terminal. Now use `pip` to
install Flask and other requirments.

    $ pip install -r requirements.txt

Done! To launch the application, run:

    $ python run.py

You can now access your Squid install at [http://localhost:5000](http://localhost:5000).


Creating a Post
---------------

Creating a new post is easy. Make a new file in the `templates/posts/` directory. The filename must be in the following format:

    [YYYYMMDD]_my_first_post.md

The first part of the filename is the date in `YYYYMMDD` format. The second part of the filename is the title to be used, with the
words seperated by underscores. All letters must be lowercase. Lastly, the file must have the `.md` extension, which stands for "Markdown".

For example, lets say today is Feb 15th, 2012 and you want to create a post with the title "10 Reasons Why Eating Rainbow Cookies Wont
Make You A Magical Unicorn". You would create this file:

    20120215_10_reasons_why_eating_rainbow_cookies_wont_make_you_a_magical_unicorn.md

Squid automatically lists new posts on the front end of the site, and will map routes matching the post title. To access the post, you would 
go to (assuming you're running on localhost):

    http://localhost:5000/post/10-reasons-why-eating-rainbow-cookies-wont-make-you-a-magical-unicorn


Creating a Page
---------------

Creating a page is even easier than a post. Simply create a file in `templates/pages/` with the title of the page. Pages dont require
the date stamp at the beginning of the file.

    about_me.md

The above file would be accessible at:

    http://localhost:5000/page/about-me


Live Site
---------

I built Squid as a fun learning project, and ended up using it to run my blog. You can check out a live working copy
of Squid at http://geekforbrains.com


Planned Features
----------------

Below are a list of features I plan on adding in the future:

- Caching
- Portfolio/Photo Gallery


Credits
-------

Squid is built on and inspired by the software and tools below:

- [Flask](http://flask.pocoo.org)
- [Bootstrap](http://twitter.github.com/bootstrap)
- [Markdown](http://daringfireball.net/projects/markdown)
- [Octopress](http://octopress.org)

Gavin Vickery  
gavin@geekforbrains.com  
http://geekforbrains.com
