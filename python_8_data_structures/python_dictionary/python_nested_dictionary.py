myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#2nd way
child4 = {
  "name" : "Emil",
  "year" : 2004
}
child5 = {
  "name" : "Tobias",
  "year" : 2007
}
child6 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child4" : child4,
  "child5" : child5,
  "child6" : child6
}
print(myfamily2)

#access item
print(myfamily["child2"]["name"])