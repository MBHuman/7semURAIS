
.PHONY: install_script_deps
install_script_deps:
	python3 -m pip install -r ./scripts/requirements.txt

.PHONY: convert_to_pdf
convert_to_pdf:
	python3 ./scripts/convert.py