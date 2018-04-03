import whois
import pprint
import traceback

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print "Provide domain as the first argument"
        sys.exit(-1)

    domain = sys.argv[1]

    try:
        results = whois.query(domain, ignore_returncode=1, use_com_for_default_tld=1)

        if results:
            pprint.pprint(results.__dict__)
        else:
            print "None"

    except Exception as ex:
        traceback.print_exc()
        print ex.message
