from enum import Enum
from typing import Union

import numpy as np
from scipy.stats import norm


class OptionType(Enum):
    CALL = "call"
    PUT = "put"


def black_scholes_price(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    option_type: OptionType,
) -> float:
    """
    Calculates the Black-Scholes price of an European option.

    Args:
        S: Underlying asset price (float)
        K: Strike price (float)
        T: Time to maturity (years) (float)
        r: Risk-free interest rate (float)
        sigma: Volatility of the underlying asset (float)
        option_type: OptionType (call or put)

    Returns:
        Option price (float)

    Raises:
        ValueError: If invalid input parameters are provided.
    """

    if S <= 0:
        raise ValueError("Underlying asset price (S) must be positive.")
    if K <= 0:
        raise ValueError("Strike price (K) must be positive.")
    if T <= 0:
        raise ValueError("Time to maturity (T) must be positive.")
    if r < 0:
        raise ValueError("Risk-free interest rate (r) cannot be negative.")
    if sigma <= 0:
        raise ValueError("Volatility (sigma) must be positive.")

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == OptionType.CALL:
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == OptionType.PUT:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type.")

    return price


if __name__ == "__main__":
    # Example usage
    S = 100.0  # Underlying price
    K = 105.0  # Strike price
    T = 0.5  # Time to maturity (years)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility

    call_price = black_scholes_price(S, K, T, r, sigma, OptionType.CALL)
    put_price = black_scholes_price(S, K, T, r, sigma, OptionType.PUT)

    print(f"Call Price: {call_price:.4f}")
    print(f"Put Price: {put_price:.4f}")