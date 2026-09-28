from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

router = APIRouter()

# --- HOME PLANNER ---
@router.post("/generate-home", response_class=HTMLResponse)
async def generate_home(
    request: Request, 
    budget: float = Form(5000), 
    lights: int = Form(2),
    fans: int = Form(1),
    lamps: int = Form(1),
    chairs: int = Form(2),
    style: str = Form("modern"),
    preferences: str = Form("")
):
    # Dynamic Unit Prices
    price_per_light = 350.0
    price_per_fan = 2500.0
    price_per_lamp = 1200.0
    price_per_chair = 1800.0
    
    total_lights_cost = lights * price_per_light
    total_fans_cost = fans * price_per_fan
    total_lamps_cost = lamps * price_per_lamp
    total_chairs_cost = chairs * price_per_chair
    
    total_estimated = total_lights_cost + total_fans_cost + total_lamps_cost + total_chairs_cost
    remaining_budget = budget - total_estimated
    
    # Pre-calculate color so it doesn't mess up the f-string curly braces
    budget_color = '#bfdbfe' if remaining_budget >= 0 else '#fca5a5'
    
    return HTMLResponse(content=f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Budget Plan</title>
        <meta charset="UTF-8">
    </head>
    <body style="margin: 0; padding: 0;">
        <div style="font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f8fafc; min-height: 100vh; padding-bottom: 50px;">
            <div style="background: linear-gradient(135deg, #0f172a, #1e3a8a, #1e40af); color: white; text-align: center; padding: 35px 20px;">
                <h1 style="font-size: 28px; font-weight: 800; margin: 0 0 6px 0;">Home Interior Budget Plan</h1>
                <p style="font-size: 14px; color: #cbd5e1; margin: 0;">Tailored recommendations for your {style} style.</p>
            </div>
            <div style="max-width: 850px; margin: 30px auto; padding: 0 20px;">
                <div style="background: linear-gradient(135deg, #1e3a8a, #2563eb); color: white; padding: 16px 24px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; font-weight: 600; font-size: 15px; margin-bottom: 25px;">
                    <div>Total Budget: <span>Rs. {budget:,.2f}</span></div>
                    <div>Style: <span style="text-transform: capitalize;">{style}</span></div>
                    <div>Remaining Budget: <span style="color: {budget_color};">Rs. {remaining_budget:,.2f}</span></div>
                </div>

                <!-- Lighting Table -->
                <div style="background: white; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 25px; padding: 20px;">
                    <h3 style="margin: 0 0 15px 0; font-size: 16px; color: #0f172a;">💡 Lighting (Subtotal: Rs. {total_lights_cost:,.2f})</h3>
                    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left;">
                        <tr style="border-bottom: 2px solid #f1f5f9; color: #475569;"><th style="padding: 10px;">Item</th><th style="padding: 10px;">Price</th><th style="padding: 10px;">Quantity</th></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px; font-weight: 600;">LED Bulbs</td><td style="padding: 12px 10px;">Rs. {total_lights_cost:,.2f}</td><td style="padding: 12px 10px;">{lights}</td></tr>
                    </table>
                </div>

                <!-- Ceiling Fans Table -->
                <div style="background: white; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 25px; padding: 20px;">
                    <h3 style="margin: 0 0 15px 0; font-size: 16px; color: #0f172a;">🌀 Ceiling Fans (Subtotal: Rs. {total_fans_cost:,.2f})</h3>
                    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left;">
                        <tr style="border-bottom: 2px solid #f1f5f9; color: #475569;"><th style="padding: 10px;">Item</th><th style="padding: 10px;">Price</th><th style="padding: 10px;">Quantity</th></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px; font-weight: 600;">Ceiling Fan</td><td style="padding: 12px 10px;">Rs. {total_fans_cost:,.2f}</td><td style="padding: 12px 10px;">{fans}</td></tr>
                    </table>
                </div>

                <!-- Lamps Table -->
                <div style="background: white; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 25px; padding: 20px;">
                    <h3 style="margin: 0 0 15px 0; font-size: 16px; color: #0f172a;">🏮 Standing Lamps (Subtotal: Rs. {total_lamps_cost:,.2f})</h3>
                    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left;">
                        <tr style="border-bottom: 2px solid #f1f5f9; color: #475569;"><th style="padding: 10px;">Item</th><th style="padding: 10px;">Price</th><th style="padding: 10px;">Quantity</th></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px; font-weight: 600;">Standing Lamp</td><td style="padding: 12px 10px;">Rs. {total_lamps_cost:,.2f}</td><td style="padding: 12px 10px;">{lamps}</td></tr>
                    </table>
                </div>

                <!-- Chairs Table -->
                <div style="background: white; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 25px; padding: 20px;">
                    <h3 style="margin: 0 0 15px 0; font-size: 16px; color: #0f172a;">🪑 Dining Chairs (Subtotal: Rs. {total_chairs_cost:,.2f})</h3>
                    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left;">
                        <tr style="border-bottom: 2px solid #f1f5f9; color: #475569;"><th style="padding: 10px;">Item</th><th style="padding: 10px;">Price</th><th style="padding: 10px;">Quantity</th></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px; font-weight: 600;">Chairs</td><td style="padding: 12px 10px;">Rs. {total_chairs_cost:,.2f}</td><td style="padding: 12px 10px;">{chairs}</td></tr>
                    </table>
                </div>

                <div style="text-align: center;"><a href="/home_planner" style="background: #0f172a; color: white; padding: 10px 25px; border-radius: 6px; text-decoration: none;">⬅ Back</a></div>
            </div>
        </div>
    </body>
    </html>
    """)

# --- JEWELRY PLANNER ---
@router.post("/generate-jewelry", response_class=HTMLResponse)
async def generate_jewelry(
    request: Request,
    budget: float = Form(10000),
    rings: int = Form(1),
    necklaces: int = Form(1),
    earrings: int = Form(1),
    metal: str = Form("gold")
):
    ring_price = 3500.0 if metal == "gold" else 1500.0
    necklace_price = 12000.0 if metal == "gold" else 4500.0
    earring_price = 4000.0 if metal == "gold" else 2000.0
    
    total_cost = (rings * ring_price) + (necklaces * necklace_price) + (earrings * earring_price)
    remaining = budget - total_cost

    budget_color = '#fef08a' if remaining >= 0 else '#fca5a5'

    return HTMLResponse(content=f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jewelry Budget Plan</title>
        <meta charset="UTF-8">
    </head>
    <body style="margin: 0; padding: 0;">
        <div style="font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f8fafc; min-height: 100vh; padding-bottom: 50px;">
            <div style="background: linear-gradient(135deg, #854d0e, #a16207); color: white; text-align: center; padding: 35px 20px;">
                <h1 style="font-size: 28px; font-weight: 800; margin: 0 0 6px 0;">Jewelry Budget Plan</h1>
                <p style="font-size: 14px; color: #fef08a; margin: 0;">Custom plan for {metal.capitalize()} collection.</p>
            </div>
            <div style="max-width: 850px; margin: 30px auto; padding: 0 20px;">
                <div style="background: linear-gradient(135deg, #713f12, #a16207); color: white; padding: 16px 24px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; font-weight: 600; font-size: 15px; margin-bottom: 25px;">
                    <div>Total Budget: <span>Rs. {budget:,.2f}</span></div>
                    <div>Metal: <span style="text-transform: capitalize;">{metal}</span></div>
                    <div>Remaining Budget: <span style="color: {budget_color};">Rs. {remaining:,.2f}</span></div>
                </div>

                <div style="background: white; border-radius: 10px; border: 1px solid #e2e8f0; padding: 20px;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left;">
                        <tr style="border-bottom: 2px solid #f1f5f9; color: #475569;"><th style="padding: 10px;">Item</th><th style="padding: 10px;">Subtotal</th><th style="padding: 10px;">Quantity</th></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px;">Rings</td><td style="padding: 12px 10px;">Rs. {rings * ring_price:,.2f}</td><td style="padding: 12px 10px;">{rings}</td></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px;">Necklaces</td><td style="padding: 12px 10px;">Rs. {necklaces * necklace_price:,.2f}</td><td style="padding: 12px 10px;">{necklaces}</td></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px;">Earrings</td><td style="padding: 12px 10px;">Rs. {earrings * earring_price:,.2f}</td><td style="padding: 12px 10px;">{earrings}</td></tr>
                    </table>
                </div>
                <div style="text-align: center; margin-top: 20px;"><a href="/jewelry_planner" style="background: #713f12; color: white; padding: 10px 25px; border-radius: 6px; text-decoration: none;">⬅ Back</a></div>
            </div>
        </div>
    </body>
    </html>
    """)

