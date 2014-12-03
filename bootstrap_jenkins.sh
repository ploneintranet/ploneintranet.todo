virtualenv --no-setuptools .
mkdir -p buildout-cache/downloads
$(which echo) -e "[buildout]\nextends = buildout.d/travis.cfg" > buildout.cfg
./bin/python bootstrap.py
./bin/buildout
./bin/develop up -f
# Xvfb :99 -a &
