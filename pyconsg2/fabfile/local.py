from django.conf import settings

from fabric.api import hide, lcd, local

from development_fabfile.fabfile import create_db, drop_db, lessc
from development_fabfile.fabfile import rebuild as rebuild_orig


def dumpdata():
    """
    Dumps everything.

    Remember to add new dumpdata commands for new apps here so that you always
    get a full initial dump when running this task.

    """
    local('python2.7 ./manage.py dumpdata --indent 4 --natural auth.user > pyconsg2/fixtures/bootstrap_auth.json')  # NOPEP8
    # account fixtures get created via signals when auth fixtures are loaded
    local('python2.7 ./manage.py dumpdata --indent 4 --natural sites > pyconsg2/fixtures/bootstrap_sites.json')  # NOPEP8

    # django-cms
    local('python2.7 ./manage.py dumpdata --indent 4 --natural cms.placeholder > pyconsg2/fixtures/bootstrap_cms_placeholder.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural cms --exclude cms.placeholder > pyconsg2/fixtures/bootstrap_cms.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural multilingual_news > pyconsg2/fixtures/bootstrap_multilingual_news.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural djangocms_text_ckeditor > pyconsg2/fixtures/bootstrap_djangocms_text_ckeditor.json')  # NOPEP8

    local('python2.7 ./manage.py dumpdata --indent 4 --natural conference > pyconsg2/fixtures/bootstrap_conference.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural speakers > pyconsg2/fixtures/bootstrap_speakers.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural proposals > pyconsg2/fixtures/bootstrap_proposals.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural proposals_pyconsg > pyconsg2/fixtures/bootstrap_proposals_pyconsg.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural schedule > pyconsg2/fixtures/bootstrap_schedule.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural sponsorship > pyconsg2/fixtures/bootstrap_sponsorship.json')  # NOPEP8

    local('python2.7 ./manage.py dumpdata --indent 4 --natural paypal_express_checkout > pyconsg2/fixtures/bootstrap_paypal_express_checkout.json')  # NOPEP8


def lessc():
    """Compiles the less files."""
    local('lessc {0}/static/css/bootstrap.less'
          ' {0}/static/css/bootstrap.css'.format(settings.PROJECT_NAME))


def loaddata():
    """Loads available fixtures."""
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_auth.json')
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_sites.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_cms_placeholder.json')
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_cms.json')
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_multilingual_news.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_djangocms_text_ckeditor.json')  # NOPEP8

    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_conference.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_speakers.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_proposals.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_proposals_pyconsg.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_schedule.json')  # NOPEP8
    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_sponsorship.json')  # NOPEP8

    local('python2.7 manage.py loaddata pyconsg2/fixtures/bootstrap_paypal_express_checkout.json')  # NOPEP8


def rebuild():
    """
    Deletes and re-creates your DB. Needs django-extensions and South.

    """
    drop_db()
    create_db()
    local('python2.7 manage.py syncdb --all --noinput')
    local('python2.7 manage.py migrate --fake')
    loaddata()
