import sys

def sanitize_input(raw_text):
    """
    PHASE 1: INPUT & SANITIZATION
    Converts text to lowercase and strips leading/trailing whitespaces.
    Ensures input normalization so variations like "HELLO " or "Hello" match cleanly.
    """
    return raw_text.lower().strip()

def process_logic(clean_text):
    """
    PHASE 2: PROCESS (The Logic Skeleton)
    Deterministic control flow using explicit if-elif-else gates.
    """
    # Greeting Intents
    if clean_text in ["hello", "hi", "hey", "greetings"]:
        return "Hello! I am your deterministic AI assistant. How can I help you today?"
    
    # Exit Intents
    elif clean_text in ["exit", "quit", "bye", "stop"]:
        return "EXIT_SIGNAL"
    
    # Informational / Domain Specific Intents
    elif "your name" in clean_text or "who are you" in clean_text:
        return "I am a Rule-Based AI Engine developed as part of my DecodeLabs Milestone 1."
    
    elif "project 1" in clean_text or "rule-based" in clean_text:
        return "Project 1 focuses on building a 'White Box' architecture using absolute logic gates instead of probabilistic engines."
    
    elif "guardrail" in clean_text or "safety" in clean_text:
        return "Rule-based systems serve as critical guardrails in modern apps (like NVIDIA NeMo) to filter probabilistic LLM outputs safely."
    
    # Fallback response for unhandled intents
    else:
        return "I'm sorry, I cannot process that intent. My hard-coded logic paths only recognize greetings, specific project queries, and exit commands."

def main():
    print("======================================================")
    print("    DECODELABS: DETERMINISTIC LOGIC CHATBOT ENGINE     ")
    print("          Type 'exit' or 'bye' to terminate.          ")
    print("======================================================")
    
    # PHASE 3: OUTPUT (Continuous Feedback Loop)
    while True:
        try:
            # Capture Raw Input
            user_raw = input("\nYou: ")
            
            # Step 1: Sanitize & Normalize
            clean_user_input = sanitize_input(user_raw)
            
            # Edge case: Skip empty hits
            if not clean_user_input:
                continue
                
            # Step 2 & 3: Process Intent and Check for Exit Signal
            bot_response = process_logic(clean_user_input)
            
            if bot_response == "EXIT_SIGNAL":
                print("Bot: Terminating continuous loop session. Goodbye!")
                break
                
            # Render Response Output
            print(f"Bot: {bot_response}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session interrupted. Exiting gracefully.")
            sys.exit(0)

if __name__ == "__main__":
    main()
