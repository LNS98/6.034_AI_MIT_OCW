#!/usr/bin/env python2


from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

from tests import backchain_to_goal_tree_4_getargs

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


# GOAL

#

def backchain_to_goal_tree(rules, hypothesis):


    if len(rules) == 0:
        return hypothesis

    # initilialise a new node which will contain all of the matching consequences
    goal_tree = OR()

    # try to match the hypothesis to a THEN statment in the rules
    for i in range(len(rules)):
        # get the other potential matching leaf
        rule = rules[i]

        # check if there is a match
        matching = match(rule.consequent()[0], hypothesis)

        # in not none you have found a match
        if matching != None:
            # get the consequent and the antecedent
            cns = rule.consequent()[0]
            ant = rule.antecedent()

            if isinstance(ant, list):
                sub = AND()

                if isinstance(ant, OR):
                    sub = OR()
                for statment in ant:
                    # print(statment)
                    # now recursivly call backchain on the ants statments
                    new_node = backchain_to_goal_tree(rules, populate(statment, matching))

                    sub.append(new_node)

                # sub.append(ant)
                goal_tree.append(sub)
            else:
                goal_tree.append(backchain_to_goal_tree(rules, populate(ant, matching)))


        else:
            goal_tree.append(hypothesis)

    return simplify(goal_tree)



# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(backchain_to_goal_tree_4_getargs()[0], backchain_to_goal_tree_4_getargs()[1])
