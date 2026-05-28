def celsius_to_fahrenheit(celsius):
    """Santigrat dereceyi Fahrenhayt'a çevirir."""
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print(f"20 Santigrat = {celsius_to_fahrenheit(20)} Fahrenhayt")


def km_to_miles(km):
    # Lider bu formülü farklı biliyor (Kasıtlı Hata/Çakışma)
    return km * 0.62