from SQLUtils import SQLUtils

def show_result(sql_result):
    for row in sql_result:
        print(row)


def col_chars(result_key_object):
    header_chars = []
    for key in result_key_object:
        header_chars += [len(key)]
    return(header_chars)

def parse_header(result):
    keys = result.keys()
    header_line = "| " + " | ".join(keys) + " |"
    print(header_line)
    print("-"*len(header_line))

def parse_line(result_line, col_size_array):
    out_line_array = []
    for idx in range(len(result_line)):
        init_length = len(result_line[idx])
        init_limit = col_size_array[idx]
        if init_length > init_limit:
            bit_out = result_line[idx][:init_limit-1] + "..."
            out_line_array += [bit_out]
        else:
            out_line_array += [result_line[idx].center(init_limit+2, " ")]
    line_out = "|" + "|".join(out_line_array) + "|"
    print(line_out)

def run_query_and_print_result(query):
    query_result = sql_engine.execute(query)

    print("Fetched {} rows".format(query_result.rowcount))

    col_size_limits = col_chars(query_result.keys())
    parse_header(query_result)

    for i in query_result:
        parse_line(i, col_size_limits)

    print("="*(sum(col_size_limits)+1+(len(col_size_limits)*3)))

if __name__ == "__main__":

    db_name = input("database name: ")

    try:
        sql_engine = SQLUtils(db_name=db_name)
    except Exception as err:
        print("Could not connect to {}. There is a good chance that the db doesn't exist!\nERROR: {}".format(db_name, err))



    quitter = None

    while not quitter:
        interaction = input("Enter Query (type 'kill' to exit): ")
        if interaction.lower() == "kill":
            break
        elif len(interaction) < 1:
            print("Query too small!")
            continue
        else:
            try:
                run_query_and_print_result(interaction)
            except Exception as err:
                print("Could not execute query as typed: {}\nERROR: {}".format(interaction,err))
                continue
print("Goodbye!")


