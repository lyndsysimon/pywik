pywik
=====

Python wrapper for the Piwik API.

# Quickstart

Connect to a running Piwik server:

    import Pywik
    
    connection = Pywik.Server(
        url='piwik.mydomain.com',
        auth_token='6a110eba31b4424558fb00c2a76f7380',
    )
   
    print(connection.version)
    > 2.7.0