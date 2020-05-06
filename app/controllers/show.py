from flask import Blueprint, render_template, request, flash, redirect, url_for
import datetime

from app import db
from app.forms import ShowForm
from app.models import Show, Artist, Venue


class controller:

    @staticmethod
    def create_action(kwargs={}):


        try:
            if not kwargs:
                
                form = ShowForm(request.form)

                venue = Venue().query.filter(Venue.name == form.venue_id.data).first()
                artist = Artist().query.filter(Artist.name == form.artist_id.data).first()

                kwargs = {
                    "venue_id" : venue.id,
                    "artist_id" : artist.id,
                    "start_time" : datetime.datetime.strptime(
                        "{} {}".format(request.form.get('start_date',''), request.form.get('start_time','')), "%b %d, %Y %H:%M %p"
                    )
                }

            model = Show(**kwargs)

            db.session.add(model)
            db.session.commit()

            flash('Show was successfully listed')

            return redirect(url_for('show.list_page', venue_id=model.id))

        except:

            flash('Whoops. Show could not be listed.')

            return redirect(url_for('show.create_form_page'))

    @staticmethod
    def create_form_page():

        form = ShowForm()

        return render_template(
            'show/forms/new.html',
            form=form
        )

    @staticmethod
    def list_page():

        data = []

        models = Show.query.all()

        for show in models:

            data.append({
                "venue_id" : show.venue.id,
                "venue_name" : show.venue.name,
                "artist_id" : show.artist.id,
                "artist_name" : show.artist.name,
                "artist_image_link" : show.artist.image_link,
                "start_time" : show.start_time.strftime("%m/%d/%Y, %H:%M")
            })

        return render_template(
            'show/pages/shows.html',
            shows=data
        )
