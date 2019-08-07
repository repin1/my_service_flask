# -*- coding: utf-8 -*-


"""
    Making rout funcs for my service
"""
from flask import render_template, flash, redirect, url_for, request, session
# flask app
from app import app
# func for getting data from github
from app.get_data import get_data
# driver to add data to db
from app.dbdriver import add_repos_to_db



@app.route('/')
def index():
    # only redirect from root to /service
    return redirect(url_for('service'))


@app.route('/service', methods=['GET', 'POST'])
def service():
    session.pop('_flashes', None)
    name = ""
    """
        User use method post when he works with page form. He must put the name of git's user whom repos info he wants to watch
    """
    if request.method == "POST":
        if "Name" in request.form:
            name = request.form["Name"]
            if name != "":
                try:
                    request_result = get_data(name)
                except Exception:
                    request_result = ""
                session.pop('_flashes', None)
                flash("GETTING DATA FINISHED")
                if request_result == "":
                    return render_template('service.html', title="Enter user name", name=name)
                else:
                    add_repos_to_db(request_result)
                    return render_template('service.html', title="Enter user name", name=name,
                            request_result=request_result)

    return render_template('service.html', title="Enter user name", name=name)
