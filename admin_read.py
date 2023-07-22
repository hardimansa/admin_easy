def Auditor(configfile, auditfile):
        configfile = configfile
        auditfile = auditfile


        # open configuration, with read priv / format outputs 
        with open(configfile, 'r') as config:
                    x = ("{}".format(config.read()))
                    conf_final = (x.lstrip().splitlines())

        # open audit file, with read priv / format outputs 
        with open(auditfile, 'r') as audit:
                    y = ("{}".format(audit.read()))
                    audit_final = (y.lstrip().splitlines())

        ### check for instances of your keyword(s) against lines in the configuraiton file
        for lines in conf_final:
                for keywords in audit_final:
                        if keywords in lines:
                                print(lines)


if __name__ == '__main__':
    Auditor('exampleconfig.txt', 'exampleaudit.txt')





