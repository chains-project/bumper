Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` class from Hamcrest with the `CoreMatchers.containsString` method from the same library. This method has the same behavior as `StringContains`, but it can be applied directly to a string, avoiding the need for the `Matcher` constructor.