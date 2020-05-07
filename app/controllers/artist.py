from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

from app import db
from app.models import Artist
from app.forms import ArtistForm

class controller(object):

    @staticmethod
    def create_form_page():
        """Returns the rendered page for creating an Artist"""

        form = ArtistForm()

        return render_template(
            'artist/forms/new.html',
            form=form
        )

    @staticmethod
    def create_action(kwargs=None):
        """Creates an Artist"""

        try:

            if not kwargs:

                form = ArtistForm(request.form)

                kwargs = {
                    "name" : form.name.data,
                    "genres" : form.genres.data,
                    "city" : form.city.data,
                    "phone" : form.phone.data,
                    "state" : form.state.data,
                    "facebook_link" : form.facebook_link.data,
                    "image_link" : form.image_link.data,
                    "website" : form.website.data,
                    "seeking_venue" : form.seeking_venue.data,
                    "seeking_description" : form.seeking_description.data
                }

            model = Artist(**kwargs)

            db.session.add(model)
            db.session.commit()

            flash('Artist ' + request.form['name'] + ' was successfully listed!')

            return redirect(url_for('artist.detail_page', artist_id=model.id))

        except:

            flash('An error occurred. Artist ' + form.name + ' could not be listed.')

        return render_template('artist/pages/list.html')

    @staticmethod
    def edit_form_page(id):
        """Returns the rendered page for editing an Artist"""

        form = ArtistForm(request.form)

        artist = Artist.query.filter(Artist.id == id).first_or_404()

        form.state.process_data(artist.state)
        form.genres.process_data(artist.genres)

        return render_template(
            'artist/forms/edit.html',
            form=form,
            artist=artist
        )

    @staticmethod
    def edit_action(id, kwargs=None):
        """Edit an Artist"""

        try:
            if not kwargs:

                form = ArtistForm(request.form)

                kwargs = {
                    "name" : form.name.data,
                    "genres" : form.genres.data,
                    "city" : form.city.data,
                    "phone" : form.phone.data,
                    "state" : form.state.data,
                    "facebook_link" : form.facebook_link.data,
                    "image_link" : form.image_link.data,
                    "website" : form.website.data,
                    "seeking_venue" : form.seeking_venue.data,
                    "seeking_description" : form.seeking_description.data
                }

            Artist.query.filter(Artist.id == id).update(kwargs)

            db.session.commit()

            flash('Artist ' + form.name.data + ' was successfully edited!')

        except:

            flash('An error occurred. Artist ' + form.name + ' could not be listed.')

        return redirect(url_for('artist.detail_page', artist_id=id))

    @staticmethod
    def detail_page(id):
        """Returns the rendered page of a Artist detail"""

        model = Artist.query.filter(Artist.id == id).first_or_404()

        return render_template(
            'artist/pages/detail.html',
            artist=model
        )

    @staticmethod
    def list_page():
        """Returns the rendered page of a list of Artist records"""

        models = Artist.query.all()

        return render_template(
            'artist/pages/list.html',
            artists=models
        )

    @staticmethod
    def search_page(search=None):
        """Returns the rendered page of a list of Artist search records"""

        if not search:
            search = request.form.get('search_term', '')

        models = Artist.query.filter(Artist.name.ilike("%" + search + "%")).all()

        results = {
            "count": len(models),
            "data": [model for model in models]
        }

        return render_template(
            'artist/pages/search.html',
            results=results,
            search_term=search
        )

    @staticmethod
    def autocomplete_name_json(search=None):
        """Returns a json list of Artist names for autocomplete"""

        if not search:
            search = request.form.get('term', '')

        models = Artist.query.filter(Artist.name.ilike("%" + search + "%")).all()

        return jsonify([model.name for model in models])
