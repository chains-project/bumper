Here's the proposed patch for the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.Matchers.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

The fix involves changing the import statement from `import static org.hamcrest.CoreMatchers.StringContains;` to `import static org.hamcrest.Matchers.StringContains;`. It seems that the `StringContains` class has been moved to a different package in the updated version of the library.