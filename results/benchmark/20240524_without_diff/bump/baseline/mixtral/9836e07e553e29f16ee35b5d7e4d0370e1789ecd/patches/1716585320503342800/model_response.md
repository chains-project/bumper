Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor from `org.hamcrest.core` with the `stringContains` method from `org.hamcrest.CoreMatchers`. This change is necessary because the `StringContains` constructor was removed in a later version of Hamcrest, and the recommended way to create a string contains matcher is now to use the `stringContains` method.

Note that the `CoreMatchers` class is a part of the Hamcrest library, so it should be available in the project's classpath. If the project doesn't include the Hamcrest library, it may need to be added as a dependency.