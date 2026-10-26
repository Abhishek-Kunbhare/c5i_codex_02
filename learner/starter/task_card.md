# Task cards

## Task A — repeat this exact task in both copies

Add optional discount support to `calculate_total`.

- Existing calls with only `items` must keep working.
- Add a keyword-only `discount_percent` parameter whose default is `0`.
- Accept values from 0 through 100 inclusive; reject values outside that range with `ValueError`.
- Apply the percentage discount to the cart subtotal.
- Keep returning a float.
- Add focused tests for 0%, 10%, 100%, and invalid values.
- Do not add dependencies or change the input item schema.

Use this same prompt in both folders. Do not improve it between runs. Compare the instructions' effect, not which run received a better prompt.

## Task B — test generalization after adding AGENTS.md

Add a helper `format_total(total)` that returns a string with exactly two digits after the decimal point, for example `"$14.00"`. Keep formatting separate from calculation. Add tests for whole-dollar values and fractional values. Do not modify `calculate_total` unless the tests show a bug in that existing function.
