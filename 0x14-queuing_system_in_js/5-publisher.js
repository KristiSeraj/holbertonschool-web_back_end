import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

async function publishMessage(message, time) {
    await new Promise(resolve => setTimeout(resolve, time));
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
