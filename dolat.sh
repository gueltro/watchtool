pdflatex -halt-on-error -output-directory $(dirname "$1") $1 
evince  ${1%.*}.pdf & 
