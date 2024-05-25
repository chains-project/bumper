Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This should fix the error message you provided.

Note that the `CoreMatchers` class is part of the Hamcrest library, which is a dependency of the JUnit testing framework. If your project is using a version of Hamcrest that does not include the `CoreMatchers` class, you may need to update your Hamcrest dependency to a newer version.