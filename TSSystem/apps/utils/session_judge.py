#!/usr/bin/env python
# encoding: utf-8



def session_judge(request):
    if 'user_id' in request.session and 'user_type' in request.session:
        user_type = request.session['user_type']
    else:
        del request.session
        return True
    if str(user_type) != '3':
        del request.session
        return True
    else:
        return False


def session_judge_teacher(request):
    if 'user_id' in request.session and 'user_type' in request.session:
        user_type = request.session['user_type']
    else:
        del request.session
        return True
    if str(user_type) != '2':
        del request.session
        return True
    else:
        return False