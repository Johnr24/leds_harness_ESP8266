# LED Harness for EMF 2026

This project controls LED animations synchronized to button presses using an ESP8266 microcontroller.

## Features
- Multiple LED animation modes
- Tap synchronization for tempo matching
- Central hexagon visualization

## Hardware Requirements
- ESP8266 microcontroller
- Addressable LED strip (WS2812B or compatible)
- Push button

## Wiring
- LED Data Pin: D5 (GPIO14)
- Button Pin: D2 (GPIO4)

## Usage
1. **Short Press**: Cycle through animation modes
2. **Long Press (1 second)**:
   - In normal mode: Enter tap sync mode
   - In sync mode: Exit without saving taps
3. **In Sync Mode**:
   - Short presses record taps for tempo synchronization
   - After 8 taps, tempo is calculated automatically

## Installation
1. Install PlatformIO
2. Clone this repository
3. Connect hardware
4. Build and upload:

```bash
pio run -t upload
```

## Dependencies
- FastLED
- Custom RGB to LAB conversion
