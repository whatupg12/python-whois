import whois
import pprint

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print "Provide domain as the first argument"
        sys.exit(-1)

    domain = sys.argv[1]
    results = whois.query(domain, ignore_returncode=1, use_com_for_default_tld=1)

    pprint.pprint(results.__dict__)
