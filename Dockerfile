# Use the Chainguard Python base image (with development tools)
FROM cgr.dev/chainguard/python:latest-dev

# Set the working directory inside the container
WORKDIR /app
ENV OLLAMA_HOST="http://host.docker.internal:11434"

USER root

# Copy the Python script into the container
COPY chat_demo.py /app/

# Install Python dependencies (including LangChain and OpenAI API)
RUN pip install --no-cache-dir langchain langchain-ollama langchain_community

USER 65532

# Expose port (optional, if you're running a web-based demo)
EXPOSE 8888

# Set the default command to run the chat demo
CMD ["chat_demo.py"]
