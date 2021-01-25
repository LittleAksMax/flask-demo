# flask-demo
> $ sudo pip install flask

Can put parameters into html with {{}}, have to name the expressions and pass them in render_template()

Can run certain python in this format
``` python
{% for _ in range(1, 10)  %}
    <p> {{_}} </p>
{% endfor %}
```
But you have to end it with the appropriate end (in this case *endfor*)
