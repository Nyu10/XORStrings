#! /bin/bash

#make run ARGS="human key1 message1"
#make run ARGS="numOut key1 message1"
# Examples : make run ARGS="encode HOTDOGSTAND BOAR"
#			make run ARGS="decode ICTUPUSKBBD BOAR"
Help:
$(info ARGS should be human/numOut, the key, the message)


run:
	@python hex.py $(ARGS)

