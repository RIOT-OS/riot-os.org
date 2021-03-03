.PHONY: update_riot_repo update_riot_data install_python_requirements
.PHONY: build serve

RIOT_REPO_URL = "https://github.com/RIOT-OS/RIOT.git"

TOOLS_DIR = $(abspath _tools)
DATA_DIR = $(abspath _data)
_DEFAULT_RIOTBASE = $(abspath _RIOT)
RIOTBASE ?= $(_DEFAULT_RIOTBASE)

RIOT_FETCH_DATA_CMD = RIOTBASE=$(RIOTBASE) DATA_DIR=$(DATA_DIR) $(TOOLS_DIR)/fetch_riot_data.py
RIOT_DATA_FILES += $(DATA_DIR)/riot_boards.yml
RIOT_DATA_FILES += $(DATA_DIR)/riot_stats.yml
RIOT_DATA_FILES += $(DATA_DIR)/riot_contributors.yml
RIOT_DATA_FILES += $(DATA_DIR)/riot_drivers.yml
RIOT_DATA_FILES += $(DATA_DIR)/riot_drivers_cats.yml
RIOT_DATA_FILES += $(DATA_DIR)/riot_cpus.yml

WATCH ?= 0

ifeq ($(WATCH),1)
  JEKYLL_BUILD_ARGS += --watch
endif

PRODUCTION ?= 0
ifeq ($(PRODUCTION),1)
  JEKYLL_BUILD_ARGS += --config _config.yml,_config_production.yml
  export JEKYLL_ENV=production
endif

$(RIOTBASE):
	@git clone $(RIOT_REPO_URL) $(RIOTBASE)

install_python_requirements:
	@pip3 install -r $(TOOLS_DIR)/requirements.txt

update_riot_repo: $(RIOTBASE)
ifeq ($(RIOTBASE),$(_DEFAULT_RIOTBASE))
	@git -C $(RIOTBASE) pull
endif

$(RIOT_DATA_FILES):
	@$(RIOT_FETCH_DATA_CMD)

update_riot_data: update_riot_repo
	@$(RIOT_FETCH_DATA_CMD)

clean_riot_data:
	rm -f $(RIOT_DATA_FILES)

build: $(RIOT_DATA_FILES)
	@bundle exec jekyll build $(JEKYLL_BUILD_ARGS)

serve: $(RIOT_DATA_FILES)
	@bundle exec jekyll serve --livereload
