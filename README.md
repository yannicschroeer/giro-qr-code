# Giro QR-Code

Script to create a QR-Code for IBAN/BIC

# Usage

Install the requirements
```shell
pip install -r requirements.txt
```

Create a new python file and execute it
```python
from qr_code import GiroCode, create_qr_giro_code

my_code = GiroCode(
    bic="NTSBDEB1XXX",
    name="Code Specialist",
    iban="DE08500105172198996453",
    amount=5.0,  # Amount in EUR
)
create_qr_giro_code(my_code)
```

This will create a file `giro_qr_code.png` in the directory of the `qr_code.py` with the encoded details:

![QR Code Example](./giro_qr_code.png)