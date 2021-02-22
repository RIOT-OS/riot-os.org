## Source code for riot-os.org

### Building
Make sure you have Jekyll and Bundle installed (see https://jekyllrb.com/docs/).

Then run

```
bundle
```

to install all further dependencies.

Run `bundle exec jekyll build`. This will create a directory `_site`.  To build
for production environment set the environmental variable
`JEKYLL_ENV=production`.  To watch for file changes and trigger a rebuild, you
can run `bundle exec jekyll build --watch`.

For local environments you need to add the `_config_development.yml` file to the
build to override the `baseurl`, by adding `--config _config.yml,_config_development.yml` to
the build command.

### Serving

Serve the website running `bundle exec jekyll serve --livereload`.
