"""
Part - 2
Congestion Control
Problem: Implement a simple congestion control algorithm, such as Additive Increase
        Multiplicative Decrease (AIMD), to handle congestion in a network. Do print the
        congestion window size in order to verify the working of AIMD. To introduce congestion
        into the network, you can add ‘loss probability’ while sending and receiving packets. Try
        different variations of the slow start threshold to see what works best.
"""

from math import floor
import random

class CongestionControl:
    def __init__(self, initial_ws, max_ws, min_ws, increase_factor, decrease_factor, loss_probability):
        self.ws = initial_ws
        self.max_ws = max_ws
        self.min_ws = min_ws
        self.threshold = max_ws // 2
        self.increase_factor = increase_factor
        self.decrease_factor = decrease_factor
        self.loss_probability = loss_probability

    def simulate_network(self):
        return random.random() > self.loss_probability

    def send_packet(self):
        # Send packet over the network
        if self.ws < self.max_ws:
            self.ws += self.increase_factor

    def receive_ack(self, transmission):
        # Receive acknowledgement from the receiver
        if transmission:
            if self.ws < self.threshold:
                self.ws += 1
            else:
                self.ws += self.increase_factor
        else:
            self.ws = floor(self.ws * self.decrease_factor)
            if self.ws < self.min_ws:
                self.ws = self.min_ws

    def run_simulation(self, iterations):
        for _ in range(iterations):
            if self.simulate_network():
                self.send_packet()
                self.receive_ack(True)
                print("WS: {} \tSUCCESS".format(self.ws))
            else:
                self.receive_ack(False)
                print("WS: {} \tPACKET LOSS".format(self.ws))

def main():
    initial_ws = 1
    max_ws = 10
    min_ws = 1
    increase_factor = 1
    decrease_factor = 1/2
    loss_probability = 0.3
    aimd = CongestionControl(initial_ws, max_ws, min_ws, increase_factor, decrease_factor, loss_probability)
    aimd.run_simulation(100)

if __name__ == '__main__':
    main()