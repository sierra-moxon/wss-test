## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Download the JGI NMDC dataflow diagram and copy it to docs for GitHub Pages
[group('deployment')]
fetch-dataflow:
  curl -L https://raw.githubusercontent.com/sierra-moxon/wss-test/main/jgi_nmdc_dataflow.html -o docs/jgi_nmdc_dataflow.html
  @echo "Downloaded jgi_nmdc_dataflow.html to docs/"
