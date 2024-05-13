import streamlit as st
import subprocess
import shlex

def send_ao_command(command):
    """Safely sends a command to the AOS CLI and returns the output or error."""
    try:
        # Using subprocess.run for better security practices
        result = subprocess.run(
            ["aos"] + shlex.split(command),
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"

def main():
    st.title('AOS Message Sender UI')

    # Input fields for user to enter target and data
    target = st.text_input("Enter the target process ID:")
    data = st.text_area("Enter the message data:")

    # Button to send the message
    if st.button("Send Message"):
        command = f'Send({{Target="{target}", Data="{data}"}})'
        response = send_ao_command(command)
        st.text_area("Response from AOS", response, height=300)

if __name__ == "__main__":
    main()
