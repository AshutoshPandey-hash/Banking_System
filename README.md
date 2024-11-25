# Bank Transaction System

## Overview

The **Bank Transaction System** is a simple Python-based application that simulates a banking environment where users can check their bank balance, deposit funds, withdraw money, and view their transaction history. This system utilizes file handling to store and update the bank balance and transaction records, ensuring that the user's balance persists across sessions.

## Features

- **Persistent Bank Balance**: The balance is saved in a file (`bank_balance.txt`) and is updated after each transaction, making sure the balance remains even after the program is closed and reopened.
- **Deposit and Withdrawal**: Users can deposit and withdraw money, with validation to ensure that only valid and positive amounts are processed.
- **Transaction History**: A running log of all deposits and withdrawals, which can be viewed by the user.
- **Error Handling**: The system includes basic error handling to handle invalid inputs (e.g., non-numeric values, negative values, or insufficient funds).

## Requirements

- Python 3.x
- Basic knowledge of Python (functions, conditionals, loops, and file handling)

## Setup

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script using a Python interpreter.

```bash
python transaction.py
