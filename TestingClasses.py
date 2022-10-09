from time import sleep
import SlidingWindow
import TimerList

windows_size = 3 # || [ ] [ ] [ ] || [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
initial_seq = 3  # || [3] [4] [5] || [6] [7] [8] [3] [4] [5] [6]
message = "Esta es una prueba de sliding window"
message_length = len(message.encode())

# Lista de Datos
data_list = [message_length, "Esta", " es ", "una ", "prue", "ba", "en sl", "idin", "g wi", "ndow"]

data_window = SlidingWindow.SlidingWindow(windows_size, data_list, initial_seq)

print(data_window)

data_window.move_window(3) # [3] [4] [5] || [6] [7] [8] || [3] [4] [5] [6]

print(data_window)

data_window.move_window(3) # [3] [4] [5] [6] [7] [8] || [3] [4] [5] || [6]

print(data_window)

data_window.move_window(3) # [3] [4] [5] [6] [7] [8] [3] [4] [5] || [6] None None||

print(data_window)

'''
Tiene pinta de que por "eficiencia" la sliding window reinicia la secuencia cuanda avanza 2*windows_size

+------+---------+---------+---------+
| Data | 36      | Esta    |  es     |
+------+---------+---------+---------+
| Seq  | Y+0 = 3 | Y+1 = 4 | Y+2 = 5 |
+------+---------+---------+---------+
+------+---------+---------+---------+
| Data | una     | prue    | ba      |
+------+---------+---------+---------+
| Seq  | Y+3 = 6 | Y+4 = 7 | Y+5 = 8 |
+------+---------+---------+---------+
+------+---------+---------+---------+
| Data | en sl   | idin    | g wi    |
+------+---------+---------+---------+
| Seq  | Y+0 = 3 | Y+1 = 4 | Y+2 = 5 |
+------+---------+---------+---------+
+------+---------+---------+---------+
| Data | ndow    | None    | None    |
+------+---------+---------+---------+
| Seq  | Y+3 = 6 | None    | None    |
+------+---------+---------+---------+
'''

print("numero de secuencia del tercer elemento de la ventana:")
print(data_window.get_sequence_number(2)) # 2 es el maximo indice, pues es una ventana de tamanho 3

print()
print("datos almacenados en el tercer elemento de la ventana:")
print(data_window.get_data(2))


timeout_value = 5 #  5 segundos de timeout
number_of_timers = 5 # Creamos 5 timers

timer_list = TimerList.TimerList(timeout_value, number_of_timers)

for timer_index in range(number_of_timers):
    timer_list.start_timer(timer_index) # Iniciamos los timers
    sleep(1)

while True:
    finished_timers = timer_list.get_timed_out_timers() # obtenemos una lista de los timers que terminaron.
    if len(finished_timers) == 5:
        print(finished_timers)
        break
    print(finished_timers)
    sleep(1)