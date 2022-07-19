from flask import jsonify, request, redirect, render_template, flash, url_for
from . import bp as app
from app.blueprints.main.models import Pokemon, User
from app import db
from flask_login import current_user, login_required
from app.forms.forms import PokemonForm


@app.route("/new_pokemon", methods=["GET", "POST"])
@login_required
def new_pokemon():
    form = PokemonForm()
    if form.validate_on_submit():
        new_pokemon=Pokemon(name=form.pokemon_name.data,
                            description=form.pokemon_description.data,
                            type_=form.pokemon_type.data,
                            owner=current_user.public_id)
        db.session.add(new_pokemon)
        db.session.commit()
        flash("You have collected a pokemon", "success")
        return redirect(url_for("main.home"))
        
    return render_template("new_pokemon.html", title="Pokemon", form=form)