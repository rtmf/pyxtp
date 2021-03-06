ROOT := $(PWD)

SITES := resite resume

BUILD := $(PWD)/build

PYXTP := $(PWD)/src/xtp.py

export PYXTP
export BUILD

SUBDIRS=$(SITES)

.PHONY: $(SUBDIRS)

all: $(BUILD) $(SUBDIRS)

clean: 
	rm -rf $(BUILD)

$(BUILD):
	mkdir -p $(BUILD)

$(SUBDIRS): $(BUILD) $(PYXTP)
	$(MAKE) -C $@ all SUBDIR=$(ROOT)/$@

install:
	$(MAKE) -C resume install
