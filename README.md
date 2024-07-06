# Custom Invoice Header for Odoo

## Overview

The Custom Invoice Header module enhances Odoo's invoice reporting functionality by adding the invoice number to the header of PDF reports from the second page onwards. This module is designed for Odoo 16 and integrates seamlessly with the existing invoice layout. This code use code from OCA Reporting-Engine -> report_qweb_element_page_visibility

## Features

- Displays the invoice number in the header of PDF reports starting from the second page
- Maintains the original invoice header layout, including company logo and details
- Only affects PDF reports, leaving other report types unchanged
- Compatible with Odoo 16

## Installation

1. Clone this repository or download the module files.
2. Place the `custom_invoice_header` folder in your Odoo addons directory.
3. Update the module list in Odoo:
   - Enable developer mode
   - Go to Apps > Update Apps List
4. Search for "Custom Invoice Header" in the Apps menu and install the module.

## Usage

Once installed, the module automatically applies the custom header to PDF invoice reports. No additional configuration is required.

To see the changes:
1. Generate a PDF invoice report with multiple pages.
2. Observe that from the second page onwards, the invoice number appears in the header on the right side.

## Technical Details

The module works by extending the `web.external_layout_standard` template and modifying the header structure for PDF reports. It uses Odoo's `report_type` context variable to ensure the custom header is only applied to PDF outputs.

Key files:
- `__manifest__.py`: Module metadata and dependencies
- `views/report_templates.xml`: XML template modifications for the custom header

## Compatibility

This module is developed and tested on Odoo 16. It may require modifications to work with other Odoo versions.

## Support

For bug reports or feature requests, please use the issue tracker on the project's GitHub repository.

## Contributors OCA JavaScript code

* Nicola Malcontenti <nicola.malcontenti@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Alex Comba <alex.comba@agilebg.com>
* Saran Limpajitkutaporn <saranl@ecosoft.co.th>
* Pimolnat Suntian <pimolnats@ecosoft.co.th>
* Tharathip Chaweewongphan <tharathipc@ecosoft.co.th>
* `Trobz <https://trobz.com>`_:
    * Hai Lang <hailn@trobz.com>
* Ángel Tornero Hernández <angel.tornero@braintec.com>

## Contributing

Contributions to improve the module are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request

## License

This module is released under the LGPL-3 license. See the LICENSE file for more details.

## Authors

[Lasse Larsson, Kubang AB, lasse.larsson@kubang.eu]

---

For more information about Odoo development, visit the [official Odoo documentation](https://www.odoo.com/documentation/16.0/).
