Here's a possible patch for the given error:

```java
private Matcher<String> manifestPushed() {
    boolean isNegated = false;
    return new StringContains(isNegated, String.format("latest: digest: %s", this.image.digest()));
}
```
In the new version of the library, the constructor of `StringContains` has only one argument, so we need to remove the `false` argument. However, we still need to specify whether the matcher should be negated or not. To do this, we create a separate boolean variable `isNegated` and pass it as an argument. Since the original code did not use the `negate()` method, we initialize `isNegated` to `false`.