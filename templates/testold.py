{% extends "base.html" %}

{% block content %}
<h1 style="color: grey">{{session['userName']}}</h1>
<div class="jumbotron">
  <h1>This is the riddle: {{session['riddle']}}<br>index Counter {{session['counter']}}</h1>
</div>
<div class="jumbotron">
  <form method="POST" name="InfoForm" action="">
        {{ form.hidden_tag() }}
        {{ form.answer.label}} {{form.answer}}
        {{form.submit()}}
  </form>
  <h4>this is your last answer: {{session['userInput']}}</h4>
  <h4>Score:  {{session['score']}}</h4>
  <p>
    {{session[wronganswer]}}
  </p>
</div>


{% endblock %}