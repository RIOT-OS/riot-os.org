## Source code for riot-os.org

### Building
Make sure you have Jekyll and Bundle installed (see https://jekyllrb.com/docs/).

Then run

```
bundle
```

to install all further dependencies.

Run `bundle exec jekyll build`. This will create a directory `_site`. To watch
for file changes and trigger a rebuild, you can run
`bundle exec jekyll build --watch`.

To build for production environment set the environmental variable
`JEKYLL_ENV=production`. For production environments you need to add the
`_config_production.yml` file to the build to override the `baseurl`, by adding
`--config _config.yml,_config_production.yml` to the build command.

### Serving

Serve the website running `bundle exec jekyll serve --livereload`.
