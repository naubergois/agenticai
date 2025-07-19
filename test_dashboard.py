import os
import glob
import subprocess
import streamlit as st

TEST_DIR = "phase_1"

st.title("Agentic Workflow Test Dashboard")

# Find all test scripts
TEST_PATTERN = os.path.join(TEST_DIR, "test_*.py")
TEST_SCRIPTS = sorted(glob.glob(TEST_PATTERN))

# Run selected test
def run_script(script_path):
    """Run a python script and capture its output."""
    result = subprocess.run(
        ["python", script_path], capture_output=True, text=True
    )
    return result.stdout + result.stderr

selected_test = st.selectbox("Select a test to run", TEST_SCRIPTS)

if st.button("Run Selected Test"):
    st.write(f"Running **{selected_test}**...")
    output = run_script(selected_test)
    st.text_area("Test Output", output, height=300)

if st.button("Run All Tests"):
    run_all = os.path.join(TEST_DIR, "run_all_tests.py")
    st.write("Running all tests...")
    output = run_script(run_all)
    st.text_area("All Tests Output", output, height=300)

# Display test logs if they exist
log_files = sorted(glob.glob(os.path.join(TEST_DIR, "test_output_*.txt")))
if log_files:
    st.header("Test Logs")
    for log in log_files:
        with st.expander(os.path.basename(log)):
            with open(log, "r", encoding="latin1") as f:
                st.text(f.read())

else:
    st.info("No log files found. Run a test to generate logs.")
