import streamlit as st
from hardware import SystemValidation, DataCollection
from data_handler import FileHandling
import time
from sys import exit

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
        time.sleep(1.3)
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
    else:
        st.session_state.second_window_clear = False

strt_time = time.time()

# start monitoring the system every second
@st.fragment(run_every=1)
def run_monitoring():
    clct = DataCollection()
    FileHandling().add_data(clct.get_cpu_usage(), clct.get_gpu_usage(), clct.get_ram_usage(), clct.get_time(strt_time))

def main():
    # this is the main executing block
    if st.session_state.monitor_btn_clicked:
        global strt_time
        FileHandling().create_file()
        run_monitoring()

        #   <------ termination happens here ------->

        st.status(label="monitoring your performance...", state="running", width="stretch")        
        terminate("monitor_btn_clicked")

        #   <--------------------------------------->

    elif st.session_state.second_window_clear:
        st.write("Second Window Clear!")
    
    # this block will only run in the first time
    else:
        begining()

if __name__ == "__main__":
    main()