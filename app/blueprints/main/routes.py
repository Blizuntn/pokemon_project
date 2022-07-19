from flask import render_template, redirect, url_for
from . import bp as app
from app.data.pokemon import pokemon_names, pokemon_types, pokemon_effects
from app.blueprints.main.models import Pokemon
from flask_login import login_required, current_user

names = pokemon_names
types = pokemon_types
effects = pokemon_effects


@app.route("/")

def home():
    if current_user.is_authenticated:
        return render_template('index.html',title="Pokemon", len=len(pokemon_names), PokemonNames=names, PokemonTypes=types, PokemonEffects=effects)
    return redirect(url_for("auth.login"))



