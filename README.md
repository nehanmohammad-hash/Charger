# Circuit design of 5V USB Charger

## Overview
This repository contains comprehensive documentation, mathematical derivations, measurements, and design files detailing the step-by-step engineering and electronic operation of a DIY 5V USB charger[cite: 10, 11]. Moving from first-principles signal analysis to physical hardware implementation, this project serves as both an educational guide and a practical reference for power electronics design[cite: 11].

---

## Key Stages & Project Structure

The project is structured into logical engineering blocks, tracing energy conversion from the AC mains to the regulated DC USB output[cite: 17]:

1. **Periodic Signals & Fourier Analysis**
   * Analysis of full-wave rectified waveforms[cite: 11].
   * Complex and real Fourier series derivations, harmonic evaluations, and symmetry properties[cite: 11, 13, 14].
   * Fourier transform properties, Dirac delta functions, and spectral line representations[cite: 14, 15].

2. **Transformer & AC Input Stage**
   * Examination of RMS vs. peak voltage relationships for sinusoidal inputs[cite: 17, 18].
   * Step-down transformer operation, turns-ratio calculations, and galvanic isolation principles[cite: 18].

3. **Full-Wave Bridge Rectification**
   * Diode conduction mechanics and bridge topology[cite: 18, 19].
   * First-order forward voltage drop accounting and resultant pulsating DC characteristics (100 Hz ripple frequency from a 50 Hz mains input)[cite: 18, 19].

4. **Smoothing & Reservoir Capacitance**
   * Capacitor charge/discharge dynamics and energy-reservoir action between ripple peaks[cite: 19, 20].
   * Mathematical estimation of peak-to-peak ripple voltage ($V_{r(pp)}$) as a function of load current and capacitance[cite: 20].

5. **Regulation & Power Conversion**
   * Comparative analysis of linear regulators (e.g., LM7805) versus switching buck converters (e.g., LM2596)[cite: 20, 21].
   * Evaluation of power dissipation, thermal behavior, headroom requirements, and conversion efficiency[cite: 21, 22].

6. **USB Output Interface & Compliance**
   * Analysis of standard downstream ports (SDP), charging downstream ports (CDP), and dedicated charging ports (DCP) under BC1.2 specifications[cite: 22, 23].
   * Data line ($D+/D-$) legacy voltage signatures and USB Type-C current advertisement protocols[cite: 22, 24].

---

## Repository Contents
* **`main.pdf` / Project Report:** The comprehensive draft detailing mathematical proofs, theoretical frameworks, and design considerations[cite: 11].
* **Measurements:** Primary laboratory data and oscilloscope/multimeter measurements captured from a working physical prototype.
* **Code:** Python scripts used for numerical verification of Fourier coefficients, spectral plots, and filter frequency responses.

## Usage & Verification
Python scripts accompanying the respective sections can be executed to verify the analytical Fourier series and transform plots against theoretical models. 

---
*Developed as part of an engineering investigation into practical power supply design.*
