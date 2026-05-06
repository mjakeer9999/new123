str_1 = "TTCGATCCATTG"
str_2 = "ATCAATCGATCG"

def hamming_loop(str_1, str_2):
    h_distance = 0
    for position in range(len(str_1)):
        if str_1[position] != str_2[position]:
            h_distance += 1
    return h_distance