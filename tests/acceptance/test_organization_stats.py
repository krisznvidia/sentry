from __future__ import absolute_import

from django.utils import timezone

from sentry.testutils import AcceptanceTestCase


class OrganizationStatsTest(AcceptanceTestCase):
    def setUp(self):
        super(OrganizationStatsTest, self).setUp()
        self.user = self.create_user('foo@example.com')
        self.org = self.create_organization(name='Org Name')
        self.team = self.create_team(name='Team Name', organization=self.org, members=[self.user])
        self.project = self.create_project(
            organization=self.org,
            team=self.team,
            name='Project Name'
        )
        self.login_as(self.user)
        self.path = '/organizations/{}/stats/'.format(self.org.slug)

    def test_simple(self):
        self.project.update(first_event=timezone.now())
        self.browser.get(self.path)
        # dashboard is a bit complex to load since it has many subcomponents
        # so we bank on the core container and the activity container being
        # enough of a check
        self.browser.wait_until('.organization-home')
        self.browser.wait_until_not('.loading-indicator')
        self.browser.snapshot('organization stats')
