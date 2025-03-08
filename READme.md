# IP Information Lookup Tool

A powerful and hacker-styled IP information lookup tool using the IPinfo API. It retrieves details about an IP address, displays them in a table, and saves a stylish HTML report.

## Features
- Retrieves IP address information (location, hostname, region, country, timezone, etc.).
- Displays results in a hacker-themed ASCII banner.
- Saves reports in an HTML format with a neon-green hacker theme.
- Multi-threaded fetching for efficiency.

## Installation
```bash
https://github.com/samiXploits/ip_detailer_tool
cd ip_detailer_tool
pip install -r requirements.txt
```

## Usage
```bash
python ip_details.py
```
Enter one or multiple IP addresses separated by commas when prompted.

## Dependencies
- `requests` for making API calls
- `prettytable` for table display
- `colorama` for terminal colors

## API Token
Replace `IPINFO_ACCESS_TOKEN` inside `ip_details.py` with your IPinfo API token.

## Output
- Terminal output with a formatted table.
- HTML report stored in the `reports/` directory.

## Example Output
```
+-------------+------------+------+--------+---------+----------+------------+------------+
| IP Address  | Hostname   | City | Region | Country | Location | Postal Code | Timezone  |
+-------------+------------+------+--------+---------+----------+------------+------------+
| 8.8.8.8     | dns.google | ...  | ...    | ...     | ...      | ...        | ...        |
+-------------+------------+------+--------+---------+----------+------------+------------+
```

## License
MIT License

## Author
Mr. Sami

