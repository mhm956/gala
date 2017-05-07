from phue import Bridge

b = Bridge('192.168.0.103')

# If running for the first time, press button on bridge and run with b.connect() uncommented
# b.connect()


def phue_lights(color=None, light_state=None, room=None):
    action_flag = False
    if room:
        uuid = int(b.get_light_id_by_name(room))
        if light_state == "on":
            b.set_light(uuid, 'on', True)
            action_flag = True
        elif light_state == "off":
            b.set_light(uuid, 'on', False)
            action_flag = True
        elif light_state == "dim":
            b.set_light(uuid, 'bri', 50)
            action_flag = True
        elif light_state == "brighten":
            b.set_light(uuid, 'bri', 200)
            action_flag = True
        else:
            pass

        if color:
            if color == 'red':
                b.set_light(uuid, 'hue', 0)
                action_flag = True
            elif color == 'orange':
                b.set_light(uuid, 'hue', 8000)
                action_flag = True
            elif color == 'blue':
                b.set_light(uuid, 'hue', 46920)
                action_flag = True
            elif color == 'green':
                b.set_light(uuid, 'hue', 22500)
                action_flag = True
            else:
                pass

    return action_flag
