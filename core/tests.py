from subprocess import run, PIPE


def assert_output(input, output):
    p = run('./app_with_omdbapi.py', stdout=PIPE, input=input.encode('ascii'))
    assert output.encode("ascii") in p.stdout, "Didn't run with your input"


if __name__ == '__main__':
    assert_output("OK\nhttp://172.26.8.77:8000/api/movies\npost\n\n\n\n\n", "<400> Saved in error_log/")
    assert_output("OK\n\n\nget\napikey=c60fe8f4\ns=mark\n\naccept:text/html\n\n\n\n", "<200> Saved in response_data/")
    assert_output("OK\nhttps://od-api.oxforddictionaries.com:443/api/v1/inflections/en/swimming\nget\n\napp_id:7bae2d70\napp_key:4b0aad78943b009ec26c46ed3de2ee8c\n\n\n\n", "<200> Saved in response_data/")
    print("Tests passed.")

