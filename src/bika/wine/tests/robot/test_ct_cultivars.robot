# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bika.wine -t test_cultivars.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bika.wine.testing.BIKA_WINE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bika/wine/tests/robot/test_cultivars.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Cultivars
  Given a logged-in site administrator
    and an add BikaSetup form
   When I type 'My Cultivars' into the title field
    and I submit the form
   Then a Cultivars with the title 'My Cultivars' has been created

Scenario: As a site administrator I can view a Cultivars
  Given a logged-in site administrator
    and a Cultivars 'My Cultivars'
   When I go to the Cultivars view
   Then I can see the Cultivars title 'My Cultivars'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add BikaSetup form
  Go To  ${PLONE_URL}/++add++BikaSetup

a Cultivars 'My Cultivars'
  Create content  type=BikaSetup  id=my-cultivars  title=My Cultivars

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Cultivars view
  Go To  ${PLONE_URL}/my-cultivars
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Cultivars with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Cultivars title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
