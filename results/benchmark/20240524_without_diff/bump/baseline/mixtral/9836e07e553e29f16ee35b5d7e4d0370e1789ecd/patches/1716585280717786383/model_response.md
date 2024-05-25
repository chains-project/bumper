Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new ContainsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` constructor with the `ContainsString` constructor, which is the new name of the class in the updated library. This should fix the error message you provided.