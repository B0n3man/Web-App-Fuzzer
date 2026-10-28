# Web App Fuzzer

A small Python command-line tool that sends HTTP GET requests using a list of test payloads. For each payload, it replaces the first occurrence of a chosen keyword in a URL and prints the response status code.

## Features

- Load payloads from a text file, one payload per line.
- Substitute each payload for the first matching keyword in the target URL.
- Send a GET request for each resulting URL and print its HTTP status code.

> **Current scope:** The CLI sends GET requests only. POST fuzzing, a working graphical interface, and the interceptor are not implemented yet.

## Requirements

- Python 3
- The `requests` package

## Setup

Install the dependency:

```bash
python -m pip install requests
```

Clone the repository and change into its directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Replace the placeholders with your GitHub repository URL and the directory created by cloning it.

## Usage

Create a text file containing one payload per line, for example `payloads.txt`:

```text
test
sample-value
another-value
```

Run the CLI:

```bash
python main.py
```

At the prompts, enter a URL containing the keyword to replace, that keyword, and the path to your payload file. For example:

```text
URL:     https://example.com/search?q=FUZZ
Keyword: FUZZ
File:    payloads.txt
```

The tool sends one GET request per payload and prints the URL and HTTP status code for each request. Payloads are substituted directly into the URL; provide values appropriate for the URL component you are testing.

## Project Structure

```text
.
├── main.py                  # Interactive command-line entry point
├── extractor.py             # Reads payloads from a text file
├── recursor.py              # Substitutes payloads and sends GET requests
├── GUI/
│   └── main.py              # Basic Tkinter window placeholder
├── Interceptor/
│   └── Interceptor.py       # Empty placeholder
└── test/
	└── main.py              # Standalone POST request example
```

## Responsible Use

Use this tool only against applications you own or have explicit permission to test. Fuzzing can generate repeated traffic and affect service availability; use a controlled test environment and a small payload list.

## Limitations

- The command-line tool performs GET requests only.
- The GUI does not currently run the fuzzer.
- The interceptor module is not implemented.
- Requests do not currently have a configurable timeout or rate limit.
- There is no automated test suite or dependency manifest yet.
