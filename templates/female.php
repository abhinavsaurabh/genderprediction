{% extends "layout.html" %}
{% block title %}gender-detect{% endblock %}
{% block content %}
<div class="site-wrapper">
    <div class="site-wrapper-inner">
        <div class="cover-container">
            <div class="inner cover">
            <h1 class="cover-heading" style="font-size: 80px; font-family: Lato !important;"><p id="out"></p><strong></strong></h1>
            <?php
            include 'index.html';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // collect value of input field
    $name = $_REQUEST['query'];
  
        echo $name ;
    }
?>
            <p class="lead"><h3>You are a <font color="pink">Female</font></h3></p>
            <div class="container">
              <div class="row">
                    <div class="col-md-6" style="margin: 0 50px">
                        <div id="custom-search-input">
                            <div class="input-group col-md-12">
                                <form name= "myform" action="/search" method="POST"><input type="text" name="query" class="form-control input-lg" placeholder="Try your name" /></form>
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