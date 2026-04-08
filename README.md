## senaite.crms

### Overview

`bika.wine` extends **Senaite** (the modern core of Bika LIMS) with 

It
- Adds Vintage and Cultivar attributes to Samples 
- Adds them to a Wine COA template

### Requirements

- **Senaite** (recommended latest version) or **Ingwe Bika LIMS 4**

### Installation

#### Using Buildout (Classic Plone/Senaite)

Add the following to your `buildout.cfg`:

cfg
[buildout]
eggs =
    ...
    bika.wine

Then run:
Bashbin/buildout

#### Docker (Recommended for Ingwe Bika LIMS 4)

Add bika.wine to your custom add-ons list in the Docker-based Ingwe Bika distribution.

### User Manual

[Bika Wine user manual](https://www.bikalims.org/new-manual/bika-wine)

### License
This project is licensed under the GNU General Public License v2.0 (GPL-2.0).

### Support & Professional Services
[Bika Lab Systems](www.bikalabs.com) offers professional implementation, training, custom development, and support for bika.wine.

Website: [https://www.bikalims.org](https://www.bikalims.org)
Email: info@bikalims.org (or contact Lemoene directly)

Made with ❤️ in Cape Town, South Africa
