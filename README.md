# Package Sorting Automation

Robotic arm package sorting system for Thoughtful's factory that categorizes packages into STANDARD, SPECIAL, or REJECTED stacks based on size and weight.

## Features

- Categorizes packages based on:
  - Bulky status (volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm)
  - Heavy status (mass ≥ 20 kg)
- Three possible outputs:
  - `STANDARD`: Neither bulky nor heavy
  - `SPECIAL`: Either bulky or heavy
  - `REJECTED`: Both bulky and heavy
