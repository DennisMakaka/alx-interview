# Project Overview

The goal of this project is to implement a function that verifies if a dataset adheres to UTF-8 encoding. UTF-8 uses variable-length encoding, meaning characters can be represented with 1 to 4 bytes. Each integer in the dataset represents a byte, and only the 8 least significant bits are relevant for validation. The function should return `True` if the dataset is a valid UTF-8 encoding and `False` if it is not.

## Concepts and Requirements

### Key Concepts

**UTF-8 Encoding Rules:** UTF-8 follows specific rules for different byte lengths:
- **1-byte character:** Starts with `0xxxxxxx`.
- **2-byte character:** Starts with `110xxxxx` and followed by `10xxxxxx`.
- **3-byte character:** Starts with `1110xxxx` and followed by two `10xxxxxx`.
- **4-byte character:** Starts with `11110xxx` and followed by three `10xxxxxx`.

**Bitwise Operations:** The function should use bitwise operations to identify and validate the bit patterns in each byte.

### Requirements
- **Language:** Python 3
- **Code Style:** Follow PEP 8 guidelines for code style.
- **Environment:** Ubuntu 20.04 LTS

## Usage

To use the UTF-8 validation function, import and call `validUTF8` with a list of integers, each representing a byte of data. The function returns a Boolean indicating whether the dataset is a valid UTF-8 encoding.
