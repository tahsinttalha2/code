import streamlit as st
import os
from sys import exit
import sys
import subprocess
from hardware import SystemValidation
import signal

# prints badges based on gpu validation from SystemValidation
def is_gpu():
    is_gpu = SystemValidation().checker()
    
    if is_gpu and SystemValidation().one_gpu():
        st.badge("Success! We've found an Nvidia GPU", color="green", icon=":material/check_circle:")
        return True
    else:
        if not SystemValidation().one_gpu():
            st.badge("Failed! We can't process multiple Nvidia GPUs", color="red", icon=":material/cancel:")
        else:
            st.badge("Failed! We couldn't find Nvidia GPU", color="red", icon=":material/cancel:")
        
        return False
    
# ensure everything clears up from the first slide when button is clicked  
if "monitor_btn_clicked" not in st.session_state:
    st.session_state.monitor_btn_clicked = False
    st.session_state.second_window_clear = False
    st.session_state.engine_start = False

if "record_pid" not in st.session_state:
    st.session_state.record_pid = None

def monitor_btn_clicked():  # initiates the monitoring
    st.session_state.monitor_btn_clicked = True
def second_window_clear():  # clears out the second window
    st.session_state.second_window_clear = True 

# validate requirements in the first slide
def begining():
    # generate texts on the page
    st.title("Performance Analysis Application")
    st.write("by Tahsin Tasnim Talha (tahsinttalha)")

    st.write("Feel free to tap the start button when you want to start monitoring. We suggest you tap start and you would have 3 seconds to switch to your desired application. You can then use it for at most 6 hours straight. We would analyse your data and provide a result.")

    # just some fancy UX
    with st.status("Please wait while we test your system's eligibility...", state="running") as status:
        #time.sleep(1)
        status.update(
            label="Done", 
            state="complete", 
            )

    if is_gpu():   
        st.button(
            label="Start Monitoring", 
            icon=":material/folder_eye:", 
            type="primary", 
            width="stretch", 
            on_click=monitor_btn_clicked
            )
        st.caption("We don't collect your data. The temporary analysis files are stored on your device or deleted upon your concern.")
    else:
        exit("Please retry when you've an Nvidia GPU.")

# initiate terminating protocols
def terminate(string):
    st.button(
        label="End Monitoring",
        icon=":material/cancel:",
        type="primary",
        width="stretch",
        on_click=termination(string)
    )    

# terminates the monitoring
def termination(string):
    if string == "monitor_btn_clicked":
        st.session_state.monitor_btn_clicked = False
        st.session_state.second_window_clear = True
        st.session_state.engine_start = True
    else:
        st.session_state.second_window_clear = False
        st.session_state.engine_start = False

# start monitoring the system and record data on record.py
def run_monitoring():
    process = subprocess.Popen([sys.executable, "record.py"])
    st.session_state.record_pid = process.pid

def main():
    # this is the main executing block
    if st.session_state.monitor_btn_clicked:
        run_monitoring()

        #   <------ termination happens here ------->

        st.status(label="monitoring your performance...", state="running", width="stretch")        
        terminate("monitor_btn_clicked")

        #   <--------------------------------------->

    elif st.session_state.second_window_clear:
        if st.session_state.record_pid is not None:
            os.kill(st.session_state.record_pid, signal.SIGTERM)
        st.write("Second Window Clear!")
    
    # this block will only run in the first time
    else:
        begining()

if __name__ == "__main__":
    main()