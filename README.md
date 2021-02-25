## Source code for riot-os.org

### Building
Make sure you have Jekyll and Bundle installed (see https://jekyllrb.com/docs/).

Then run

```
bundle
```

to install all further dependencies.

Run `make build`. This will create a directory `_site`. To watch
for file changes and trigger a rebuild, you can set the environment variable
`WATCH`:

```
WATCH=1 make build`.
```

To build for production environment set the environmental variable
`PRODUCTION`:

```
PRODUCTION=1 make build
```

### Serving

Run `make serve`. The site will be available at http://localhost:4000

### Updating RIOT-related data
All RIOT-related data that is rendered in the website (e.g. statistics,
contributors and board list) is parsed from files in the `_data` folder. To
update these files with fresh information some `make` targets are available:

- `update_riot_stats`
- `update_riot_board_list`
- `update_riot_contributors`
- `update_riot_drivers`

To update everything at once run `make update_riot_data`.

#### Local RIOT repo
You can specify where your local RIOT repo is located by defining the `RIOTBASE`
environment variable. When the variable is not defined the repo will be cloned
into the project folder.

#### Github Token
In order to update the list of contributors requests to the Github API are performed.
If no [token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
is provided then you may run into restrictions on the
amount of times you can update the list. To provide the token define the environment
variable `GITHUB_TOKEN` with the value of the token.
