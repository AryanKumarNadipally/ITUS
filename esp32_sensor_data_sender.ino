#include <WiFi.h>
#include <HTTPClient.h>
#include <Adafruit_SEN5X.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* api_url = "your_supabase_url";
const char* api_key = "your_supabase_api_key";

Adafruit_SEN5X sen5x;

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    sen5x.begin();
}

void loop() {
    sen5x.measure();
    float temperature = sen5x.getTemperature();
    float humidity = sen5x.getHumidity();
    float pm1 = sen5x.getPM1();
    float pm2_5 = sen5x.getPM2_5();
    float pm10 = sen5x.getPM10();
    float voc = sen5x.getVOC();
    sendDataToSupabase(temperature, humidity, pm1, pm2_5, pm10, voc);
    delay(900000); // Sending data every 15 minutes
}

void sendDataToSupabase(float temp, float hum, float pm1, float pm2_5, float pm10, float voc) {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(api_url);
        http.addHeader("Content-Type", "application/json");
        http.addHeader("apikey", api_key);

        String postData = "{\"temperature\":" + String(temp) + ", \"humidity\":" + String(hum) + ", \"pm1\":" + String(pm1) + ", \"pm2_5\":" + String(pm2_5) + ", \"pm10\":" + String(pm10) + ", \"voc\":" + String(voc) + "}";
        int httpResponseCode = http.POST(postData);
        if (httpResponseCode > 0) {
            String response = http.getString();
            Serial.println(httpResponseCode);
            Serial.println(response);
        } else {
            Serial.println("Error in sending POST");
            Serial.println(httpResponseCode);
        }
        http.end();
    } else {
        Serial.println("WiFi Disconnected");
    }
}
