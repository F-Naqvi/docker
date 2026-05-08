from flask import Flask
import redis
import os
import socket


app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

client = redis.Redis(
    host=redis_host,
    port=redis_port,
    decode_responses=True
)

# Route 1 - Welcome Message
@app.route('/')
def welcome():
    return f"Welcome! Handled by: {socket.gethostname()}"

# Route 2 - Visitor Count
@app.route('/count')
def count():
    visitor_count = client.incr('visitor_count')
    return f'you are visitor number: {visitor_count}'

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)
