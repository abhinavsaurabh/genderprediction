{% extends "layout.html" %}
{% block title %}gender-predict{% endblock %}
{% block content %}
<div class="site-wrapper">
 	<div class="site-wrapper-inner">
	    <div class="cover-container">
			<div class="inner cover">
            <h1 class="cover-heading" style="font-size: 80px; font-family: Lato !important;"><strong>gender</strong>-<strong>predict</strong></h1>
            <p class="lead">Determine gender from first name</p>
			<div class="container">
			  <div class="row">
			        <div class="col-md-6" style="margin: 0 50px">
			            <div id="custom-search-input">
			                <div class="input-group col-md-12">
			                    <form name= "myform" id="name" action="/search" method="POST"><input type="text" name="query" class="form-control input-lg" placeholder="Try your name" /></form>
			                    <?php
			                    require 'female.php';
			                    $name='query';
			                    ?>
			                    <span class="input-group-btn">
			                        <button class="btn btn-info btn-lg" type="button">
			                            <i class="glyphicon glyphicon-search"></i>
			                        </button>
			                    </span>
			                </div>
			            </div>
			        </div>
			  </div>
			</div>
			</div>
		</div>
	</div>
</div>
{% endblock %}