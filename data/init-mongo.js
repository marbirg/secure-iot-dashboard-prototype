db = new Mongo().getDB("hospital");

db.createUser({
  user: 'nodered',
  pwd: 'nodered',
  roles: [
    {
      role: 'readWrite',
      db: 'hospital',
    },
  ],
});



db.createCollection('devices', { capped: false });
db.createCollection('properties', { capped: false });
