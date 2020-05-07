from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
import datetime

from app import db
from app.forms import VenueForm
from app.models import Venue, Show

class controller(object):

    @staticmethod
    def create_form_page():
        """Returns the rendered page for creating a Venue"""

        form = VenueForm()

        return render_template(
            'venue/forms/new.html',
            form=form
        )

    @staticmethod
    def create_action(kwargs={}):
        """Creates a Venue"""

        try:

            form = VenueForm(request.form)

            kwargs = {
                "name" : form.name.data,
                "city" : form.city.data,
                "state" : form.state.data,
                "address" : form.address.data,
                "phone" : form.phone.data,
                "genres" : form.genres.data,
                "facebook_link" : form.facebook_link.data,
                "image_link" : form.image_link.data,
                "website" : form.website.data,
                "seeking_talent" : form.seeking_talent.data,
                "seeking_description" : form.seeking_description.data
            }

            model = Venue(
                **kwargs
            )

            db.session.add(model)
            db.session.commit()

            flash('Venue ' + model.name + ' was successfully listed!')

            return redirect(url_for('venue.detail_page', venue_id=model.id))

        except:

            flash('Whoops. Venue ' + kwargs.get('name','') + ' could not be listed.')

            return redirect(url_for('venue.list_page'))

    @staticmethod
    def edit_form_page(id):
        """Returns the rendered page for editing a Venue"""

        try:

            venue = Venue.query.filter_by(id=id).first()

        except:

            return redirect(url_for('core.index_page'))

        form = VenueForm(request.form)
        form.state.process_data(venue.state)
        form.genres.process_data(venue.genres)

        return render_template(
            'venue/forms/edit.html',
            form=form,
            venue=venue
        )

    @staticmethod
    def edit_action(id, kwargs={}):
        """Edit a Venue"""

        try:
            if not kwargs:

                form = VenueForm(request.form)

                kwargs = {
                        "name" : form.name.data,
                        "city" : form.city.data,
                        "state" : form.state.data,
                        "address" : form.address.data,
                        "phone" : form.phone.data,
                        "genres" : form.genres.data,
                        "facebook_link" : form.facebook_link.data,
                        "image_link" : form.image_link.data,
                        "website" : form.website.data,
                        "seeking_talent" : form.seeking_talent.data,
                        "seeking_description" : form.seeking_description.data
                    }

            Venue.query.filter(Venue.id == id).update(kwargs)

            db.session.commit()

            flash('Venue' + form.name.data + ' was successfully updated!')

        except:

            flash('An error occurred. Venue ' + form.name.data + ' could not be updated.')

        return redirect(url_for('venue.edit_form_page', venue_id=id))

    @staticmethod
    def delete_action(id):
        """Deletes a Venue"""

        try:

            model = Venue.query.filter_by(id=id).first()

            db.session.delete(model)
            db.session.commit()

            flash('The venue has been removed together with all of its shows.')

            return redirect(url_for('venue.list_page'))

        except:

            flash('Whoops. It\'s not possible to delete this Venue')

            return redirect(url_for('venue.detail_page', venue_id=id))

    @staticmethod
    def detail_page(id):
        """Returns the rendered page of a Venue detail"""

        try:

            venue = Venue.query.filter_by(id=id).first()
            venue.past_shows = Show.query.filter( Show.start_time < datetime.datetime.now(), Show.venue_id == venue.id).all()
            venue.upcoming_shows = Show.query.filter( Show.start_time > datetime.datetime.now(), Show.venue_id == venue.id ).all()
            venue.past_shows_count = len(venue.past_shows)
            venue.upcoming_shows_count = len(venue.upcoming_shows)

            return render_template(
                'venue/pages/detail.html',
                venue=venue
            )

        except:

            return redirect(url_for('core.not_found_error_page'))

    @staticmethod
    def list_page():
        """Returns the rendered page of a list of Venue records"""

        try:

            areas = Venue.query.distinct(Venue.city, Venue.state).all()

            for area in areas:

                area.venues = [v for v in Venue.query.filter_by(city=area.city, state=area.state).all()]

            return render_template(
                'venue/pages/list.html',
                areas=areas
            )

        except:

            return redirect(url_for('core.server_error_page'))

    @staticmethod
    def search_page(search=None):
        """Returns the rendered page of a list of Venue search records"""

        if not search:

            search = request.form.get('search_term', '')

        venues = Venue.query.filter(Venue.name.ilike("%" + search + "%")).all()

        results = {
            "count": len(venues),
            "data": [venue for venue in venues]
        }

        return render_template(
            'venue/pages/search.html',
            results=results,
            search_term=search
        )

    @staticmethod
    def autocomplete_name_json(search=""):
        """Returns a json list of Venue names for autocomplete"""

        if not search:

            search = request.form.get('term', '')

        models = Venue.query.filter(Venue.name.ilike("%" + search + "%")).all()

        return jsonify([model.name for model in models])

    @staticmethod
    def autocomplete_hours_json(filter=""):
        """Returns a json list of show hours for autocomplete"""

        if not filter:

            filter = request.form.get('term', '')

        time = datetime.datetime.strptime("1970-01-01 00:00", "%Y-%m-%d %H:%M")
        end = datetime.datetime.strptime("1970-01-02 00:00", "%Y-%m-%d %H:%M")

        times = []

        while time < end:

            time_string = str(time.strftime("%-I:%M %p"))

            if time_string.startswith(filter):

                times.append(time_string)

            time += datetime.timedelta(minutes=30)

        return jsonify(times)
