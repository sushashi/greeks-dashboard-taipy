# Greeks Dashboard

Greeks Dashboard is a web application for visualizing option greeks for vanilla options using the Black-Scholes model.

Built with [Taipy](https://taipy.io/), a Python library for data webapp.

## Why this app

The idea was to create something more interactive than the explanations in my notebook about derivatives while learning how to use Taipy. All Black-Scholes computation code is reused from the original notebook.

Source code and basic introduction to derivatives and option greeks in my [**Notebook**](https://github.com/sushashi/finance-notebooks/blob/main/01_Intro_Derivatives_BSM_Greeks.ipynb)

## Installation
 
```
git clone https://github.com/sushashi/greeks-dashboard-taipy
cd greeks-dashboard-taipy
pip install -r requirements.txt
cd src
taipy run main.py
```

## Alternatively with docker

```
git clone https://github.com/sushashi/greeks-dashboard-taipy
cd greeks-dashboard-taipy
docker-compose up
```

## Live Demo

**https://greeks-dashboard-taipy.onrender.com/**

The app runs on [Render](https://render.com/)'s free plan, so it would take a moment (~30 seconds) to spin it up.

Moreover, performance is slower on the free plan due to limited resources.

## Screenshots

![2d plot](/img/screenshot_greeks_2d.jpg)
![3d plot](/img/screenshot_greeks_3d.jpg)