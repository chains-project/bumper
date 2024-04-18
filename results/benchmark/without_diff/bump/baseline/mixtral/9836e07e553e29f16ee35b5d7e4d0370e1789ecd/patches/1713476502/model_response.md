Here's a possible patch for the code you provided:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.<String>containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, we are using the `containsString` method from the `CoreMatchers` class, which is an added method in Hamcrest 2.2 (increased coverage). The `CoreMatchers` class is used to create matchers for testing. The `containsString` method checks if a string contains a specific substring. This should fix the error you encountered.