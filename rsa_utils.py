def base_calculations(p, q, save_steps):
    n = p*q
    phi = (p-1)*(q-1)

    save_and_print_step(f"n = {p} * {q} = {n}", save_steps)
    save_and_print_step(f"Phi(n) = {p-1} * {q-1} = {phi}", save_steps)
    return n, phi



def GCD(phi, e, save_steps):
    steps = []
    save_and_print_step("\nEuklidischer Algorithmus:", save_steps)

    while e != 0:
        remainder = phi % e
        amount_of_times_e_fits = phi // e

        save_and_print_step(f"{phi} = {e} * {amount_of_times_e_fits} + {remainder}", save_steps)

        steps.append((remainder, phi, amount_of_times_e_fits, e))

        phi, e = e, remainder

    gcd = phi # If we don't return this gcd, it will return the original phi. Probably an issue with the for loop under this.
    if gcd != 1:
            raise ValueError(f"Der größte gemeinsame Teiler von Phi und E muss für die RSA-Verschlüsselung 1 sein!\nGGT: {gcd}")

    save_and_print_step("\nUmformen zu:", save_steps)

    for remainder, phi, amount_of_times_e_fits, e in reversed(steps):
        if remainder != 0:
            save_and_print_step(f"{remainder} = {phi} - {amount_of_times_e_fits} * {e}", save_steps)

    return gcd



def extended_GCD(a, b, save_steps):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_GCD(b, a % b, save_steps)
        save_and_print_step(f"{d} = {y} * {a} - {x - (a // b) * y} * {b}", save_steps)
        return d, y, x - (a // b) * y
    


def print_extended_GCD(e, phi, save_steps):
    save_and_print_step("\nErweiterter Euklidischer Algorithmus:", save_steps)

    gcd, d, _ = extended_GCD(e, phi, save_steps)  # calculate d
    # d cannot be negative, add phi to it.
    if d<0: 
        d += phi
    return gcd, d



def print_keys(n, e, d, save_steps):
    # Printing ÄÖÜ is NOT supported when converting to exe via PyInstaller!!!
    # This will inevitably cause your program to just stop.
    save_and_print_step(f"\nOeffentlicher Schluessel: ({n}, {e})\nPrivater Schluessel: ({n}, {d})", save_steps)



def save_and_print_step(string, save_steps):
    print(string)
    save_steps.append(string)