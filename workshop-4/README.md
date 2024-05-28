# Workshop 4 - Solution

This is a workshop where lays the backend of a car dealership

## Requirements

The requirements for this workshop are presented as follows:
- Cars must have next attributes: transmission, chassis, year, trade, model, combustible
type, and engine.
- Yacht must have next attributes: length, weight, year, trade, model, engine.
- Trucks and Motorcycles will keep same attributes as before. However, just for trucks
you need to calculate the gas consumption due to regulations of both USA and Europe.
- You need to add next vehicles options, and you must define the appropriate atteibutes
they need: Helicopter, Scooter.
- All engines must have next attributes: stability, power, weight, dimensions, torque,
and maximum speed.
- There are 3 types of engines: _Gas Engine_, _Electric Engine_ and _Hybrid Engine_, each of these 3 engines has 2 variations: _Expensive_ and _Cheap_

## Business Rules

- Every vehicle just have chassis of type A or B.
- Gas consumption is based on engine information...
- Gas consumption is based on next equation. 
  `1.1 ∗ engine.potency + 0.2 ∗ engine.weight - (0.3 if A or 0.5 if B)`
