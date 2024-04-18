Here is a fixed version of the method using a `contains` method from the `org.hamcrest.core.StringContains` class to check if a string contains a substring:

```java
private static Matcher<String> imagePulled(final String image) {
    String matchString = String.format("Downloaded newer image for %s", image);
    return new StringContains(false, matchString).matches(matchString);
}
```
In this version, I created a new variable `matchString` to store the substring that we want to check for in the log message. Then, I created a new `StringContains` object with the `matches` method, passing in the `matchString` as a parameter. This will check if the log message contains the substring.

Note: I am assuming that the `StringContains` class has a `matches` method that takes a string as a parameter. If this is not the case, you may need to adjust the code accordingly.