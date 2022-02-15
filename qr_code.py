import pathlib
from enum import Enum
from typing import Optional

import qrcode
from pydantic import BaseModel

path = pathlib.Path(__file__).parent


class Version(Enum):
    v1 = "1"
    v2 = "2"


class GiroCode(BaseModel):
    service_tag: Optional[str] = "BCD"
    version: Optional[Version] = Version.v2
    encoding: Optional[str] = "2"
    service_identification: Optional[str] = "SCT"
    bic: str
    name: str
    iban: str
    amount: float
    dta_key: Optional[str] = "CHAR"
    reference: Optional[str]
    purpose: Optional[str]
    hint: Optional[str]

    def __str__(self):
        return \
            f"""{self.service_tag}
            {self.version.value}
            {self.encoding}
            {self.service_identification}
            {self.bic}
            {self.name}
            {self.iban}
            EUR{round(self.amount, 2)}
            {self.dta_key}
            {self.reference if self.reference else ""}
            {self.purpose if self.purpose else ""}
            {self.hint if self.hint else ""}"""


def create_qr_giro_code(code: GiroCode):
    qr_code = qrcode.make(str(code))
    qr_code.save(f"{path}/giro_qr_code.png")


if __name__ == '__main__':
    my_code = GiroCode(
        bic="NTSBDEB1XXX",
        name="Code Specialist",
        iban="DE08500105172198996453",
        amount=5.0,  # Amount in EUR
    )
    create_qr_giro_code(my_code)