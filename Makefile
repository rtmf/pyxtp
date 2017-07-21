ROOT := $(PWD)

SITES := resite

BUILD := $(PWD)/build

PYXTP := $(PWD)/src/xtp.py

export PYXTP
export BUILD

SUBDIRS=$(SITES)

.PHONY: $(SUBDIRS)

all: $(BUILD) $(SUBDIRS) resume.fodt

clean: 
	rm -rf $(BUILD)

$(BUILD):
	mkdir -p $(BUILD)

$(SUBDIRS): $(BUILD) $(PYXTP)
	$(MAKE) -C $@ all SUBDIR=$(ROOT)/$@

resume.fodt: $(PYXTP) resume.py
	$(PYXTP) resume.py
