Here's a fixed version of the `manifestPushed` method that should work with the updated library version:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

In the original code, the `StringContains` constructor was being called with two arguments (`false` and a formatted string), but the updated constructor only accepts a single string argument.

To fix the issue, we can remove the `false` argument and format the string separately before passing it to the constructor. This results in code that is equivalent to the original, but should now be compatible with the updated library version.