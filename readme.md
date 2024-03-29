
# Updates!

For the light trickle of people I've seen cloning and visiting. I'm presently at the end of a big house move and still in the throes of starting a new job. However, in a few months updates to this and adjacent repos will resume (although at a slower pace). If you are interested in contributing, please feel free to let me know, open an issue, make a PR and I will do my best to get back to you.

# OpenHubAPI

A GUI for managing iOT hubs, hardware, and homekit accessory configurations for [OpenHub](https://github.com/ganonp/OpenHub) and [OpenController](https://github.com/ganonp/OpenController).
 

Main features:

* Create, delete, rename OpenHub hubs from one GUI.
* Add and manage hardware to any OpenHub hub on your network with an easy to use interface.
* Collect statistics on hardware readings.
* Create HomeKit Accessories using combinations of hardware outputs, mathmatical transformations, and hardware stats.


## Installation 


```
$ sudo apt-get update
$ sudo apt-get install python3-pip --fix-missing -y
$ sudo python3 -m pip install openhub-api
$ sudo python3 -m OpenHubAPI.install
```

## Configuration / Setup

1. Install OpenHubAPI on a Raspberry Pi.
2. Install [OpenHub](https://github.com/ganonp/OpenHub) on the same or a different device.
3. (Optional) Install  [OpenController](https://github.com/ganonp/OpenController) on a Raspberry Pi Pico and connect to to the OpenHub device.
4. Hub will automatically find and add itself to OpenHubAPI on the same network.
5. Create user on OpenHubAPI
6. Add user to newly added hub.
7. Create and configure hardware.
8. Create and configure channels on hardware.
9. Create and configure accessories with channels.
10. Reboot device running [OpenHub](https://github.com/ganonp/OpenHub).
11. Add accessories to HomeKit.

## UI 


<img width="1622" alt="Screen Shot 2022-01-27 at 3 45 55 PM" src="https://user-images.githubusercontent.com/3904428/151461905-d9f48712-7256-4d01-98a7-02211f3cffd3.png">
<img width="1630" alt="Screen Shot 2022-01-27 at 3 45 20 PM" src="https://user-images.githubusercontent.com/3904428/151461972-b9c5a553-09c5-45f2-b833-a7ff027e07e7.png">
<img width="1635" alt="Screen Shot 2022-01-27 at 3 45 42 PM" src="https://user-images.githubusercontent.com/3904428/151462009-85e4a45e-471f-4c59-9c53-028f1a72450b.png">
