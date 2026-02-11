page_surfaces = """

<|d-flex|

<|{show_pane}|pane|persistent|show_button|width=300px|
<|container|

<br/>
<|card|
<|navbar|lov={[('/greeks', '2D Greeks'),('/surface', '3D Surface')]}|>
|>

## Variables

**Option Type**<br/>
<|{option_type}|toggle|lov=Call; Put|on_change=update_surfaces|>

**Strike price:** <|{K}|text|><br/>
<|{K}|slider|min=50|max=150|on_change=update_surfaces|>

**Volatility:** <|{sigma}|text|><br/>
<|{sigma}|slider|min=0.1|max=2|step=0.1|on_change=update_surfaces|>

**Interest rate:** <|{r}|text|><br/>
<|{r}|slider|min=0.0|max=0.2|step=0.01|on_change=update_surfaces|>

<|Update Surfaces|button|on_action=update_surfaces|>

|>
|>

<|
<|container|

# Option Greeks Surface 
 
<|Computing...|progress|value={progress_value}|show_value=true|linear=true|>

<|layout|columns=1 1|

<|chart|figure={fig_surface_price}|decimate=0.1|>

<|chart|figure={fig_surface_delta}|decimate=0.1|>

<|chart|figure={fig_surface_gamma}|decimate=0.1|>

<|chart|figure={fig_surface_vega}|decimate=0.1|>

<|chart|figure={fig_surface_theta}|decimate=0.1|>

<|chart|figure={fig_surface_rho}|decimate=0.1|>

|>
|>
|>
|>
"""