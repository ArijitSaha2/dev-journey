# Create a function using **kwargs
# Accept any number of key=value pairs about a person
# Print each detail on a new line formatted as "Key: Value"
# Call it with at least 5 details

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


info(Name="Antony Starr",
     Country="Australia",
     Role="Homelander",
     Seasons="#1-5",
     Show="The Boys")