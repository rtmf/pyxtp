# resite target's Makefile
LOSRCF = fodt
XTPFMT = $(LOSRCF)
MSFMTS = doc  \
				 docx \
				 uot  \
				 rtf
LOFMTS = odt
IMFMTS = pdf  \
				 png  
LOCONV = $(LOFMTS) \
				 $(MSFMTS) \
				 $(IMFMTS)
FORMAT = \
				 $(XTPFMT) \
				 $(LOCONV)
SOURCE = resume.py
RESUME = $(BUILD)/resume/resume.
BUILDS = $(FORMAT:%=$(RESUME)%)
OUTPUT = $(BUILDS)
SITE   = /srv/http/tymestl.org/
all: $(OUTPUT)

$(BUILD)/resume:
	mkdir $(BUILD)/resume

$(RESUME)$(XTPFMT): $(SOURCE) $(PYXTP) $(BUILD)/resume
	cd $(BUILD)/resume && /usr/bin/env python3 $(PYXTP) $(SOURCE:%=$(SUBDIR)/%)

$(RESUME)%: $(RESUME)$(LOSRCF) $(SOURCE)
	libreoffice --headless --convert-to $(@:$(RESUME)%=%) $< --outdir $(BUILD)/resume/

$(BUILD)/%: %
	mkdir -p $(BUILD)/$(dir $<)
	cp $< $@

install: $(BUILD)/resume
	cp -rv $(BUILD)/resume/ -t $(SITE)
