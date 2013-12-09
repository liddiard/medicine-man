import os, sys, getpass
import heroku
from requests.exceptions import HTTPError

# var initialization
try:
    my_app = sys.argv[1]
    domains_file = sys.argv[2]
except IndexError:
    print "\nUsage: ~$ python add_domains.py app_name domains_to_add.txt\n"
    sys.exit(1)
heroku_email = raw_input("Heroku email: ")
heroku_pass = getpass.getpass()
domains_error = []
d_success = 0
d_failure = 0

# read the supplied domains file
with open(domains_file, 'r') as f:
    domains = [line.strip() for line in f]
print "Attempting to add %d domains to '%s' from supplied '%s'..." % (len(domains), my_app, domains_file)

# log in to Heroku
cloud = heroku.from_pass(heroku_email, heroku_pass)
app = cloud.apps[my_app]
domain = app.domains

# try adding domains
for d in domains:
    try:
        domain.add(d)
        d_success += 1
        print "added: %s" % d
    except HTTPError:
        domains_error.append(d)
        d_failure += 1
        print "ERROR adding: %s" % d

# print the report
if domains_error:
    print "\nHeroku encountered an error adding the following domains: \n%s" %\
          '\n'.join(domains_error)
print "\n----------\n"
print "%d domains successfully added; %d domains encountered an error." % (d_success, d_failure)
