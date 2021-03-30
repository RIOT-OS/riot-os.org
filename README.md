## Source code for riot-os.org

### Building
Make sure you have Jekyll and Bundle installed (see https://jekyllrb.com/docs/).
Python 3.6+ is also required.

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
All RIOT-related data rendered in the website (e.g. statistics,
contributors and board list) is parsed from the RIOT repository and the GitHub
API at build time using a custom Python script (requires Python 3.6+).

To update this data run `make update_riot_data`.

To fetch the list of RIOT contributor, install the "requests" Python package using
`make install_python_requirements`

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

### Adding companies
Companies display their logos on the logo wall. To add a new company a new entry
in `_data/companies.yml` is needed. Each company needs a unique key to be
referenced. Place the logo under `assets/img/companies`. The needed data to add
a company is:

- `name`: Display name of the company
- `logo`: Path to the logo, relative to `assets/img/companies/`.
- `url`: URL to the company website

### Adding Use Cases
Use cases are displayed as cards in the Users section. They also have their own
page that describes in detail the use case. Use cases are a collection. To add a
new one, create a new file in the `_use_cases` directory. The first lines will
contain the metadata of the use case in YAML format. This section must have
lines before and after containing `---`. Following the metadata, place the main
content in Markdown format.

Use cases will contain a quote. You will need a photo of the author of the
quote, place it under `assets/img/use-cases/user-photos`. Each use case must be
associated to a company (see #adding-companies).

The metadata required for an use case is the following:

- `project`: Project title (used as title of the page)
- `quote`: Quote from the user
- `user`: Author of the quote
- `user_position`: Position of the user in the company
- `user_photo`: Path to the user photo, relative to `assets/img/use-cases/`
- `company`: key of the company in `companies.yml` (see #adding-companies)

### Blog
For now the blog is not published. For local development you can render the blog
section by setting `blog` to `true` in `_config.yml`.
