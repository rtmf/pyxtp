JS = \
		 js/bootstrap.js \
		 js/filter.js \
		 js/form.js \
		 js/jquery.js \
		 js/main.js \
		 js/modernizr.js \
		 js/sidebarEffects.js 
CSS = \
			css/animate.min.css \
			css/bootstrap.min.css \
			css/filter.css \
			css/style.css 
IMG = \
			img/products/laser-3.5W.jpeg \
			img/products/laser-7.8W.jpeg \
			img/products/telepresence-rig.jpeg \
			img/products/minimodem.jpeg \
			img/products/laser-5.6W.jpeg \
			img/products/antbot-full.jpeg \
			img/products/spectroscope.jpeg \
			img/products/renegade-full.jpeg \
			img/products/antbot-board.jpeg \
			img/robots-everywhere.png \
			img/dot.png \
			img/robots-everywhere-logo.jpeg \
			img/robots-everywhere-hero-grigio.jpg \
			img/robots-everywhere-footer.png \
			img/favicon.ico
SOURCE = resite.py xtp.py
STATIC = $(JS) $(CSS) $(IMG)

resite.zip: index.html $(STATIC)
	zip $@ $^

index.html: $(SOURCE) $(STATIC)
	/usr/bin/env python3 resite.py > $@

