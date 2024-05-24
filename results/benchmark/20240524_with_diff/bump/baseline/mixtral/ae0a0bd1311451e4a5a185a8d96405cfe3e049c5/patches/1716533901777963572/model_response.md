Here is the proposed patch:

```java
private Matcher<String> manifestPushed() {
    boolean ignoreCase = false;
    return new StringContains(ignoreCase, String.format("latest: digest: %s", this.image.digest()));
}
```

The `StringContains` constructor now requires a boolean argument `ignoreCase` in addition to the string argument. The original code only passed one argument, which caused the compilation error. The patch initializes `ignoreCase` to `false` and passes it to the constructor.