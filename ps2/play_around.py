#!/usr/bin/env python2


from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain

theft_rule = IF( 'you have (?x)',
 THEN( 'we have (?x)' ),
 DELETE( 'you have (?x)' ))

data = ( 'you have apple',
 'you have orange',
 'you have pear' )


print forward_chain([theft_rule], data, verbose=False)
