# Write a python program to implement simple question answering system that can answer following questions
print("Simple Question Answer System")
print("************************")
print("You May Ask About")
print("AI.")
print("Rational Agent")
print("Properties of rational agent.")
print("Laws of Thoughts.")
print("Turing Test")
while True:
  q=input("Enter a Question: ")
  v=q.find("AI")
  if v>=0:
    print("AI is the science and engineering of designing computer programs that can perform similar to human mind")
  if q.find("rational agent")>=0:
    print("A rational agent can be anything that makes decisions, typically a person, firm, machine, or software.")
  if q.find("laws of thoughts")>=0:
    print("(1) the law of contradiction, (2) the law of excluded middle, and (3) the principle of identity. ")
  if q.find("properties of rational agent")>=0:
    print("co operative autonomy reactive")
  if q.find("turing test")>=0:
    print("The Turing test, developed by Alan Turing in 1950, is a test of a machine's ability to exhibit intelligent behaviour")

