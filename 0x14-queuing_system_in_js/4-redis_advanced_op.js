import { createClient, print } from "redis";

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const key = 'HolbertonSchools';

const data = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}

for (const [school, value] of Object.entries(data)) {
    client.hset(key, school, value, print);
}

client.hgetall(key, (err, res) => {
    console.log(res);
});