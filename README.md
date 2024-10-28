# AI stuff

## Directions
1. Install [Ollama](https://ollama.com/) to run LLMs locally on your Mac.  OpenAI API keys wear out fast and get expensive.  Your laptop is pretty powerful and can do a lot of this already.
2. Once it's installed, launch it in the terminal with `ollama run llama3.1`.  This will start the server and you can access it at `http://localhost:11434` or on the command line.  This model works is a general purpose one that works well enough and seems appropriately sized to also build containers on the laptop.
3. Make sure Podman is running on your machine
4. Build the `Dockerfile` and run it.

    ```shell
    podman build -t test .
    podman run --rm -it test
    ```

5. Chat with your bot.  This should get you some nice output, as shown below:

    ```plaintext
    Chatbot is running! Type 'exit' to stop.
    User: test
    Assistant: Hello! I'm here to help with any questions or tasks you might have. What's on your mind?
    User: hi there, how are you today?
    Assistant: I'm doing great, thanks for asking! I'm here to help with any questions or tasks you may have. How can I assist you today? Is there something on your mind that you'd like to talk about or a problem you're trying to solve?
    User: what color are cornflowers?
    Assistant: Cornflowers are typically blue in color, although some varieties can have white or pink flowers as well. The traditional and most iconic shade of a cornflower is a bright, clear blue. Would you like to know more about cornflowers?
    ```
