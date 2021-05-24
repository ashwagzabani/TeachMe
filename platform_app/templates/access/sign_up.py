{% extends 'base_form.html' % }
{% load crispy_forms_tags % }
{% load static % }
{% block body % }

{% if title is 'Sign Up' % }
<p class = "login-card-description" > Craete your account now!< /p >

{% else % }
<p class = "login-card-description" > Sign into your account < /p >
{% endif % }

<form method = "POST" action = "." >
    {% csrf_token % }
    {{form | crispy}}

    {% if title is 'Sign Up' % }
    <button class = "btn btn-block login-btn mb-4" type = "submit" > REGISTER < /button >

    {% else % }
    <button class = "btn btn-block login-btn mb-4" type = "submit" > LOG IN < /button >
    {% endif % }

</form >
<div class = "border-bottom pt-3" >
    {% if title is 'Sign Up' % }
    <small class = "test-mute" >
    Do you Have an account? < a href = "{%url 'logIn'%}" > Log In < /a >
    </small >
    {% else % }
    <small class = "test-mute" >
    Need an account? < a href = "{%url 'signup'%}" > Sign Up < /a >
    </small >
    <br >
    <small class = "test-mute" >
    Forget your password? < a href = "{%url 'password_reset'%}" > Reset password < /a >
    </small >
    {% endif % }

</div >
{ % endblock % }
