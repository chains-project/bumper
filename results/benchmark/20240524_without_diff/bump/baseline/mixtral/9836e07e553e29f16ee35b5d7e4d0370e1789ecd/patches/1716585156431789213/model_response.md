Here's the proposed patch for the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

The fix involves changing the import statement from `import static org.hamcrest.core.StringContains.stringContains;` to `import static org.hamcrest.CoreMatchers.StringContains.StringContains;`. This is necessary because the `StringContains` constructor has been moved from the `org.hamcrest.core` package to the `org.hamcrest.CoreMatchers` package in the new version of the library.