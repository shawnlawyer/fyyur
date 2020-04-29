from flask import Blueprint, render_template, request, flash, redirect, url_for

from app import db
from forms import ArtistForm
from models import Artist

artist = Blueprint('artist', __name__)

@artist.route('/artists')
def artists():
    models = Artist.query.all()
    return render_template(
        'artist/pages/list.html',
        artists=models
    )

@artist.route('/artists/search', methods=['POST'])
def search_artists():
    search = request.form.get('search_term', '')

    models = Artist.query.filter(Artist.name.ilike("%" + search + "%")).all()

    response = {
        "count": len(models),
        "data": [model for model in models]
    }

    return render_template(
        'artist/pages/search.html',
        results=response,
        search_term=search
    )

@artist.route('/artists/<int:artist_id>')
def show_artist(artist_id):

    model = Artist.query.filter(Artist.id == artist_id).first_or_404()

    return render_template('artist/pages/detail.html', artist=model)

@artist.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):

    form = ArtistForm(request.form)

    artist = Artist.query.filter(Artist.id == artist_id).first_or_404()

    form.state.process_data(artist.state)
    form.genres.process_data(artist.genres)

    return render_template(
        'artist/forms/edit_artist.html',
        form=form,
        artist=artist
    )

@artist.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):

    form = ArtistForm(request.form)

    try:

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

        Artist.query.filter(Artist.id == artist_id).update(kwargs)

        db.session.commit()

        flash('Artist ' + form.name.data + ' was successfully edited!')

    except:

        flash('An error occurred. Artist ' + form.name + ' could not be listed.')

    finally:

        db.session.close()

    return redirect(url_for('artist.show_artist', artist_id=artist_id))

@artist.route('/artists/create', methods=['GET'])
def create_artist_form():

    form = ArtistForm()

    return render_template(
        'artist/forms/new_artist.html',
        form=form
    )

@artist.route('/artists/create', methods=['POST'])
def create_artist_submission():

    try:
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

    except:

        flash('An error occurred. Artist ' + form.name + ' could not be listed.')

    finally:

        db.session.close()

    return render_template('artist/pages/list.html')
