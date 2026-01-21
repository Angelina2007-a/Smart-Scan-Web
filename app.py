from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# --- PRODUCT DATABASE ---
# Demo Date set to: 2025-12-27
# Lion Dates is set to an expired date to demonstrate the Red Alert.
PRODUCT_DB = {
    "890123456701": {
        "name": "Glucose-C Orange", 
        "brand": "Generic", 
        "price": 50.00, 
        "expiry": "2026-03-01"
    },
    "8901138848484": {
        "name": "Aloe Vera Face Gel", 
        "brand": "Himalaya", 
        "price": 90.00, 
        "expiry": "2028-04-01"
    },
    "890297903528": {
        "name": "Green Snack Pack", 
        "brand": "CavinKare", 
        "price": 10.00, 
        "expiry": "2026-02-01"
    },
    "8901396315803": {
        "name": "Liquid Handwash", 
        "brand": "Dettol", 
        "price": 35.00, 
        "expiry": "2027-07-01"
    },
    "890123456707": {
        "name": "Lion Dates Syrup", 
        "brand": "Lion", 
        "price": 212.00, 
        "expiry": "2025-12-03" # EXPIRED
    },
    "8906037000410": {
        "name": "Ayurvedic Medicine", 
        "brand": "Pankajakasthuri", 
        "price": 380.00, 
        "expiry": "2027-05-01"
    }
}

# --- ROUTES ---

@app.route('/')
def login_page():
    """Serves the login portal."""
    return render_template('login.html')

@app.route('/billing')
def billing_page():
    """Serves the main POS terminal after login."""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    """Handles barcode scanning and expiry validation."""
    data = request.get_json()
    barcode = data.get('barcode', '')
    
    # Static date for consistent hackathon demonstration
    today = "2025-12-27"
    
    if barcode not in PRODUCT_DB:
        return jsonify({
            "status": "NOT_FOUND", 
            "message": "⚠️ UNKNOWN PRODUCT: Not in local inventory."
        })
    
    product = PRODUCT_DB[barcode]
    
    # Expiry Check Logic
    if product['expiry'] < today:
        return jsonify({
            "status": "EXPIRED", 
            "message": f"🚫 SECURITY ALERT: ITEM EXPIRED ({product['expiry']})!"
        })

    return jsonify({
        "status": "VALID", 
        "product": product, 
        "message": "✅ Item Verified & Compliant"
    })

if __name__ == '__main__':
    # host='0.0.0.0' allows access from your mobile phone on the same Wi-Fi
    app.run(debug=True, host='0.0.0.0', port=5000)