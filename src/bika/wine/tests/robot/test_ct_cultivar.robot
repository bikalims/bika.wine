# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bika.wine -t test_cultivar.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bika.wine.testing.BIKA_WINE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bika/wine/tests/robot/test_cultivar.robot
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

Scenario: As a site administrator I can add a Cultivar
  Given a logged-in site administrator
    and an add Cultivars form
   When I type 'My Cultivar' into the title field
    and I submit the form
   Then a Cultivar with the title 'My Cultivar' has been created

Scenario: As a site administrator I can view a Cultivar
  Given a logged-in site administrator
    and a Cultivar 'My Cultivar'
   When I go to the Cultivar view
   Then I can see the Cultivar title 'My Cultivar'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Cultivars form
  Go To  ${PLONE_URL}/++add++Cultivars

a Cultivar 'My Cultivar'
  Create content  type=Cultivars  id=my-cultivar  title=My Cultivar

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Cultivar view
  Go To  ${PLONE_URL}/my-cultivar
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Cultivar with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Cultivar title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
