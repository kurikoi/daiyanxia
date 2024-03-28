#!/usr/bin/env python
# coding: utf-8

# In[3]:


class TNE: 
    def __init__(self):
        self.diesel_engine_status = 'off' 
        self.power_status = 'stopped' 
        self.robot_status = 'stopped' 
        self.operations = { 'diesel engine': self.set_diesel_engine_status, 'power switch': self.set_power_status, 'robot': self.set_robot_status }
        def set_diesel_engine_status(self, status): 
            if status in ['on', 'on device', 'off', 'off device']: 
                self.diesel_engine_status = 'on'
                if status.starts with('on') 
                else 'off' print('Diesel engine is now', 'running' if status.startswith('on') else 'stopped') else: print('Invalid command')
                    def set_power_status(self, status): 
                        if status in ['on', 'on device', 'off', 'off device', 'check', 'check status']: 
                            if status.startswith('check'): print('Power is currently', self.power_status) 
                                else: self.power_status = 'running' 
                                    if status.startswith('on') 
                                    else 'stopped' print('Power is now', self.power_status) 
                                    else: print('Invalid command') 
                                        def set_robot_status(self, status): 
                                            if status in ['forward', 'f', 'rotate', 'r', 'stop', 's']: 
                                                self.robot_status = status 
                                                if len(status) == 1 
                                                else 'forward' 
                                                if status == 'f'
                                                else 'rotate'
                                                if status == 'r'
                                                else 'stop' print('Robot is now', self.robot_status) 
                                                else: print('Invalid command') 
                                                    def perform_operation(self, operation, status): method = self.operations.get(operation)
                                                        if method: method(status)
                                                            else: print('Invalid command') 
                                                                T = TNE()
                                                                operation = input("Please input the operation (choose from Diesel engine, Power switch, and Robot)\n").lower() status = input("Please input the status\n").lower() T.perform_operation(operation, status)


# In[4]:


class TNE: 
    def __init__(self):
        self.diesel_engine_status = 'off' 
        self.power_status = 'stopped' 
        self.robot_status = 'stopped' 
        self.operations = { 'diesel engine': self.set_diesel_engine_status, 'power switch': self.set_power_status, 'robot': self.set_robot_status }
        def set_diesel_engine_status(self, status): 
            if status in ['on', 'on device', 'off', 'off device']: 
                self.diesel_engine_status = 'on'
                if status.starts with('on') 
                else 'off' print('Diesel engine is now', 'running' if status.startswith('on') else 'stopped') else: print('Invalid command')
                    def set_power_status(self, status): 
                        if status in ['on', 'on device', 'off', 'off device', 'check', 'check status']: 
                            if status.startswith('check'): print('Power is currently', self.power_status) 
                                else: self.power_status = 'running' 
                                    if status.startswith('on') 
                                    else 'stopped' print('Power is now', self.power_status) 
                                    else: print('Invalid command') 
                                        def set_robot_status(self, status): 
                                            if status in ['forward', 'f', 'rotate', 'r', 'stop', 's']: 
                                                self.robot_status = status 
                                                if len(status) == 1 
                                                else 'forward' 
                                                if status == 'f'
                                                else 'rotate'
                                                if status == 'r'
                                                else 'stop' print('Robot is now', self.robot_status) 
                                                else: print('Invalid command') 
                                                    def perform_operation(self, operation, status): method = self.operations.get(operation)
                                                        if method: method(status)
                                                            else: print('Invalid command') 
                                                                T = TNE()
                                                                operation = input("Please input the operation (choose from Diesel engine, Power switch, and Robot)\n").lower() status = input("Please input the status\n").lower() T.perform_operation(operation, status)


# In[ ]:




