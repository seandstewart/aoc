SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:

MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(VIRTUAL_ENV), )
	RUN_PREFIX := poetry run
else
	RUN_PREFIX :=
endif


# region: environment

bootstrap: setup-poetry update install  ## Bootstrap your local environment for development.
.PHONY: bootstrap

setup-poetry:  ## Set up your poetry installation and ensure it's up-to-date.
	@poetry self update -q
.PHONY: setup-poetry

install:  ## Install or re-install your app's dependencies.
	@poetry install
	@$(RUN_PREFIX) pre-commit install && $(RUN_PREFIX) pre-commit install-hooks
.PHONY: install

update:  ## Update app dependencies
	@poetry update
	@$(RUN_PREFIX) pre-commit autoupdate
.PHONY: update

# endregion
# region: dev

target ?= .
files ?= --all-files
ifneq ($(target), .)
	files := --files=$(target)
endif

format:  ## Manually run code-formatters for the app.
	@$(RUN_PREFIX) pre-commit run ruff-format $(files)
	@$(RUN_PREFIX) pre-commit run ruff $(files)
.PHONY: format

SRC := src/aoc
year ?= y2024
day ?= 1
part ?= 1
DAY_PKG := $(SRC)/$(year)/day$(day)/
PART_PKG := $(DAY_PKG)part$(part)/


puzzle:  ## Get the puzzle for the targeted day. Arguments: `day=<day|1>`, `part=<part|1>`.
	mkdir -p "$(DAY_PKG)"
	touch "$(DAY_PKG)/__init__.py"
	cp -R ".template" $(PART_PKG)
	rm -rf "$(PART_PKG)/.template"
	chmod +x "$(PART_PKG)/solve.py"
	aoc download --day=$(day) --input-file="$(PART_PKG)/input" --puzzle-file="$(PART_PKG)/puzzle.md" --overwrite
	aoc read --day=$(day)
	git add "$(DAY_PKG)"
.PHONY: puzzle


solve:  ## Run the solution for the targeted day. Arguments: `day=<day|1>`
	poetry run ./$(PART_PKG)solve.py
.PHONY: solve

submit:  ## Run the solution for the targeted day and submit it to AOC for the targeted part. Arguments: `day=<day|1>`, `part=<part|1>`.
	aoc submit --day=$(day) $(part) $(shell poetry run ./$(PART_PKG)solve.py)
.PHONY: submit


# endregion
# region: ci

lint:  ## Run this app's linters. Target a specific file or directory with `target=path/...`.
	@$(RUN_PREFIX) pre-commit run ruff $(files)
	@$(RUN_PREFIX) pre-commit run mypy $(files)
.PHONY: lint

test: ## Run this app's tests with a test db. Target a specific path `target=path/...`.
	$(RUN_PREFIX) pytest $(target) $(TEST_ARGS)
.PHONY: test

TEST_ARGS ?= --cov --cov-config=.coveragerc --cov-report=xml --cov-report=term --junit-xml=junit.xml

rule ?= patch


release-version:  ## Bump the version for this package.
	$(eval current_version := $(shell poetry version -s))
	$(eval new_version := $(shell poetry version -s $(rule)))
	$(eval message := "Release $(current_version) -> $(new_version)")
	git add pyproject.toml
	git commit -m $(message)
	git tag -a v$(new_version) -m $(message)
.PHONY: release-version


report-version:  ## Show the current version of this library.
	@$(VERSION_CMD)
.PHONY: report-version

docs-version:  ## Show the current version of this library as applicable for documentation.
	@$(VERSION_CMD) | $(SED_CMD) $(DOCS_FILTER)
.PHONY: docs-version

docs: ## Build the versioned documentation
	@$(RUN_PREFIX) mike deploy -u --push $(version) $(alias)
.PHONY: docs

VERSION_CMD ?= poetry version -s
SED_CMD ?= sed -En
DOCS_FILTER ?= 's/^([[:digit:]]+.[[:digit:]]+).*$$/v\1/p'
version ?= $(shell $(VERSION_CMD) | $(SED_CMD) $(DOCS_FILTER))
alias ?= latest

changelog:  ## Compile the latest changelog for the current branch.
	@$(RUN_PREFIX) git-changelog
	@git add docs/changelog.md
	@git commit -m "[skip ci] Update changelog." --allow-empty
.PHONY: changelog

release-notes:  ## Compile release notes for VCS
	@$(RUN_PREFIX) git-changelog --release-notes
.PHONY: release-notes

# endregion

.PHONY: help
help: ## Display this help screen.
	@printf "$(BOLD)$(ITALIC)$(MAGENTA)✨  Make typelib with Make. ✨ $(RESET)\n"
	@printf "\n$(ITALIC)$(GREEN)Supported Commands: $(RESET)\n"
	@grep -E '^[a-zA-Z0-9._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(CYAN)$(MSGPREFIX) %-$(MAX_CHARS)s$(RESET) $(ITALIC)$(DIM)%s$(RESET)\n", $$1, $$2}'

.DEFAULT_GOAL := help

# Messaging
###
MAX_CHARS ?= 24
BOLD := \033[1m
RESET_BOLD := \033[21m
ITALIC := \033[3m
RESET_ITALIC := \033[23m
DIM := \033[2m
BLINK := \033[5m
RESET_BLINK := \033[25m
RED := \033[1;31m
GREEN := \033[32m
YELLOW := \033[1;33m
MAGENTA := \033[1;35m
CYAN := \033[36m
RESET := \033[0m
MSGPREFIX ?=   »
