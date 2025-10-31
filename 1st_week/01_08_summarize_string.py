input_str = "acccdeee"

def summarize_string(input_str):
    char_count_array = [0] * 26


    for c in input_str:
        char_count_array[ord(c) - ord('a')] += 1

    output_str = ""
    for index, count in enumerate(char_count_array):
        if count == 0:
            continue
        else:
            output_str += chr(index + ord('a'))
            output_str += str(count)
            output_str += "/"

    return output_str[:len(output_str)-1]

print(summarize_string(input_str))