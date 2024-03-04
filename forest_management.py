"""
A module for automatuion of various forest management
particulars
"""

deforestation_level = input('Enter the current deforestation level')

def deforestation_approach(deforestation_level):
    """Decides on what approach to take based on the current deforestation level

    Args:
        deforestation_level (int) : An integer representing the current level of
                                    deforestation

    Result : 
        str :  A string with the strategy to implement based on the current deforestation
                level.
    """
    if deforestation_level <= 0.1:
        print(f'Deforestation low at {deforestation_level}. No immediate action needed.')
    elif 0.1 < deforestation_level <= 0.3:
        print(f'Deforestation moderate at {deforestation_level}. Monitor for increase in level')
    elif 0.3 < deforestation_level <= 0.5:
        print(f'Deforestation high at {deforestation_level}. Notify authorities, initiate restoration 
              efforts')
    else:
        print(f'Deforestation critical at {deforestation_level}. Notify authorities, stop all activities,
               initialise restoration and close off area to public access')

