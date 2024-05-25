Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` constructor from the `org.hamcrest.core` package with the `stringContains` method from the `org.hamcrest.CoreMatchers` package. This should fix the error message you provided, which indicates that the `StringContains` constructor cannot be applied to the given type.

Note that the `CoreMatchers` class is part of the Hamcrest library, which should be included in your project's dependencies. If you don't have the Hamcrest library in your project, you may need to add it as a dependency before this patch can work.