from django.shortcuts import redirect


def candidate_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_candidate:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('access_denied')

    return wrapper


def employee_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_employee:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('access_denied')

    return wrapper
