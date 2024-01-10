import socket
import time

SERVER_IP = '90.23.20.72'
SERVER_PORT = 3196

CONN_TIMEOUT = 10
MAX_DATA_LENGTH = 200

class Questionnaire:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def do_socket_read(
        timeout,
        max_data_length):

        Questionnaire.conn.settimeout(CONN_TIMEOUT)

        start_time = time.clock()
        while time.clock() - start_time < timeout:
            Questionnaire.conn.connect((SERVER_IP, SERVER_PORT))

            data = None
            try:
                data = Questionnaire.conn.recv(max_data_length)
            except:
                return False

            if len(data) == max_data_length:
                if sum_of_data > 3000000:
                    return True

            if len(data) >= 150:
                if sum_of_data > 2000000:
                    return True

            else:
                if sum_of_data > 1000000:
                    return True
                else:
                    return False

        return False

Questionnaire.do_socket_read(CONN_TIMEOUT, MAX_DATA_LENGTH)