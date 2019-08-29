
from werkzeug.security import safe_str_cmp
from user import Users




users = {
    Users(1 , 'nifty' , 'noob457')

}


user_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}
# users ={
#
#     'id'=1,
#     'username'='nifty',
#     'password'='noob457'
# }
#
# user_mapping = {'nifty':{
#         'id'=1,
#         'username'='nifty',
#         'password'='noob457'
#     }
# }
#
# userid_mapping = {1:{
#     'id'=1,
#     'username'='nifty',
#     'password'='noob457'
# }}

def authenticate(username,password):
    user = user_mapping.get (username, None)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)
