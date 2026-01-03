# libraries for system analysis
import psutil                       
import pynvml 

# libraries for file management                     
import streamlit    

# libraries for time management & GUI
import time as lib_time

# <---- Measuring Hardware Performance ---->

# track how long the process is running (seconds)
def time_tracker(start_time):
    crnt_time = lib_time.time()
    delta = crnt_time - start_time
    return delta

# track how much gpu is being used by the process and gpu temperature
def gpu_performance():
    gpu_count = pynvml.nvmlDeviceGetCount()

    for gpu in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu)
        load = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
        memory = memory.used * 100 / memory.total
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

    return {
            "load": load,
            "usage": memory,
            "temperature": temp
        }

# <---- Creating the GUI ---->

def main():
    streamlit.title("tahsinttalha's Performance Monitor App")

    # set up the columns
    col_cpu, col_gpu, col_ram, col_time = streamlit.columns(4)
    with col_cpu: cpu_text = streamlit.empty()
    with col_gpu: gpu_text = streamlit.empty()
    with col_ram: ram_text = streamlit.empty()
    with col_time: timeline = streamlit.empty()

    # keep the data safe when streamlit reruns
    if "data_chart" not in streamlit.session_state:
        streamlit.session_state.cpu_usage = []
        streamlit.session_state.gpu = []
        streamlit.session_state.ram_usage = []
        streamlit.session_state.time = []

        # assign switches to control the application
        streamlit.session_state.run_switch = False
        streamlit.session_state.nvml_switch = False
        streamlit.session_state.data_chart = True

    # assign short names for the lists (the data in data_chart)
    cpu_usage = streamlit.session_state.cpu_usage
    gpu_usage = streamlit.session_state.gpu
    ram_usage = streamlit.session_state.ram_usage
    time = streamlit.session_state.time
    
    # assign button to evoke the switches
    start, end = streamlit.columns(2)
    with start:
        if streamlit.button("Start"):
            streamlit.session_state.run_switch = True
            streamlit.session_state.nvml_switch = True
            streamlit.session_state.strt_time = lib_time.time()

    if streamlit.session_state.nvml_switch:
        pynvml.nvmlInit()
    
    with end:
        if streamlit.button("End"): 
            streamlit.session_state.run_switch = False

    # <-------------- implementing the application engine -------------->

    if streamlit.session_state.run_switch:
        # collecting data on cpu_usage, gpu_usage, ram_usage and elapsed time
        data_cpu = psutil.cpu_percent(interval=0.1)
        data_gpu = gpu_performance()
        data_gpu = round(data_gpu["usage"],2)
        data_ram = psutil.virtual_memory().percent
        data_time = round(time_tracker(streamlit.session_state.strt_time))

        # adding data to the lists
        cpu_usage.append(data_cpu)
        gpu_usage.append(data_gpu)
        ram_usage.append(data_ram)
        time.append(data_time)

        # adding live updates of the data
        cpu_text.metric("CPU : ", f"{data_cpu}%")
        gpu_text.metric("GPU Usage: ", f"{data_gpu}%")
        ram_text.metric("RAM : ", f"{data_ram}%")
        timeline.metric("Time Elapsed : ", f"{data_time} seconds")

        lib_time.sleep(0.5)
        streamlit.rerun()

    # create graphical tabs for user interests in usages
    if len(time) > 0 and not streamlit.session_state.run_switch:
        show_data = streamlit.radio(
            label="Change View: ", 
            options= ["All", "CPU Usage", "GPU Usage", "RAM Usage"],
            horizontal = True
        )

        chart = streamlit.empty()

        if show_data == "All":
            chart.line_chart(
                {
                 "CPU (%)": cpu_usage,
                 "GPU (%)": gpu_usage,
                 "RAM (%)": ram_usage
                }
            )
        elif show_data == "CPU Usage":
            chart.line_chart(cpu_usage)
        elif show_data == "GPU Usage":
            chart.line_chart(gpu_usage)
        elif show_data == "RAM Usage":
            chart.line_chart(ram_usage)

if __name__ == "__main__":
    main()