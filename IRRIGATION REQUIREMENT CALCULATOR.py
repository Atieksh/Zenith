import math

def calculate_net_irrigation_requirement(et_o, kc, p_eff, application_efficiency=0.85):
    try:
        if et_o < 0 or kc < 0 or p_eff < 0 or not (0 < application_efficiency <= 1):
            print()
            return None

        etc = et_o * kc

        nir = etc - p_eff

        gir = nir / application_efficiency if nir > 0 else 0.0

        return etc, nir, gir

    except Exception as e:
        print(e)
        return None

def main():
    print()
    print()

    try:
        print()

        et_o = float(input())

        kc = float(input())

        p_eff = float(input())

        eff = float(input())

    except ValueError:
        print()
        return

    results = calculate_net_irrigation_requirement(et_o, kc, p_eff, eff)

    if results:
        etc, nir, gir = results

        if nir <= 0:
            action = ""
            gir_display = "0.00 mm"
        else:
            action = ""
            gir_display = f"{gir:.2f} mm"

        print()
        print(f"{etc:.2f} mm")
        print(f"{nir:.2f} mm")
        print(f"{gir_display}")
        print(f"\n{action}")
        print()

if __name__ == "__main__":
    main()
