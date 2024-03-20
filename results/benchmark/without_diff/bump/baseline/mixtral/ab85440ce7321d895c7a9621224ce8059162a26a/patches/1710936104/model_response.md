Here is a potential patch for the failing client code:
```java
private static Matcher<String> imagePulled(final String image) {
    String expectedLogMessage = String.format("Status: Downloaded newer image for %s", image);
    return is(containsString(expectedLogMessage));
}
```
Explanation:

* The error message suggests that there is a syntax error related to a missing semicolon. Looking at the code, I noticed that there is an extra parenthesis at the end of the `containsString` method call.
* To fix the issue, I created a new variable `expectedLogMessage` to store the string that we are looking for in the log message. This makes the code easier to read and helps avoid the syntax error.
* I then used the `expectedLogMessage` variable in the `containsString` method call.
* I kept the method signature and the return type the same, as specified in the prompt.
* I did not remove the `@Override` decorator, as there is no information about the superclass method.
* I did not use any removed library methods or introduce any new syntax errors.
* I only changed the code related to the failing method, as requested.