# --- PARTY PLANNER ---
@router.post("/generate-party", response_class=HTMLResponse)
async def generate_party(
    request: Request,
    budget: float = Form(15000),
    guests: int = Form(10),
    food_per_head: float = Form(300.0),
    decoration_cost: float = Form(2000.0)
):
    total_food = guests * food_per_head
    total_cost = total_food + decoration_cost
    remaining = budget - total_cost

    budget_color = '#fbcfe8' if remaining >= 0 else '#fca5a5'

    return HTMLResponse(content=f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Party Budget Plan</title>
        <meta charset="UTF-8">
    </head>
    <body style="margin: 0; padding: 0;">
        <div style="font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f8fafc; min-height: 100vh; padding-bottom: 50px;">
            <div style="background: linear-gradient(135deg, #831843, #9d174d); color: white; text-align: center; padding: 35px 20px;">
                <h1 style="font-size: 28px; font-weight: 800; margin: 0 0 6px 0;">Party Budget Plan</h1>
                <p style="font-size: 14px; color: #fbcfe8; margin: 0;">Event plan for {guests} guests.</p>
            </div>
            <div style="max-width: 850px; margin: 30px auto; padding: 0 20px;">
                <div style="background: linear-gradient(135deg, #831843, #9d174d); color: white; padding: 16px 24px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; font-weight: 600; font-size: 15px; margin-bottom: 25px;">
                    <div>Total Budget: <span>Rs. {budget:,.2f}</span></div>
                    <div>Guests: <span>{guests}</span></div>
                    <div>Remaining Budget: <span style="color: {budget_color};">Rs. {remaining:,.2f}</span></div>
                </div>

                <div style="background: white; border-radius: 10px; border: 1px solid #e2e8f0; padding: 20px;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left;">
                        <tr style="border-bottom: 2px solid #f1f5f9; color: #475569;"><th style="padding: 10px;">Category</th><th style="padding: 10px;">Cost</th></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px;">Catering / Food ({guests} guests)</td><td style="padding: 12px 10px;">Rs. {total_food:,.2f}</td></tr>
                        <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 12px 10px;">Decoration & Setup</td><td style="padding: 12px 10px;">Rs. {decoration_cost:,.2f}</td></tr>
                    </table>
                </div>
                <div style="text-align: center; margin-top: 20px;"><a href="/party_planner" style="background: #831843; color: white; padding: 10px 25px; border-radius: 6px; text-decoration: none;">⬅ Back</a></div>
            </div>
        </div>
    </body>
    </html>
    """)