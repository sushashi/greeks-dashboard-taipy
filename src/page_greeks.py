page_greeks = """

<|d-flex|

<|{show_pane}|pane|persistent|show_button|width=300px|
<|container|

<br/>
<|card|
<|navbar|lov={[('/greeks', '2D Greeks'),('/surface', '3D Surface')]}|>
|>

## Variables

**Option Type**<br/>
<|{option_type}|toggle|lov=Call; Put|on_change=update_plot|>

**Strike price:** <|{K}|text|><br/>
<|{K}|slider|min=50|max=150|on_change=update_plot|>

**Volatility:** <|{sigma}|text|><br/>
<|{sigma}|slider|min=0.1|max=2|step=0.1|on_change=update_plot|> 

**Interest rate:** <|{r}|text|><br/>
<|{r}|slider|min=0.0|max=0.2|step=0.01|on_change=update_plot|> 

**Time to maturity** <|{T}|text|><br/>
<|{T}|slider|min=0.01|max=2.0|step=0.01|on_change=update_plot|> 

|>
|>

<|
<|container|

# Option Greeks

<|layout|columns=1 1|

<|{data}|chart|mode=lines|x=S|y=option_price|title=Price|>

<|{data}|chart|mode=lines|x=S|y=option_delta|title=Delta|>

<|{data}|chart|mode=lines|x=S|y=option_gamma|title=Gamma|>

<|{data}|chart|mode=lines|x=S|y=option_vega|title=Vega|>

<|{data}|chart|mode=lines|x=S|y=option_theta|title=Theta|>

<|{data}|chart|mode=lines|x=S|y=option_rho|title=Rho|>

|>
|>
|>
|>
"""