# Aircraft Design Optimizer

This project models and optimizes aircraft wing design using physics-based aerodynamic equations.

## Overview
The optimizer evaluates different wing areas and angles of attack to identify the most efficient configuration for flight.

## Methodology
- Lift and drag are calculated using standard aerodynamic equations
- A simplified lift model accounts for stall behavior beyond 12° angle of attack
- Designs must satisfy a minimum lift requirement
- Efficiency is maximized using the lift-to-drag ratio (L/D)
- Realistic constraints (e.g., maximum wing area) are applied

## Features
- Iterative search over design parameters
- Constraint-based filtering
- Performance optimization using L/D ratio
- Clear output and interpretation of results

## Example Output
The program identifies the wing configuration that:
- Meets lift requirements
- Minimizes aerodynamic inefficiency
- Operates within realistic physical constraints

## Purpose
This project demonstrates how computational methods can be used to explore engineering trade-offs in aircraft design.
