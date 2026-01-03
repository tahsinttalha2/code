# project.py - Final Fix
import psutil
import win32gui
import win32process
import pynvml
import streamlit
import time as lib_time

# <--------------------- Measuring Hardware Performance -------------------------->

def crnt_process():
    """Safely gets the current foreground process."""
    try:
        app_handle = win32gui.GetForegroundWindow()
        if not app_handle:
            return None
        _, process_id = win32process.GetWindowThreadProcessId(app_handle)
        return psutil.Process(process_id)
    except Exception:
        return None

def gpu_performance():
    """Safely reads GPU data. Returns None if GPU is missing/fails."""
    try:
        # We assume nvmlInit() was called in main()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        
        # Load
        load = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        
        # Memory
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        usage = (mem_info.used / mem_info.total) * 100
        
        # Temp
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        return {
            "load": load,
            "usage": round(usage, 1),
            "temperature": temp
        }
    except Exception:
        return None

# <-------------------------- Creating the GUI --------------------------->

def main():
    streamlit.title("tahsinttalha's Performance Monitor App")

    # 1. Setup Interface Columns
    col_cpu, col_gpu, col_ram, col_time = streamlit.columns(4)
    with col_cpu: cpu_text = streamlit.empty()
    with col_gpu: gpu_text = streamlit.empty()
    with col_ram: ram_text = streamlit.empty()
    with col_time: timeline = streamlit.empty()

    # 2. Initialize Session State (Memory that survives reruns)
    if "data_chart" not in streamlit.session_state:
        streamlit.session_state.cpu_usage = []
        streamlit.session_state.gpu = []
        streamlit.session_state.ram_usage = []
        streamlit.session_state.time_log = []
        
        streamlit.session_state.run_switch = False
        streamlit.session_state.start_time = 0  # To track duration properly
        
        # Initialize GPU Driver safely once at startup
        try:
            pynvml.nvmlInit()
        except:
            pass 

    # 3. Control Buttons
    start, end = streamlit.columns(2)
    with start:
        if streamlit.button("Start"):
            streamlit.session_state.run_switch = True
            # [CRITICAL FIX] Set start time in session_state so it isn't lost on rerun
            streamlit.session_state.start_time = lib_time.time()

    with end:
        if streamlit.button("End"):
            streamlit.session_state.run_switch = False
            streamlit.rerun()

    # 4. The Engine (Runs only when switch is True)
    if streamlit.session_state.run_switch:
        
        process = crnt_process()
        
        if process:
            try:
                # [Data Collection]
                # interval=0.1 ensures we get a fresh reading, not a cached 0.0
                data_cpu = process.cpu_percent(interval=0.1)
                data_ram = round(process.memory_percent(), 1)
                data_gpu = gpu_performance()
                
                # [Time Logic]
                elapsed = lib_time.time() - streamlit.session_state.start_time
                data_time = round(elapsed, 1)

                # [Storage]
                streamlit.session_state.cpu_usage.append(data_cpu)
                streamlit.session_state.ram_usage.append(data_ram)
                streamlit.session_state.time_log.append(data_time)
                
                if data_gpu:
                    streamlit.session_state.gpu.append(data_gpu)

                # [Display Update]
                cpu_text.metric("CPU", f"{data_cpu}%")
                ram_text.metric("RAM", f"{data_ram}%")
                timeline.metric("Time", f"{data_time}s")
                
                if data_gpu:
                    # Show simple load % to keep UI clean
                    gpu_text.metric("GPU", f"{data_gpu['load']}%")
                else:
                    gpu_text.metric("GPU", "N/A")

            except Exception as e:
                # Shows error on screen instead of crashing silently
                streamlit.error(f"Error reading metrics: {e}")

        # [Heartbeat] Wait a bit, then refresh the screen
        lib_time.sleep(0.5)
        streamlit.rerun()

    # 5. Analysis Mode (Charts - only shows when stopped and has data)
    if not streamlit.session_state.run_switch and len(streamlit.session_state.time_log) > 0:
        streamlit.markdown("---")
        
        view_option = streamlit.radio(
            "Select Metric to Graph:", 
            ["CPU Usage", "RAM Usage", "GPU Load"], 
            horizontal=True
        )

        if view_option == "CPU Usage":
            streamlit.line_chart(streamlit.session_state.cpu_usage)