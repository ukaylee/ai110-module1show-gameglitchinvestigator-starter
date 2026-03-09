# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

It keeps telling me to go lower even though I already went to 1. Then it keeps telling me to go higher even though I already went to 100. I would expect it to do the opposite.

It won't let me make a new game.

It doesn't make an error if I go out of bounds, it just records it as a guess.

When I change the difficulty, it doesn't change the range to guess by.

It doesn't log some attempts and doesn't give feedback for some events.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used AI as a teammate to identify the lines of code that were producing my bugs.
Question 1: I used Copilot and Claude.
Question 2: Copilot gave me the fix for fixing "Too high" and "Too low" being inverted. It suggested just switching the text and I verified the result because it was what I would have done too.
Question 3: It told me to change st.session_state.status to be 1 when a new game was played, but I thought it should be 0 because there are no attempts at the start of a game.
I tested by playing around with it in the actual game and trying to "break" it.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was really fixed by testing it out a few times on the actual game. One test I ran was checking if we could make a new game, and it was correctly resetting the state and getting me a new game, so I thought it was good. AI helped me make the tests by writing the test suite.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because whenever we interacted with the game, streamlit does a rerun. So I think it would run "secret = random.randint(low, high)" every time and not preserve the state.

A Streamlit rerun happens when the app re-executes the entire Python script from top to bottom. Since this happens every time a user interacts with stuff, state can be lost, so streamlit provides st.session_state to keep it.

That's why to give it a stable secret number, the work around is to do st.session_state.secret so that we can keep it.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to use AI to make test cases and troubleshoot issues that I encounter so that it can explain to me what is going on so that I could approach it and find an answer.

One thing I would do differently is to be more careful when coding with AI and to review it more to ensure it is going to do what it should.

This project changed the way I think about AI code by teaching me to recognize that AI is prone to small bugs that change the way things function, and also that AI is good at refactoring and explaining.
