import importlib
import listingfile

def changes():
    try:
        importlib.reload(listingfile)
        listingfile.print_changes()
    except:
        pass
for i in range(10):
    changes()
    
    input("Hit enter to reload")