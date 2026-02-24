import json
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone as phone_timezone
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Branding
TOOL_NAME = "NORRY_GHOSTY"
AUTHOR = "NORRIS"

@app.route('/')
def index():
    return render_template('index.html', tool_name=TOOL_NAME, author=AUTHOR)

@app.route('/api/ip', methods=['POST'])
def ip_track():
    data = request.json
    ip = data.get('target')
    if not ip:
        return jsonify({"error": "No IP provided"}), 400
    
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        
        # Add Google Maps link if latitude/longitude exist
        if "latitude" in ip_data and "longitude" in ip_data:
            lat = int(ip_data['latitude'])
            lon = int(ip_data['longitude'])
            ip_data["maps"] = f"https://www.google.com/maps/@{lat},{lon},8z"
            
        return jsonify(ip_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/phone', methods=['POST'])
def phone_track():
    data = request.json
    number = data.get('target')
    if not number:
        return jsonify({"error": "No phone number provided"}), 400
    
    try:
        # Default region ID for Indonesia
        default_region = "ID" 
        parsed_number = phonenumbers.parse(number, default_region)
        
        results = {
            "Location": geocoder.description_for_number(parsed_number, "en"),
            "Region Code": phonenumbers.region_code_for_number(parsed_number),
            "Timezone": ', '.join(phone_timezone.time_zones_for_number(parsed_number)),
            "Operator": carrier.name_for_number(parsed_number, "en"),
            "Valid number": phonenumbers.is_valid_number(parsed_number),
            "Possible number": phonenumbers.is_possible_number(parsed_number),
            "International format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "Mobile format": phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True),
            "Original number": parsed_number.national_number,
            "E.164 format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "Country code": parsed_number.country_code,
            "Local number": parsed_number.national_number,
        }
        
        number_type = phonenumbers.number_type(parsed_number)
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            results["Type"] = "Mobile number"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            results["Type"] = "Fixed-line number"
        else:
            results["Type"] = "Other type of number"
            
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/username', methods=['POST'])
def username_track():
    data = request.json
    username = data.get('target')
    if not username:
        return jsonify({"error": "No username provided"}), 400
    
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
        {"url": "https://www.youtube.com/{}", "name": "Youtube"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
        {"url": "https://www.medium.com/@{}", "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
        {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://www.telegram.me/{}", "name": "Telegram"}
    ]
    
    results = []
    for site in social_media:
        url = site['url'].format(username)
        try:
            # Added a timeout to avoid hanging
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                results.append({"name": site['name'], "url": url, "status": "found"})
            else:
                results.append({"name": site['name'], "url": url, "status": "not found"})
        except:
            results.append({"name": site['name'], "url": url, "status": "error"})
            
    return jsonify(results)

@app.route('/api/myip')
def my_ip():
    try:
        response = requests.get('https://api.ipify.org/')
        return jsonify({"ip": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
