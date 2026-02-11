from taipy.gui import Gui
import numpy as np
import warnings
import time

from utils import *
from page_greeks import page_greeks
from page_surfaces import page_surfaces

S = np.arange(0.01, 200, 3)
T = 1.0
T_range = np.arange(0.01, 1.0, 0.05)
r = 0.01
sigma = 0.3
K = 100
option_price = BSM_call(S, K, T, r, sigma)
option_delta = delta(S, K, T, r, sigma)
option_gamma = gamma(S, K, T, r, sigma)
option_vega = vega(S, K, T, r, sigma)
option_theta = theta(S, K, T, r, sigma)
option_rho = rho(S, K, T, r, sigma)

X, Y = np.meshgrid(S, T_range)
fig_surface_price = plot_surface(X, Y, BSM_call(X, K, Y, r, sigma), "Price")
fig_surface_delta = plot_surface(X, Y, delta(X, K, Y, r, sigma), "Delta")
fig_surface_gamma = plot_surface(X, Y, gamma(X, K, Y, r, sigma), "Gamma")
fig_surface_vega = plot_surface(X, Y, vega(X, K, Y, r, sigma), "Vega")
fig_surface_theta = plot_surface(X, Y, theta(X, K, Y, r, sigma), "Theta")
fig_surface_rho = plot_surface(X, Y, rho(X, K, Y, r, sigma), "Rho")

data = {
    'S': S,
    'T': T,
    'r': r,
    'sigma': sigma,
    'K': K,
    'option_price': option_price,
    'option_delta': option_delta,
    'option_gamma': option_gamma,
    'option_vega' : option_vega,
    'option_theta': option_theta,
    'option_rho' : option_rho,
}

option_type = "Call"
show_pane = True
progress_value = 0

def update_surfaces(state):
    time.sleep(1)
    if state.option_type == "Call":
        state.fig_surface_price = plot_surface(X, Y, BSM_call(X, state.K, Y, state.r, state.sigma), "Price")
        state.progress_value = 16
        state.fig_surface_delta = plot_surface(X, Y, delta(X, state.K, Y, state.r, state.sigma), "Delta")
        state.progress_value = 32
        state.fig_surface_gamma = plot_surface(X, Y, gamma(X, state.K, Y, state.r, state.sigma), "Gamma")
        state.progress_value = 50
        state.fig_surface_vega = plot_surface(X, Y, vega(X, state.K, Y, state.r, state.sigma), "Vega")
        state.progress_value = 64
        state.fig_surface_theta = plot_surface(X, Y, theta(X, state.K, Y, state.r, state.sigma), "Theta")
        state.progress_value = 80
        state.fig_surface_rho = plot_surface(X, Y, rho(X, state.K, Y, state.r, state.sigma), "Rho")
        state.progress_value = 100
    else:
        state.fig_surface_price = plot_surface(X, Y, BSM_put(X, state.K, Y, state.r, state.sigma), "Price")
        state.progress_value = 16
        state.fig_surface_delta = plot_surface(X, Y, delta(X, state.K, Y, state.r, state.sigma) - 1, "Delta")
        state.progress_value = 32
        state.fig_surface_gamma = plot_surface(X, Y, gamma(X, state.K, Y, state.r, state.sigma), "Gamma")
        state.progress_value = 50
        state.fig_surface_vega = plot_surface(X, Y, vega(X, state.K, Y, state.r, state.sigma), "Vega")
        state.progress_value = 65
        state.fig_surface_theta = plot_surface(X, Y, theta(X, state.K, Y, state.r, state.sigma)- r*K*np.exp(-r*state.T), "Theta")
        state.progress_value = 80
        state.fig_surface_rho = plot_surface(X, Y, rho_put(X, state.K, Y, state.r, state.sigma), "Rho")
        state.progress_value = 100

def update_plot(state):
    time.sleep(0.5)
    if state.option_type == "Call":
        state.data.option_price = BSM_call(S, state.K, state.T, state.r, state.sigma)
        state.data.option_delta = delta(S, state.K, state.T, state.r, state.sigma) 
        state.data.option_gamma = gamma(S, state.K, state.T, state.r, state.sigma)
        state.data.option_vega = vega(S, state.K, state.T, state.r, state.sigma)
        state.data.option_theta = theta(S, state.K, state.T, state.r, state.sigma)
        state.data.option_rho = rho(S, state.K, state.T, state.r, state.sigma)
    else: 
        state.data.option_price = BSM_put(S, state.K, state.T, state.r, state.sigma)
        state.data.option_delta = delta(S, state.K, state.T, state.r, state.sigma) - 1
        state.data.option_gamma = gamma(S, state.K, state.T, state.r, state.sigma)
        state.data.option_vega = vega(S, state.K, state.T, state.r, state.sigma)
        state.data.option_theta = theta(S, state.K, state.T, state.r, state.sigma) - r*K*np.exp(-r*state.T)
        state.data.option_rho = rho_put(S, state.K, state.T, state.r, state.sigma)

def on_navigate(state, page_name):
    if page_name == "greeks" :
        update_plot(state)
    else:
        update_surfaces(state)

home = """
"""

pages = {
    "/": home,
    "greeks": page_greeks,
    "surface": page_surfaces,
}

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message=".*invalid page name 'None'.*") # To get rid of warning message from on_navigate() that returns nothing
        Gui(pages=pages).run(dark_mode=False, title="Option Greeks", port=8000)