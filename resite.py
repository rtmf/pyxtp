#!/usr/bin/env python3
# vim: ts=2 sw=2 noet
import xtp
resite	= {
		"items"				: [
			{ "name"		: "laser-3.5W",
				"price"		: 195,
				"class"		: "laser",
				"title"		:	"",
				"desc"		:	"""
								""",
								},
			{ "name"		: "laser-5.6W",
				"price"		: 245,
				"class"		: "laser",
				"title"		:	"",
				"desc"		:	"""
								""",
								},
			{ "name"		: "laser-7.8W",
				"price"		: 275,
				"class"		: "laser",
				"title"		:	"",
				"desc"		:	"""
								""",
								},
			{ "name"		: "antbot-board",
				"price"		: 39,
				"class"		: "android-compatible arduino-droidbot-platform antbot-platform board component",
				"title"		:	"",
				"desc"		:	"""
								""",
								},
			{ "name"		: "antbot-full",
				"price"		: 199,
				"class"		: "android-compatible arduino-droidbot-platform antbot-platform robot",
				"title"		:	"",
				"desc"		:	"""
								""",
								},
			{ "name"		: "renegade-full",
				"price"		: 599,
				"class"		: "android-compatible arduino-heavy-droidbot-platform antbot-platform robot",
				"title"		:	"Renegade Rover aka TruckBot",
				"desc"		:	"""
			This massive beast is built around our Heavy Hybrid Motor Controller, a near drop-in replacement for the pololu motor driver at the heart of our classic arduino-backed droidbot platform capable of switching over twice the load at 1.21kW.
								""",
								},
			{ "name"		: "minimodem",
				"price"		: 14,
				"class"		: "android-compatible component",
				"title"		:	"",
				"desc"		:	"""
								""",
								},
			{ "name"		: "telepresence-rig",
					"price"		: 699,
					"class"		: "android-compatible propeller-droidbot-platform robot",
					"title"		:	"",
					"desc"		:	"""
								""",
								},
			{ "name"		: "spectroscope",
					"price"		: 299,
					"class"		: "",
					"title"		:	"",
					"desc"		:	"""
								""",
								},
			],
	"categories"	: [
			{ "name"		: "antbot",
				"title"		: "Antbot" },
			{ "name"		: "renegade",
				"title"		: "Renegade" },
			{ "name"		: "truckbot",
				"title"		: "Truckbot" },
			{ "name"		: "rsv",
				"title"		: "RSV" },
			],
	"menu"				: [
			[
				{
					"class"		: "menu-tendina",
					"link"		: "robots/",
					"title"		: "Robots",
					"template":	"tendina",
					},
				{
					"link"		: "robots/land/",
					"title"		: "Land",
					},
				{
					"link"		: "robots/sea/",
					"title"		: "Sea",
					},
				{
					"link"		: "robots/air/",
					"title"		: "Air",
					},
				{
					"link"		: "robots/space/",
					"title"		: "Space",
					},
				{
					"link"		: "robots/underwater/",
					"title"		: "Underwater",
					},
				],
			{
				"link"		: "data-loggers/",
				"title"		: "Automation",
				},
			{
				"link"		: "consulting/",
				"title"		: "Consulting",
				},
			{
				"link"		: "purchase/",
				"title"		: "Buy/Download",
				},
			{
				"link"		: "support/",
				"title"		: "Support",
				},
			{
				"link"		: "support/contact-us/",
				"title"		: "Contact us",
				},
			{
				"class"		: "label-social",
				"title"		: "Follow Us",
				},
			{
					"class"		: "social",
					"link"		: "#",
					"icon"		: "icon-youtube-play",
					},
			{
					"class"		: "social",
					"link"		: "#",
					"icon"		: "icon-facebook-official",
					},
			{
					"class"		: "social",
					"link"		: "#",
					"icon"		: "icon-linkedin",
					},
			],
	"templates"		: {
			"dtd"				: """
			<!doctype html>
			""",
			"html-for-ie"			: """
				<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
				<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
				<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
				<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
			""",
			"html"		  : """
				<html>
					${_}
				</html>
			""",
			"head"			: """
				<head>
					<meta charset="utf-8">
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<title>Nome pagina - Robots Everywhere</title>
					<link href='https://fonts.googleapis.com/css?family=Hind' rel='stylesheet' type='text/css'>
					<link href='https://fonts.googleapis.com/css?family=Roboto:400,500,700,900' rel='stylesheet' type='text/css'>
					<link href='https://fonts.googleapis.com/css?family=Roboto+Mono:400,700' rel='stylesheet' type='text/css'>
					<link rel="stylesheet" href="css/bootstrap.min.css">
					<link rel="stylesheet" href="css/animate.min.css">
					<!--<link rel="stylesheet" href="css/main.css">-->
					<link rel="stylesheet" href="css/style.css">
					<link rel="stylesheet" type="text/css" href="css/filter.css" />
					<!--<link rel="stylesheet" href="css/responsive.css">-->
					<script src="http://use.fonticons.com/dc00d20b.js"></script>
					<link rel="shortcut icon" href="http://robots-everywhere.com/re_site/wp-content/uploads/2012/02/favicon.ico"/>
				</head>
			""",
			"body"		:	"""
				<body>
					<div id="st-container" class="st-container">
						<div class="st-pusher">
							<template name="filters" />
							<div class="st-content"><!-- this is the wrapper for the content -->
								<template name="header" />
								<template name="items" />
								<template name="contact" />
								<template name="footer" />
							</div><!-- /st-content -->
						</div><!-- /st-pusher -->
					</div><!-- /st-container -->	
					<template name="js" />
				</body>
			""",
			"js"			: """
				<script src="js/jquery.js"></script>
				<script>window.jQuery || document.write('<script src="js/jquery.min.js"><\/script>')</script>
				<script src="js/bootstrap.js"></script>
				<!--<script src="js/retina.min.js"></script>-->
				<script src="js/modernizr.js"></script>
				<script src="js/main.js"></script>  
				<script src="js/filter.js"></script>
				<script src="js/sidebarEffects.js"></script>
				<script src="js/form.js"></script>
			""",
			"index"		: """
				<template name="dtd" />
				<template name="html">
					<template name="head" />
					<template name="body" />
				</template>
			""",
			"items"		:	"""
				<section>
					<div id="st-trigger-effects" class="column">
						<button data-effect="st-effect-7">filter robots</button>
					</div><!-- st-trigger-effects .column -->
					<ul class="products-list">
						<foreach list="items" name="item" />
					</ul>
				</section>
			""",
	"item"		: """
				<li class="${class}" name="${name}">
					<div class="single-product">
						<a href="#">
							<img src="img/products/${name}.jpeg">	
						</a>
					</div> <!-- .single-product -->
					<div class="info">
						<h3><a href="#">${title}</a></h3>
						<p>${desc}</p>
						<footer class="infobtn">
							<a class="btn btn-large" href="#contact" id="buy">buy</a>
							<a class="btn btn-large" href="#" target="_blank">info</a>
						</footer>
					</div> <!-- .info -->
				</li>
			""",
			"category": """
				<li class="filterbtn" id="${name}"><a href="#">${title}</a></li>
			""",
			"filters"	:	"""
				<!-- 	
					MENU - FILTER
				-->
				<nav class="st-menu st-effect-7" id="menu-7">
					<h2 class="icon icon-lab">What kind of robots do you wanna buy?</h2>
					<ul>
						<foreach list="categories" name="category" />
						<li class="filterbtn" id="all"><a href="#">View All</a></li>
					</ul>
				</nav>
			""",
			"menuitem-top": """
				<li ${class:+class="${class}"}>
					${link:+<a href="${link}">}
						${icon:+<i class="icon ${icon}"></i>}
						${title}
					${link:+</a>}
			""",
			"menuitem": """
				<template name="menuitem-top" />
				</li>
			""",
			"tendina"	: """
				<template name="menuitem-top" />
					<nav class="tendina">
						<ul>
							<foreach name="menuitem" list="itersublist" />
						</ul>
					</nav>
				</li>
			""",
			"menu"		: """
				<header id="header">
					<div class="header-content clearfix">
						<a class="logo" href="http://robots-everywhere.com/re_site/"><img  src="img/robots-everywhere.png"> <span>ROBOTS EVERYWHERE</span></a>
						<nav class="navigation" role="navigation">
							<ul class="primary-nav">
								<foreach subtemp="first" sublist="yes" name="menuitem" list="menu" />
							</ul>
						</nav>
						<a href="#" class="nav-toggle">Menu<span></span></a>
					</div><!-- header-content -->
				</header><!-- header -->
			""",
			"header"	:	"""
				<div class="st-content-inner"><!-- extra div for emulating position:fixed of the menu -->
					<template name="menu" />
				</div><!-- /st-content-inner -->
				<div class="store-header">
					<h1>Page Title</h1>
					<h2>Lorem ipsum dolor sit amet</h2>
				</div><!-- /store-header -->
			""",
			"contact"	: """
				<section id="contact">
					<h2>Contact us</h2>
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quam quam, commodo nec lacinia id, volutpat fermentum tortor.</p>
					<div id="contact_form">
						<form id="formcontact" class="cbp-mc-form" action="" name="contact"><!-- name="emailform" -->
							<div class="cbp-mc-column">
								<label for="first_name">Name</label>
								<input id="nomeinput" name="name" placeholder="Noel" type="text"><!--id="first_name"-->
								<label class="error" for="name" id="name_error" style="display: none;">Your name is required.</label>
								
								<label for="email">Email</label>
								<input id="emailinput" name="email" placeholder="noel.doe@gmail.com" type="text"><!--id="email"-->
								<label class="error" for="email" id="email_error" style="display: none;">Your email is required.</label>
															<label class="error" for="email" id="email_valid" style="display: none;">Your email is not valid.</label>
								
								<input class="trick" id="checkinput" name="check" placeholder="" type="text">
								<label class="error" for="check" id="trick_error" style="display: none;">You're a bot || SPAM.</label>
								
								<label for="msg">Any questions?</label>
								<textarea id="msginput" name="msg"></textarea><!--id="msg"-->
							</div><!-- .cbp-mc-column -->
							<div class="cbp-mc-submit-wrap">
								<input id="submitinput" class="cbp-mc-submit" value="Send" type="submit">
							</div><!-- .cbp-mc-submit-wrap -->
						</form>
					</div> <!-- end contact_form -->
				</section>
			""",
			"footer"	: """
				<footer>
					<div class="container">
						<div class="row">
							<div class="col-md-5 col-lg-5">
								<div class="brand">
									<div class="logo-footer">
										<img src="img/robots-everywhere-footer.png">
									</div><!-- .logo-footer -->
									<div class="content-footer">
										<span>Robots Everywhere</span><br>
										Lorem ispsum lorem ipsum lorem ipsum lorem 
			ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem 
			ipsum lorem ipsum.
									</div><!-- .content-footer -->
								</div><!-- .brand -->
							</div><!-- .col -->
							<div class="col-md-7 col-lg-7">
								<ul>
									<li><a href="http://robots-everywhere.com/re_site/consulting/">Consulting</a></li>
									<li><a href="http://robots-everywhere.com/re_site/blog/">Blog</a></li>
									<li><a href="http://robots-everywhere.com/re_site/support/">Support</a></li>
									<li><a href="http://robots-everywhere.com/re_site/support/contact-us/">Contact us</a></li>
								</ul>
								<ul>
									<li class="social"><a href="https://www.youtube.com/channel/UCwfCldqmzcFZkjjnZi_IHAw"><i class="icon icon-youtube-play icon-2x"></i></a></li>
									<li class="social"><a href="#"><i class="icon icon-facebook-official icon-2x"></i></a></li>
									<li class="social"><a href="#"><i class="icon icon-linkedin icon-2x"></i></a></li>
								</ul>
								<p class="result"></p>
							</div><!-- .col -->
						</div><!-- .row -->
					</div><!-- .container -->
				</footer>
			""",
	},
}

def render():
	print(xtp.TemplateEngine(**resite).render("index"))

if __name__ == '__main__':
	render()
