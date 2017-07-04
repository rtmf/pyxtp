ROOT := $(PWD)

SITES := resite

BUILD := $(PWD)/build

PYXTP := $(PWD)/src/xtp.py

export PYXTP
export BUILD

SUBDIRS=$(SITES)

.PHONY: $(SUBDIRS)

all: $(BUILD) $(SUBDIRS)

clean: $(SUBDIRS)
	$(MAKE) -C $@ clean

$(BUILD):
	mkdir -p $(BUILD)

$(SUBDIRS): $(BUILD) $(PYXTP)
	$(MAKE) -C $@
