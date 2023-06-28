people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(type(people))

#sort dict will result in array and will return only keys -> list
print(sorted(people))
print(type(sorted(people)))

#sort dict based on keys -> list
print(sorted(people.items()))
print(type(sorted(people.items())))

#sort dict based on values -> list
print(sorted(people.items(), key=lambda x:x[1]))
print(type(sorted(people.items(), key=lambda x:x[1])))

#sort dict based on values -> dict
print(dict(sorted(people.items())))
print(type(dict(sorted(people.items()))))