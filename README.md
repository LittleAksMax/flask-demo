# flask-demo
> $ sudo pip install flask

can put parameters into html with {{}}, have to name the expressions and pass them in render_template()
can run certain python in this format
``` python
{% for _ in range(1, 10)  %}
    <p> {{_}} </p>
{% endfor %}
```
But you have to end it with the appropriate end 

You can get certain tools from bootstrap, stuff to do in base.html.
Can also make base html and make everything inherit from it, you can fill it with blocks that need filling for things that need to change. Very good for no duplicate code.