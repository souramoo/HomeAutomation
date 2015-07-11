# Home Automation
Python-based modular home automation system.

## What is it?
I wrote this in python to simplify my home automation control. The other approaches I have seen are very complicated and are slow on my Raspberry Pi, and hard to customise to do what I want with my own custom bindings.

This system provides a simple plug and play architecture, where I can write Drivers (outputs) and Sensors (inputs, which can trigger events into a queue for processing by EventProcessors or simply provide a passive reading when needed)

EventProcessors can be subclasses to provide a way for different triggers to provide different outputs. A HTTP API is provided (implemented as a sensor) to allow control over devices over wifi, for example.
