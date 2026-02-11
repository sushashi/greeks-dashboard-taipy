import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go


def d1(S, K, T, r, sigma):
    return (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma*np.sqrt(T)

def N(x):
    return norm.cdf(x)

def BSM_call(S, K, T, r, sigma):
    x1 = d1(S, K, T, r, sigma)
    x2 = d2(S, K, T, r, sigma)
    return S*N(x1) - K*np.exp(-r*T)*N(x2)

def BSM_put(S, K, T, r, sigma):
    x1 = d1(S, K, T, r, sigma)
    x2 = d2(S, K, T, r, sigma)
    return K*np.exp(-r*T)*N(-x2) - S*N(-x1)

def delta(S, K, T, r, sigma):
    return N(d1(S, K, T, r, sigma))

def gamma(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) * np.sqrt(T) * S

def theta(S, K, T, r, sigma):
    return - sigma * norm.pdf(d1(S, K, T, r, sigma)) * S / (2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2(S, K, T, r, sigma))

def rho(S, K, T, r, sigma):
    return K*T*np.exp(-r*T)*N(d2(S, K, T, r, sigma))

def rho_put(S, K, T, r, sigma):
    return -K*T*np.exp(-r*T)*N(-d2(S, K, T, r, sigma))


def plot_surface(X, Y, Z, title):
    fig = go.Figure(data = [go.Surface(z=Z, x=X, y=Y, 
                    hovertemplate = 'S: %{x:.2f}<br>' +
                                    'T: %{y:.2f}<br>' +
                                    'Value: %{z:.2f}<extra></extra>',
                    opacity=1,
                    colorscale='jet'
    )])

    fig.update_layout(  scene_camera = dict(
                            up=dict(x=0, y=0, z=1),
                            center=dict(x=0, y=0, z=0),
                            eye=dict(x=-1.5, y=-1.5, z=0.8)
                        ),
                        scene = dict(
                            xaxis_title="S",
                            yaxis_title="T",
                            zaxis_title=title,
                        ),
                        title=title)
    return fig