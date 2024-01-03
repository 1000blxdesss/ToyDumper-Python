import win32con, win32api, win32process
import psutil
import logging
logger = logging.getLogger(__name__)
def get_pid_by_name(name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == name:
            return proc.info['pid']
def dump_process_memory(pid, start_address, end_address, filename='dump.txt'):
    PROCESS_ALL_ACCESS = (win32con.PROCESS_VM_READ | win32con.PROCESS_QUERY_INFORMATION)
    process_handle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    with open(filename, 'wb') as file:
        current_address = start_address
        while current_address < end_address:
            size = min(4096, end_address - current_address)
            try:
                data = win32process.ReadProcessMemory(process_handle, current_address, size)
                file.write(data)
                current_address += size
            except win32process.error as e:
                print(f'Cannot read memory at address: 0x{current_address:X}: {e}')
                current_address += size
    win32api.CloseHandle(process_handle)