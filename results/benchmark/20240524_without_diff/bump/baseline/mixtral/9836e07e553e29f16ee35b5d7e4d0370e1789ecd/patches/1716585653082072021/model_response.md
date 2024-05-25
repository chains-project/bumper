Here's a possible patch that you can apply to the code in order to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we've changed the import statement from `org.hamcrest.core.StringContains` to `org.hamcrest.CoreMatchers.StringContains`. This is because the `StringContains` class has been moved to a different package in the newer version of the library. By using the fully-qualified name of the class, we can ensure that the code will work correctly even if the import statement is not updated.

Note that I've used `org.hamcrest.CoreMatchers.StringContains` as an added library method identified with `++`. This is because the `StringContains` class has been added to the `CoreMatchers` class in the newer version of the library.

Also, I've changed nothing in the code except for the import statement, because it's unnecessary to change anything else in this specific case.