# handling errors
def Equal(param1, param2, param3):
	try: 
		value = False
		if int(param1) == int(param2) or int(param1) == int(param3) or int(param2) == int(param3):
			value = True
		else:
			value = False
	except ValueError:
		print("VALUE ERROR: Only numbers")
	except TypeError:
		print("TYPE ERROR: Only numbers")
	except Exception:
		print(Exception)
		print("Exception: only numbers")
	finally:
		print("Values:", param1, param2, param3)
		return value

print(Equal(6,5,"5"))
print(Equal("a", "b", "c"))

# I chose the third assigment and I modified it by putting try-except-finally blocks