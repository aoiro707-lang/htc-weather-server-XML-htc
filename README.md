# HTC Weather Server (for HTC HD2)

Server nhỏ dùng để trả về dữ liệu thời tiết theo XML/JSON phù hợp với app Weather gốc của HTC HD2.

## Cách chạy local

```bash
pip install -r requirements.txt
python htc_weather_server.py
```

Mở trình duyệt:
- XML: http://127.0.0.1:8080/getstaticweather?locCode=Hanoi
- JSON (debug): http://127.0.0.1:8080/getstaticweather_json?locCode=Hanoi

## Deploy lên Render

1. Fork repo này hoặc tải về rồi push lên GitHub.
2. Vào [Render](https://render.com/) → **New Web Service**.
3. Kết nối repo GitHub, chọn branch `main`.
4. Environment: `Python 3`.
5. Start command:
```
gunicorn htc_weather_server:app
```
6. Deploy 🎉

## API Demo

```xml
<weather>
  <location>Hanoi</location>
  <temperature>31</temperature>
  <humidity>72</humidity>
  <wind_speed>4.8</wind_speed>
  <condition>Showers</condition>
</weather>
```
