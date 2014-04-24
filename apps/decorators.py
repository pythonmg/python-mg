#!/usr/bin/env python
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apps.membros.models import Member


def register_is_valid(function):
    @login_required
    def validate(request, *args, **kwargs):
        if not Member.objects.filter(user=request.user).exists():
            return redirect('register')
        else:
            return function(request, *args, **kwargs)
    return validate


class RegisterValidMixin(object):

    @method_decorator(register_is_valid)
    def dispatch(self, *args, **kwargs):
        return super(RegisterValidMixin, self).dispatch(*args, **kwargs)


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)
