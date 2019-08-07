from app import app
"""
    Script starts here. Start it from cmd. You need to pass login (-l=...) and password(-p=...) in github to start service correctly.
"""
import argparse
if __name__ == '__main__':
    # get keys from cmd: login and password in github for connection and requests for repos data
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", metavar='l', default="", help="Your login to authenticate in GIT")
    parser.add_argument("--password", metavar='p', default="", help="Your password to authenticate in GIT")
    args = parser.parse_args()
    from app.get_data import auth_list
    auth_list.extend([args.login, args.password])

    # app.debug = True    # only for debug
    app.run()