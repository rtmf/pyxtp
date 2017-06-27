#!/usr/bin/env python3
# vim: ts=2 sw=2 noet
import xtp
items				= [
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
		{ "name"		: "telepresence rig",
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
		]
categories	= [
		{ "name"		: "antbot",
			"title"		: "Antbot" },
		{ "name"		: "renegade",
			"title"		: "Renegade" },
		{ "name"		: "truckbot",
			"title"		: "Truckbot" },
		{ "name"		: "rsv",
			"title"		: "RSV" },
		]
menu				= [
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
		]
templates		= {
		"dtd"				: """
			<!doctype html>
		""",
		"html"			: """
			<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
			<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
			<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
			<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
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
					<template name="header" />
					<template name="items" />
			</body>
		""",
		"index"		: """
			<template name="dtd" />
			<template name="html">
			<template name="head" />
			<template name="body" />
			</html>
		""",
		"items"		:	"""
			<section>
				<div id="st-trigger-effects" class="column">
					<button data-effect="st-effect-7">filter robots</button>
				</div>
				<ul class="products-list">
					<foreach list="items" name="item" />
				</ul>
			</section>
		""",
		"item"		: """
			<li class="${class}" name="${name}">
				<div class="single-product">
					<a href="#">
						<img src="img/${name}.jpeg">	
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
			<div class="st-content"><!-- this is the wrapper for the content -->
				<div class="st-content-inner"><!-- extra div for emulating position:fixed of the menu -->
					<!-- Top Navigation -->
					<header id="header">
						<div class="header-content clearfix">
							<a class="logo" href="http://robots-everywhere.com/re_site/"><img  src="img/robots-everywhere.png"> <span>ROBOTS EVERYWHERE</span></a>
							<nav class="navigation" role="navigation">
								<ul class="primary-nav">
									<foreach subtemp="first" sublist="yes" name="menuitem" list="menu" />
								</ul>
							</nav>
						<a href="#" class="nav-toggle">Menu<span></span></a>
					</div><!-- header content -->
				</header><!-- header -->
			</div>
		""",
		"header"	:	"""
			<div id="st-container" class="st-container">
			<!-- content push wrapper -->
			<div class="st-pusher">
				<template name="filters" />
				<template name="menu" />
						<div class="store-header">
				<h1>Page Title</h1>
				<h2>Lorem ipsum dolor sit amet</h2>
			</div>
		""",
		
}
