from app import create_app 
from app.models import User , Rig01 ,db 

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User , 'Rig01': Rig01 }
