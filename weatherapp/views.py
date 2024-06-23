from django.shortcuts import render
import requests
import datetime

def home(request):
    weather_data = []
    cities = ['Mumbai', 'Delhi', 'Bangalore','Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur',
    'Lucknow', 'Kanpur', 'Nagpur', 'Visakhapatnam', 'Indore', 'Thane', 'Bhopal', 'Pimpri-Chinchwad', 'Patna',
    'Vadodara', 'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan-Dombivli',
    'Vasai-Virar', 'Varanasi', 'Srinagar', 'Aurangabad', 'Dhanbad', 'Amritsar', 'Navi Mumbai', 'Allahabad', 
    'Howrah', 'Ranchi', 'Gwalior', 'Jabalpur', 'Coimbatore', 'Vijayawada', 'Jodhpur', 'Madurai', 'Raipur', 
    'Kota', 'Guwahati', 'Chandigarh', 'Solapur', 'Hubli-Dharwad', 'Bareilly', 'Moradabad', 'Mysore', 'Gurgaon', 
    'Aligarh', 'Jalandhar', 'Tiruchirappalli', 'Bhubaneswar', 'Salem', 'Warangal', 'Guntur', 'Bhiwandi', 
    'Saharanpur', 'Gorakhpur', 'Bikaner', 'Amravati', 'Noida', 'Jamshedpur', 'Bhilai', 'Cuttack', 'Firozabad', 
    'Kochi', 'Nellore', 'Bhavnagar', 'Dehradun', 'Durgapur', 'Asansol', 'Rourkela', 'Nanded', 'Kolhapur', 
    'Ajmer', 'Akola', 'Gulbarga', 'Jamnagar', 'Ujjain', 'Loni', 'Siliguri', 'Jhansi', 'Ulhasnagar', 'Jammu', 
    'Sangli-Miraj & Kupwad', 'Mangalore', 'Erode', 'Belgaum', 'Ambattur', 'Tirunelveli', 'Malegaon', 'Gaya', 
    'Jalgaon', 'Udaipur', 'Maheshtala', 'Tirupur', 'Davanagere', 'Kozhikode', 'Akbarpur', 'Shahjahanpur', 
    'Satara', 'Bijapur', 'Rampur', 'Shivamogga', 'Chandrapur', 'Junagadh', 'Thrissur', 'Alwar', 'Bardhaman', 
    'Kulti', 'Nizamabad', 'Parbhani', 'Tumkur', 'Khammam', 'Ozhukarai', 'Bihar Sharif', 'Panipat', 'Darbhanga', 
    'Bally', 'Aizawl', 'Dewas', 'Ichalkaranji', 'Karnal', 'Bathinda', 'Jalna', 'Eluru', 'Kirari Suleman Nagar', 
    'Barasat', 'Purnia', 'Satna', 'Mau', 'Sonipat', 'Farrukhabad', 'Sagar', 'Rourkela', 'Durg', 'Imphal', 
    'Ratlam', 'Hapur', 'Arrah', 'Anantapur', 'Karimnagar', 'Etawah', 'Ambernath', 'North Dumdum', 'Bharatpur', 
    'Begusarai', 'New Delhi', 'Gandhidham', 'Baranagar', 'Tiruvottiyur', 'Puducherry', 'Sikar', 'Thoothukudi', 
    'Rewa', 'Mirzapur', 'Raichur', 'Pali', 'Ramagundam', 'Haridwar', 'Vijayanagaram', 'Katihar', 'Kollam', 
    'Hosur', 'Nagercoil', 'Thanjavur', 'Murwara', 'Naihati', 'Sambhal', 'Nadiad', 'Yamunanagar', 'English Bazar', 
    'Eluru', 'Sambalpur', 'Junagadh', 'Baripada', 'Saharsa', 'Hindupur', 'Puri', 'Robertsonpet', 'Erode', 
    'Batala', 'Haldia', 'Khandwa', 'Machilipatnam', 'Shimla', 'Karaikudi', 'Gudivada', 'Medininagar', 'Balurghat', 
    'Chandannagar', 'Hosangabad', 'Adilabad', 'Jorhat', 'Viluppuram', 'Hazaribagh', 'Bhimavaram', 'Kumbakonam', 
    'Bongaigaon', 'Moga', 'Tiruvannamalai', 'Kaithal', 'Jaunpur', 'Madhyamgram', 'Hathras', 'Patan', 'Palghar', 
    'Anand', 'Villupuram', 'Bhind', 'Shimoga', 'Kishanganj', 'Motihari', 'Gangapur', 'Karaikal', 'Sahibganj', 
    'Amroha', 'Mahbubnagar', 'Chittoor', 'Palakkad', 'Tadipatri', 'Kalyani', 'Nagaur', 'Port Blair', 'Itarsi', 
    'Cuttack', 'Deoli', 'Pilibhit', 'Satna', 'Haldwani', 'Darjiling', 'Jind', 'Chhindwara', 'Santipur', 'Balaghat', 
    'Hoshiarpur', 'Malda', 'Kashipur', 'Banda', 'Jalpaiguri', 'Hugli-Chinsurah', 'Suri', 'Navsari', 'Bhadrak', 
    'Rishra', 'Chandrapur', 'Bhilai', 'Cuddalore', 'Dehri', 'Dibrugarh', 'Madanapalle', 'Chitradurga', 'Vaniyambadi', 
    'Bhimavaram', 'Kolkata', 'Chennai', 'Hyderabad', 'Ahmedabad', 'Surat', 'Pune'  ]
    
    for city in cities:
        city_weather = {}
        if 'city' in request.POST and request.POST['city'].strip():
            city_to_search = request.POST['city'].strip()
        else:
            city_to_search = None
        
        if city_to_search and city.lower() != city_to_search.lower():
            continue
        
        api_key = '14071d9d2ee599df4d6e134d7f3ac245'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                temperature = data['main']['temp']
                description = data['weather'][0]['description'].capitalize()
                icon = data['weather'][0]['icon']
                day = datetime.date.today()
                
                city_weather = {
                    'city': city.capitalize(),
                    'temperature': temperature,
                    'description': description,
                    'icon': icon,
                    'day': day,
                    'exception_occurred': False,
                }
            else:
                city_weather = {
                    'city': city.capitalize(),
                    'temperature': None,
                    'description': None,
                    'icon': None,
                    'day': datetime.date.today(),
                    'exception_occurred': True,
                }
        except Exception as e:
            city_weather = {
                'city': city.capitalize(),
                'temperature': None,
                'description': None,
                'icon': None,
                'day': datetime.date.today(),
                'exception_occurred': True,
            }
        
        if city_weather:
            weather_data.append(city_weather)
    
    return render(request, 'weatherapp/index.html', {'weather_data': weather_data})
