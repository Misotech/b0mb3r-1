from db0mb3r.services.service import Service


class PrivatBankCard(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://carddesign.privatbank.ua/phone",
            data={"phone": "+" + self.formatted_phone},
        )
