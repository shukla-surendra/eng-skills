PYTHON := $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)

.PHONY: docs check mkdocs

docs: ## Clean, render Markdown docs to HTML under docs_html/, and serve at http://localhost:8000
	rm -rf docs_html
	$(PYTHON) scripts/build_docs.py
	$(PYTHON) -m http.server --directory docs_html 8000

check: ## Validate all relative Markdown links, then build docs (no serve) - CI-friendly
	$(PYTHON) scripts/check_links.py
	rm -rf docs_html
	$(PYTHON) scripts/build_docs.py

mkdocs: ## Serve the MkDocs Material site at http://localhost:8010 (live-reloads on edits to the real .md files)
	$(PYTHON) scripts/link_mkdocs_docs.py
	$(PYTHON) -m mkdocs serve -a localhost:8010
