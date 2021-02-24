.PHONY: update_riot_stats update_riot_repo update_riot_board_list update_riot_data
.PHONY: update_riot_contributors install_python_requirements

RIOT_REPO_URL = "https://github.com/RIOT-OS/RIOT.git"

TOOLS_DIR = $(abspath _tools)
DATA_DIR = $(abspath _data)
_DEFAULT_RIOTBASE = $(abspath _RIOT)
RIOTBASE ?= $(_DEFAULT_RIOTBASE)

RIOT_BOARDS_FILE = $(DATA_DIR)/riot_boards.yml
RIOT_STATS_FILE = $(DATA_DIR)/riot_stats.yml
RIOT_CONTRIBUTORS_FILE = $(DATA_DIR)/contributors.json

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

update_riot_data: update_riot_contributors update_riot_board_list update_riot_stats;
