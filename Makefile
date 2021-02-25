.PHONY: update_riot_stats update_riot_repo update_riot_board_list update_riot_data
.PHONY: update_riot_contributors install_python_requirements
.PHONY: update_riot_drivers
.PHONY: build serve

RIOT_REPO_URL = "https://github.com/RIOT-OS/RIOT.git"

TOOLS_DIR = $(abspath _tools)
DATA_DIR = $(abspath _data)
_DEFAULT_RIOTBASE = $(abspath _RIOT)
RIOTBASE ?= $(_DEFAULT_RIOTBASE)

RIOT_BOARDS_FILE = $(DATA_DIR)/riot_boards.yml
RIOT_STATS_FILE = $(DATA_DIR)/riot_stats.yml
RIOT_CONTRIBUTORS_FILE = $(DATA_DIR)/contributors.json
RIOT_DRIVERS_FILE = $(DATA_DIR)/riot_drivers.csv
RIOT_DRIVERS_CATS_FILE = $(DATA_DIR)/riot_drivers_cats.csv

WATCH ?= 0

ifeq ($(WATCH),1)
	JEKYLL_BUILD_ARGS += --watch
endif

PRODUCTION ?= 0
ifeq ($(PRODUCTION),1)
	JEKYLL_BUILD_ARGS += --config _config.yml,_config_production.yml
endif

$(RIOTBASE):
	@git clone $(RIOT_REPO_URL) $(RIOTBASE)

install_python_requirements:
	@pip install -r $(TOOLS_DIR)/requirements.txt

update_riot_repo: $(RIOTBASE)
ifeq ($(RIOTBASE),$(_DEFAULT_RIOTBASE))
	@git -C $(RIOTBASE) pull
endif

update_riot_stats: update_riot_repo
	@$(TOOLS_DIR)/riot-stats.sh $(RIOTBASE) > $(RIOT_STATS_FILE)

update_riot_board_list: update_riot_repo
	@$(TOOLS_DIR)/riot-boards.sh $(RIOTBASE) > $(RIOT_BOARDS_FILE)

update_riot_contributors: install_python_requirements
	@python $(TOOLS_DIR)/riot-contributors.py > $(RIOT_CONTRIBUTORS_FILE)

update_drivers_cats:
	@$(TOOLS_DIR)/riot-drivers-cats.sh $(RIOTBASE) > $(RIOT_DRIVERS_CATS_FILE)

update_riot_drivers: update_drivers_cats
	@$(TOOLS_DIR)/riot-drivers.sh $(RIOTBASE) > $(RIOT_DRIVERS_FILE)

update_riot_data: update_riot_contributors update_riot_board_list update_riot_stats update_riot_drivers;

build:
	@bundle exec jekyll build $(JEKYLL_BUILD_ARGS)

serve:
	@bundle exec jekyll serve --livereload
