# Rates Derivatives Pricing GUI – Python Demo

Python implementation of interest rate derivatives pricing with a lightweight GUI, including Bermudan swaptions, American bond options, and cap/floor instruments.

## Overview
This project demonstrates pricing of interest rate derivatives using a trinomial tree methodology.  
The implementation is written in Python and covers Bermudan swaptions, American bond options, and cap/floor products.

The project focuses on refactoring legacy Jupyter Notebook–based models into a modular, user-friendly application suitable for non-technical users.

## Quantitative Methods
- Short-rate models: Hull–White and Vasicek
- Trinomial tree construction for short-rate term structure
- Numerical approximation techniques for interest rate derivatives

## User Interface
A lightweight GUI built with Tkinter allows users to:
- Upload input data (transaction-level inputs and market data)
- Update mapping files externally (e.g. currency scope, European swaption volatility indices, short-rate model assumptions)
- Generate output files in a designated output directory

## Status
The project is functionally complete.  
The current implementation follows a step-by-step modelling approach, which may become computationally expensive for large-scale datasets.

Potential future improvements include performance optimization using vectorization or concurrent execution (e.g. `concurrent.futures`).

The current version reflects recent independent refactoring work:
- Migration from legacy Jupyter Notebook workflows to a standalone GUI application
- Extension from Vasicek-only modelling to support Hull–White short-rate dynamics

