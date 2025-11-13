# BankAccount va PremiumAccount

Python dasturlash tilida yozilgan oddiy bank hisoblarini boshqarish tizimi.

## Xususiyatlar

### `BankAccount`
- Hisob raqami, mijoz ismi va balans maxfiy (`__` bilan).
- Balans faqat `deposit()` va `withdraw()` orqali o‘zgaradi.
- Balans manfiy bo‘lishi mumkin emas.
- `get_balance()` faqat o‘qish uchun.

### `PremiumAccount`
- `BankAccount` dan meros oladi.
- `withdraw()` da chegirmali foiz qo‘llaniladi (standart: 10%).

## Foydalanish

```python
# Oddiy hisob
acc = BankAccount("12345", "Ali")
acc.deposit(1000)
acc.withdraw(400)
print(acc.get_balance())  # 600

# Premium hisob
prem = PremiumAccount("67890", "Vali", discount_rate=0.15)
prem.deposit(2000)
prem.withdraw(1000)  # 1000 * 0.85 = 850 ayiriladi
print(prem.get_balance())  # 1150
