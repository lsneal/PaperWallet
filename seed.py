from monero.seed import Seed

s = Seed()

secret_spend = s.secret_spend_key()
secret_view = s.secret_view_key()
spend = s.public_spend_key()
view = s.public_view_key()
address = s.public_address()

print(f"Seed: {s.phrase}")
print(f"secret_spend: {secret_spend}")
print(f"secret_view: {secret_view}")
print(f"spend: {spend}")
print(f"view: {view}")
print(f"address: {address}")


# recovery with seed on hexa
hexa_seed = s.hex

seed = Seed(hexa_seed)

print(seed.phrase)
print(f"secret_spend: {secret_spend}")
