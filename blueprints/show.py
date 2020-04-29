from flask import Blueprint, render_template, request, flash

from app import db
from forms import ShowForm
from models import Show

show = Blueprint('show', __name__)

@show.route('/shows')
def shows():

    data = []

    models = Show.query.all()

    for show in models:

        data.extend([{
            "venue_id" : show.venue.id,
            "venue_name" : show.venue.name,
            "artist_id" : show.artist.id,
            "artist_name" : show.artist.name,
            "artist_image_link" : show.artist.image_link,
            "start_time" : show.start_time.strftime("%m/%d/%Y, %H:%M")
        }])

    return render_template(
        'show/pages/shows.html',
        shows=data
    )

@show.route('/shows/create')
def create_shows():

    form = ShowForm()

    return render_template(
        'show/forms/new_show.html',
        form=form
    )

@show.route('/shows/create', methods=['POST'])
def create_show_submission():

    try:

        form = ShowForm(request.form)

        kwargs = {
            "venue_id" : form.venue_id.data,
            "artist_id" : form.artist_id.data,
            "start_time" : form.start_time.data
        }

        model = Show(
            **kwargs
        )

        db.session.add(model)
        db.session.commit()

        flash('Show was successfully listed')

    except:

        flash('An error occurred. Show could not be added')

    finally:

        db.session.close()

    return render_template('show/pages/shows.html')
