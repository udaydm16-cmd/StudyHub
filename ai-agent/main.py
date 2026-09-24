from agent import StudyHubAgent


agent = StudyHubAgent()

print("=================================")
print("       STUDY HUB AI AGENT")
print("=================================")
print("Type 'exit' to stop.\n")

while True:

    question = input("Teacher: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = agent.answer(question)

    print("\nStudy Hub AI:")
    print(answer)