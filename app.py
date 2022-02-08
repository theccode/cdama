import os
from app import create_app 
app = create_app(os.getenv('CDAMA_CONFIG') or 'default')

# @app.shell_context_processor
# def make_shell_context():
#     return None