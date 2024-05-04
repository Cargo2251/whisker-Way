from flask import render_template, Blueprint
from supabase import create_client, Client
import os
from dotenv import load_dotenv

views = Blueprint('views', __name__)
load_dotenv()


@views.route('/')
def index():

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    response = supabase.table('ActivityLog').select("*").execute()
    return render_template('index.html', data=response.data)
