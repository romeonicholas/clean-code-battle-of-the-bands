# Code Smells

## Code smells from refactoring.guru:
* Duplicate code — Multiple functions return variations on the same thing and could be simplified
* Switch Statements — Multiple functions contain unnecessarily complex series of if/else statements

## Other concerns:
* Strings used repeatedly for equivalence checks, strings used for returns outside of formatter functions
* Functions performing more than one task (usually both a calculation and formatting)
* Naming convention concerns: variables like “getvotes” instead of “get_votes”, redefined Python’s built in “type” instead of using “vote_type” or similar
* status() is really confusing--it doesn't actually get or set _status, that's done by close()
* Inconsistent returns (every branch should return something, or none should)

### Can't be changed without changing tests:
Most of it. Function names and parameters are already being used by the tests, so trying to clean any of those would cause tests to fail even if the logic stayed the same. The places strings are returned can't be simplified for the same reason.

### Refactoring steps:
1. Simplifying Conditional Expressions (Consolidate Duplicate Conditional Fragments): vote() used four branches where three would suffice, and the conditions were in a less-than ideal order (unsuccessful returns on the first and last branch, instead of grouped together as guard clauses)

2. Simplifying Conditional Expressions: status() used nested if/else logic even though it didn't require it, so flattening those if/elses makes it a little clearer

3. Simplifying Conditional Expressions (Consolidate Duplicate Conditional Fragments): close() had two almost identical branches that could be combined into a single guard clause