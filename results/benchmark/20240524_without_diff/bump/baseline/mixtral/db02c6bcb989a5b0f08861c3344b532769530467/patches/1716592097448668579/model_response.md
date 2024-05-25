Here is a possible patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` class from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This is because the `StringContains` constructor is no longer available in the version of Hamcrest that you are using. By using `containsString`, you can achieve the same functionality without relying on the deprecated constructor.