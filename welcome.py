def get_welcome_message(name):
    if name.lower() == "arielle pine":
        return f"¡Ay, caramba! {name}! Don't have a cow, man! You're totally rad! 🍩"
    return f"Welcome, {name}! We're excited to have you here! 🎉"

def main():
    print("Hello! Let's get to know each other.")
    name = input("What's your name? ")
    welcome_message = get_welcome_message(name)
    print("\n" + welcome_message)

if __name__ == "__main__":
    main() <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Story Time</title>
    <!-- Google Fonts for cursive title -->
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet">
    <!-- Tailwind CSS CDN for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom font for a better look */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #ffcccc; /* Pink background */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }
        /* Basic styling for the main container */
        .container {
            background-color: #ffffff;
            border-radius: 15px; /* Rounded corners for the container */
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); /* Soft shadow */
            padding: 30px;
            max-width: 800px;
            width: 100%;
            text-align: center;
        }
        /* Style for the story display area */
        #story-display {
            background-color: #f9fafb; /* Slightly darker background for story */
            border-radius: 10px;
            padding: 20px;
            min-height: 150px;
            text-align: left;
            white-space: pre-wrap; /* Preserves whitespace and line breaks */
            margin-bottom: 20px;
            border: 1px solid #e5e7eb; /* Light border */
            max-height: 400px; /* Limit height */
            overflow-y: auto; /* Scroll if content overflows */
        }
        /* Style for choice buttons */
        .choice-button {
            /* Rainbow gradient background */
            background-image: linear-gradient(to right, #ff7e5f, #feb47b, #86a8e7, #91e8e1);
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease; /* Smooth transition for all changes */
            font-weight: 500;
            width: 100%; /* Full width for choices */
            margin-bottom: 10px;
            border: none; /* No border */
            background-size: 200% auto; /* For animation effect */
        }
        .choice-button:hover {
            background-position: right center; /* Move gradient on hover */
            transform: translateY(-2px); /* Slight lift effect */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Add shadow on hover */
        }
        .choice-button:active {
            transform: translateY(0);
        }
        .choice-button:disabled {
            background-image: linear-gradient(to right, #fca5a5, #fed7aa, #a7bceb, #a5e8e4); /* Lighter rainbow when disabled */
            cursor: not-allowed;
            box-shadow: none;
        }
        /* Style for primary action button */
        .primary-button {
            /* Another rainbow gradient for primary button */
            background-image: linear-gradient(to right, #a18cd1, #fbc2eb, #ffecd2, #fcb69f);
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            border: none;
            background-size: 200% auto;
        }
        .primary-button:hover {
            background-position: right center;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .primary-button:active {
            transform: translateY(0);
        }
        .primary-button:disabled {
            background-image: linear-gradient(to right, #c1aad1, #fbd2ef, #ffe6c2, #fcd0ba); /* Lighter gradient when disabled */
            cursor: not-allowed;
            box-shadow: none;
        }
        /* Style for input field */
        .input-field {
            border: 1px solid #d1d5db;
            border-radius: 8px;
            padding: 10px 15px;
            width: 100%;
            box-sizing: border-box;
            margin-bottom: 20px;
        }
        .input-field:focus {
            outline: none;
            border-color: #a18cd1; /* Matches a color from the primary button gradient */
            box-shadow: 0 0 0 3px rgba(161, 140, 209, 0.2);
        }
        /* Loading indicator styles */
        .loading-spinner {
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-top: 4px solid #a18cd1; /* Matches a color from the primary button gradient */
            border-radius: 50%;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
            display: none; /* Hidden by default */
        }
        .loading-spinner.active {
            display: block;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        /* Message box for alerts */
        #message-box {
            background-color: #fef2f2; /* Red-ish background for errors */
            color: #ef4444; /* Red text */
            border: 1px solid #fca5a5; /* Red border */
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
            display: none; /* Hidden by default */
            text-align: left;
            font-size: 0.9em;
        }
        /* Cursive font for the title */
        #main-title {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem; /* Larger font size for emphasis */
            /* Tailwind classes below are still applied */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 id="main-title" class="text-3xl font-bold text-rose-500 mb-6">🖊️ Story Time 🖊️</h1>

        <p class="text-gray-600 mb-4">Start a new story by giving me a prompt, then make choices to guide the narrative!</p>

        <input type="text" id="initial-prompt" class="input-field" placeholder="E.g., A wizard on a quest for a lost artifact in a magical forest...">

        <button id="start-story-button" class="primary-button w-full mb-6">Start Story</button>

        <div id="story-display" class="text-gray-700">
            Your story will appear here...
        </div>

        <div id="choices-container" class="space-y-3">
            </div>

        <div id="loading-spinner" class="loading-spinner mt-6"></div>

        <div id="message-box"></div>
    </div>

    <script type="module">
        // Get references to HTML elements
        const initialPromptInput = document.getElementById('initial-prompt');
        const startStoryButton = document.getElementById('start-story-button');
        const storyDisplay = document.getElementById('story-display');
        const choicesContainer = document.getElementById('choices-container');
        const loadingSpinner = document.getElementById('loading-spinner');
        const messageBox = document.getElementById('message-box');

        // Initialize chat history for the AI model
        let chatHistory = [];
        // The API key is left as an empty string; the environment will provide it at runtime.
        const apiKey = ""; // <--- PASTE YOUR GOOGLE CLOUD API KEY HERE!
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

        /**
         * Shows a message in the message box.
         * @param {string} message - The message to display.
         * @param {string} type - Type of message (e.g., 'error', 'info').
         */
        function showMessage(message, type = 'info') {
            messageBox.textContent = message;
            messageBox.style.display = 'block';
            // You can add different styling based on type here if needed
            if (type === 'error') {
                messageBox.style.backgroundColor = '#fef2f2';
                messageBox.style.color = '#ef4444';
                messageBox.style.borderColor = '#fca5a5';
            } else {
                messageBox.style.backgroundColor = '#eff6ff';
                messageBox.style.color = '#2563eb';
                messageBox.style.borderColor = '#bfdbfe';
            }
        }

        /**
         * Hides the message box.
         */
        function hideMessage() {
            messageBox.style.display = 'none';
        }

        /**
         * Enables or disables UI elements based on loading state.
         * @param {boolean} isLoading - True if loading, false otherwise.
         */
        function setLoading(isLoading) {
            startStoryButton.disabled = isLoading;
            initialPromptInput.disabled = isLoading;
            loadingSpinner.classList.toggle('active', isLoading);
            // Disable all choice buttons when loading
            const choiceButtons = choicesContainer.querySelectorAll('.choice-button');
            choiceButtons.forEach(button => button.disabled = isLoading);
        }

        /**
         * Clears all dynamically generated choice buttons.
         */
        function clearChoices() {
            choicesContainer.innerHTML = '';
        }

        /**
         * Generates the next part of the story and potential choices using the AI model.
         * @param {string} promptText - The text prompt for the AI.
         */
        async function generateStory(promptText) {
            setLoading(true);
            hideMessage();
            clearChoices(); // Clear previous choices before generating new ones

            try {
                // Add the user's prompt to the chat history
                chatHistory.push({ role: "user", parts: [{ text: promptText }] });

                // Define the payload for the API call.
                // We use a responseSchema to ask the model for a structured JSON output
                // containing the story segment and an array of choices.
                const payload = {
                    contents: chatHistory,
                    generationConfig: {
                        responseMimeType: "application/json",
                        responseSchema: {
                            type: "OBJECT",
                            properties: {
                                "storySegment": { "type": "STRING" },
                                "choices": {
                                    "type": "ARRAY",
                                    "items": { "type": "STRING" }
                                }
                            },
                            "propertyOrdering": ["storySegment", "choices"]
                        }
                    }
                };

                // Make the API call
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(`API error: ${response.status} - ${errorData.error.message || response.statusText}`);
                }

                const result = await response.json();

                // Check if the response structure is as expected
                if (result.candidates && result.candidates.length > 0 &&
                    result.candidates[0].content && result.candidates[0].content.parts &&
                    result.candidates[0].content.parts.length > 0) {

                    const jsonResponse = result.candidates[0].content.parts[0].text;
                    const parsedData = JSON.parse(jsonResponse);

                    const storySegment = parsedData.storySegment;
                    const choices = parsedData.choices;

                    // Append the AI's response to the chat history
                    chatHistory.push({
                        role: "model",
                        parts: [{ text: JSON.stringify(parsedData) }] // Store the structured response
                    });

                    // Update the story display
                    storyDisplay.textContent += `\n\n${storySegment}`;
                    storyDisplay.scrollTop = storyDisplay.scrollHeight; // Scroll to bottom

                    // Create choice buttons
                    if (choices && choices.length > 0) {
                        choices.forEach(choice => {
                            const button = document.createElement('button');
                            button.textContent = choice;
                            button.classList.add('choice-button');
                            button.addEventListener('click', () => selectChoice(choice));
                            choicesContainer.appendChild(button);
                        });
                    } else {
                        // If no choices, indicate the story might have ended or needs a new prompt
                        showMessage("The story seems to have reached a conclusion, or the AI couldn't provide more choices. Start a new one!", 'info');
                    }

                } else {
                    showMessage("Received an unexpected response from the AI. Please try again.", 'error');
                    console.error("Unexpected AI response structure:", result);
                }
            } catch (error) {
                console.error("Error generating story:", error);
                showMessage(`Failed to generate story: ${error.message}. Please check your prompt and try again.`, 'error');
            } finally {
                setLoading(false);
            }
        }

        /**
         * Handles a user's choice and continues the story.
         * @param {string} selectedChoice - The choice selected by the user.
         */
        function selectChoice(selectedChoice) {
            // Append the chosen action to the story display for context
            storyDisplay.textContent += `\n\n> You chose: "${selectedChoice}"`;
            storyDisplay.scrollTop = storyDisplay.scrollHeight;
            generateStory(`I chose: "${selectedChoice}". Continue the story and give me new choices.`);
        }

        // Event listener for the "Start Story" button
        startStoryButton.addEventListener('click', () => {
            const initialPrompt = initialPromptInput.value.trim();
            if (initialPrompt) {
                storyDisplay.textContent = ''; // Clear previous story
                chatHistory = []; // Reset chat history for a new story
                generateStory(`Start a story about: ${initialPrompt}. Provide the first segment and 2-3 choices for continuation.`);
            } else {
                showMessage("Please enter an initial prompt to start the story!", 'info');
            }
        });

        // Initial message when the page loads
        document.addEventListener('DOMContentLoaded', () => {
            storyDisplay.textContent = "Enter a prompt above and click 'Start Story' to begin your adventure!";
        });
    </script>
</body>
</html>

