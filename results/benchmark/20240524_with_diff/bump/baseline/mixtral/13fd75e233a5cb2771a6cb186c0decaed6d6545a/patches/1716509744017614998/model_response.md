Here's the proposed patch to fix the error:

```java
private Matcher<String> manifestPushed() {
    boolean ignoreCase = false;
    return new StringContains(ignoreCase, String.format("latest: digest: %s", this.image.digest()));
}
```

The `StringContains` constructor now requires a boolean argument `ignoreCase` as its first parameter. To fix the error, we can create a new variable `ignoreCase` with a value of `false` and pass it as the first argument to the `StringContains` constructor. This will make the code compatible with the new library version.