Here's the fixed method using a different approach to create the `Matcher`:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringStartsWith<>("Status: Downloaded newer image for ").matches(String.format("%s", image));
}
```

This version uses the `StringStartsWith` matcher, which checks if the input string starts with the specified prefix. Then, it combines it with the `matches` matcher to ensure the input string has the correct format.