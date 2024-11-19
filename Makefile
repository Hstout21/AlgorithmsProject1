PYTHON = python3
PIP = pip3
REQUIREDPIPS = allPips.txt
QUESTION1 = Question1.py
QUESTION2 = Question2.py

all: install run

install:
	@echo "Checking Pips."
	@if [ -f $(REQUIREDPIPS) ]; then $(PIP) install -r $(REQUIREDPIPS); \
	else echo "Warning, cannot find pips file."; fi

run: $(QUESTION1) $(QUESTION2)
	@echo "Running $(QUESTION1)."
	$(PYTHON) $(QUESTION1)
	@echo "Running $(QUESTION2)."
	$(PYTHON) $(QUESTION2)

clean:
	@echo "Running Clean."
	find . -type f -name '*.png' -delete
	find . -type f -name 'Results.txt' -delete
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

help:
	@echo "Make cmds:"
	@echo "  make         - Install pips and run files."
	@echo "  make clean   - Clean old images."
	@echo "  "
	@echo "  make install - Install pips."
	@echo "  make run     - Run files."