# Create a function that accepts both *args and **kwargs
# *args should be a list of hobbies
# **kwargs should be personal details (name, age, city)
# Print the details first, then print hobbies

def hob_details(*args, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    for arg in args:
        print(arg, end=" ")

hob_details("Reading", "Writing", "Gaming", "SkyWatching",
            name="Kayleigh",
            age="23",
            city="Texas")